#!/usr/bin/env python3
"""Extract questions from .docx files (ZIP archives) and output as JSON.

Supports TWO source formats:

Format 1 (inline) - used by Fan 1 & Fan 2:
   One paragraph per question:
   "Question text?A) correct B) wrong C) wrong D) wrong"

Format 2 (multiline) - used by Fan 3:
   "12. Question text?"   (numbered)
   "a) correct"
   "b) wrong"
   "c) wrong"
   "d) wrong"

In BOTH formats option A / a) is the correct answer.
"""
import zipfile
import re
import sys
import html
import json


def extract_docx_paragraphs(path):
    """Extract text paragraphs from a docx file."""
    with zipfile.ZipFile(path) as z:
        with z.open('word/document.xml') as f:
            xml = f.read().decode('utf-8', errors='replace')

    paragraphs = []
    for p_match in re.findall(r'<w:p[ >].*?</w:p>', xml, flags=re.DOTALL):
        # Match <w:t> or <w:t ...> but NOT <w:tab .../>
        texts = re.findall(r'<w:t(?: [^>]*)?>(.*?)</w:t>', p_match, flags=re.DOTALL)
        para = ''.join(texts)
        para = html.unescape(para).strip()
        if para:
            paragraphs.append(para)
    return paragraphs


# ---------------- Format 1: inline ----------------

def parse_inline(para):
    """Parse single-paragraph 'Q?A) .. B) .. C) .. D) ..' format."""
    markers = {}
    for letter in ['A', 'B', 'C', 'D']:
        m = re.search(r'%s\)' % letter, para)
        if not m:
            return None
        markers[letter] = m.start()

    a, b, c, d = markers['A'], markers['B'], markers['C'], markers['D']
    if not (a < b < c < d):
        return None

    question = para[:a].strip()
    opt_a = para[a + 2:b].strip()
    opt_b = para[b + 2:c].strip()
    opt_c = para[c + 2:d].strip()
    opt_d = para[d + 2:].strip()

    if len(question) < 5 or not (opt_a and opt_b and opt_c and opt_d):
        return None

    return {'question': question, 'correctAnswer': opt_a, 'wrong': [opt_b, opt_c, opt_d]}


def parse_file_inline(paras):
    out = []
    for para in paras:
        parsed = parse_inline(para)
        if parsed:
            out.append(parsed)
    return out


# ---------------- Format 2: multiline ----------------

QUESTION_RE = re.compile(r'^\s*(\d+)\s*[\.\)]\s*(.*)$')
# Allow an optional leading bullet marker (•, -, *, etc.) before the option letter
OPTION_RE = re.compile(r'^\s*(?:[\u2022\u25aa\u25e6\u00b7\-\*o]\s*)?([a-dA-D])\s*\)\s*(.*)$')


def parse_file_multiline(paras):
    out = []
    i = 0
    n = len(paras)
    while i < n:
        qm = QUESTION_RE.match(paras[i])
        if not qm:
            i += 1
            continue
        # Collect question text (may span the numbered line + following non-option lines)
        q_parts = []
        first = qm.group(2).strip()
        if first:
            q_parts.append(first)
        j = i + 1
        # gather extra question lines before the first option
        while j < n and not OPTION_RE.match(paras[j]) and not QUESTION_RE.match(paras[j]):
            q_parts.append(paras[j].strip())
            j += 1
        # gather options
        options = {}
        while j < n:
            om = OPTION_RE.match(paras[j])
            if not om:
                break
            letter = om.group(1).lower()
            options[letter] = om.group(2).strip()
            j += 1
            if letter == 'd':
                break
        # Build question if we have a,b,c,d
        if all(k in options and options[k] for k in ['a', 'b', 'c', 'd']):
            # Prefer the line ending with '?' as the question if multiple parts
            q_with_qmark = [p for p in q_parts if p.rstrip().endswith('?')]
            if q_with_qmark:
                question = q_with_qmark[-1]
            else:
                question = ' '.join(q_parts)
            question = question.strip()
            if len(question) >= 5:
                out.append({
                    'question': question,
                    'correctAnswer': options['a'],
                    'wrong': [options['b'], options['c'], options['d']],
                })
        i = j if j > i else i + 1
    return out


def clean_text(t):
    """Normalize text: strip markdown bold, bullets, stray markers, collapse whitespace."""
    t = t.replace('**', '').replace('\u200b', '')
    t = re.sub(r'\s+', ' ', t).strip()
    # Remove stray leading bullets / markers
    t = re.sub(r'^[\u2022\u25aa\u25e6\u00b7\-\*]+\s*', '', t)
    # Remove stray trailing markers like '+' or bullets sometimes left from source
    t = re.sub(r'\s*[\+\u2022]+\s*$', '', t)
    return t.strip()


def norm_key(t):
    """Normalization key for dedup."""
    return re.sub(r'[^a-z0-9]', '', clean_text(t).lower())


def main():
    files = [
        ('Turizm loyihasini boshqarish', '(1-fan)TURIZM LOYIHASINI BOSHQARISH.docx'),
        ('Menejmentga kirish', '(2-fan) Menejmentga kirish.docx'),
        ('Madaniyatlararo muloqot', '(3-fan) Madaniyatlararo muloqot .docx'),
    ]

    all_questions = []
    seen = set()
    qid = 1
    summary = {}
    for subject, fname in files:
        paras = extract_docx_paragraphs(fname)
        # Run BOTH parsers (files may mix inline + multiline formats)
        combined = parse_file_inline(paras) + parse_file_multiline(paras)
        added = 0
        for p in combined:
            q = clean_text(p['question'])
            key = norm_key(q)
            if not key or key in seen:
                continue
            seen.add(key)
            all_questions.append({
                'id': qid,
                'subject': subject,
                'question': q,
                'correctAnswer': clean_text(p['correctAnswer']),
                'wrong': [clean_text(w) for w in p['wrong']],
            })
            qid += 1
            added += 1
        summary[subject] = added

    sys.stderr.write('SUMMARY:\n')
    for s, c in summary.items():
        sys.stderr.write('  %s: %d\n' % (s, c))
    sys.stderr.write('  TOTAL: %d\n' % len(all_questions))

    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
