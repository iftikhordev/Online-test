#!/usr/bin/env python3
"""Inject questions.json into index.html at the __QUESTION_BANK__ placeholder."""
import json

with open('questions.json', encoding='utf-8') as f:
    questions = json.load(f)

# Compact but readable: one question object per line
lines = []
for q in questions:
    obj = {
        'id': q['id'],
        'subject': q['subject'],
        'question': q['question'],
        'correctAnswer': q['correctAnswer'],
        'wrong': q['wrong'],
    }
    lines.append('  ' + json.dumps(obj, ensure_ascii=False))

array_text = '[\n' + ',\n'.join(lines) + '\n]'

with open('index.html', encoding='utf-8') as f:
    html = f.read()

if '__QUESTION_BANK__' not in html:
    raise SystemExit('Placeholder __QUESTION_BANK__ not found (already injected?)')

html = html.replace('__QUESTION_BANK__', array_text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Injected {len(questions)} questions into index.html')
