#!/usr/bin/env python3
"""Inject questions.json into index.html at the __RAW__ placeholder.

Converts each question to the RAW format used by the Silk Road style UI:
    { topic, q, opts:[correctAnswer, wrong0, wrong1, wrong2] }
opts[0] is always the correct answer; it is shuffled across A-D at runtime.
"""
import json

with open('questions.json', encoding='utf-8') as f:
    questions = json.load(f)

lines = []
for q in questions:
    obj = {
        'topic': q['subject'],
        'q': q['question'],
        'opts': [q['correctAnswer']] + q['wrong'],
    }
    lines.append('  ' + json.dumps(obj, ensure_ascii=False))

array_text = '[\n' + ',\n'.join(lines) + '\n]'

with open('index.html', encoding='utf-8') as f:
    html = f.read()

if '__RAW__' not in html:
    raise SystemExit('Placeholder __RAW__ not found (already injected?)')

html = html.replace('__RAW__', array_text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Injected {len(questions)} questions into index.html')
