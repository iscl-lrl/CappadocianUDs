#!/usr/bin/env python3

from transliterate import translit
from conllu import conllu_sentences

infile = 'AnnotationsFinal/AnnotationsFinal.conllu'

sentences = []
for sent in conllu_sentences(infile):
    for i in range(len(sent.comment)):
        if sent.comment[i].startswith('# text = '):
            tr = translit(sent.comment[i][8:], 'el', reversed=True)
            sent.comment.insert(i + 1, "# translit = " + tr)
            break
    sentences.append(sent)

for sent in sentences:
    print(sent)
