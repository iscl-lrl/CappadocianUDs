#!/usr/bin/env python3

from conllu import conllu_sentences
import glob
import os
from sklearn.metrics import cohen_kappa_score, confusion_matrix

dir1 = 'Evaluation/NewSentencesInessa'
dir2 = 'Evaluation/NewSentencesEleni'

pos1, pos2, rel1, rel2 = [], [], [], []
n, posmatch, labelmatch, headmatch, relmatch = 0, 0, 0, 0, 0
for f1 in glob.glob(os.path.join(dir1, '*.conllu')):
    f2 = os.path.join(dir2, os.path.basename(f1))
    try:
        sent1 = list(conllu_sentences(f1))[0]
    except:
        print(f"Failed processing. {f1}")
        continue
    try:
        sent2 = list(conllu_sentences(f2))[0]
    except:
        print(f"Failed processing. {f2}")
        continue
    if len(sent1) != len(sent2):
        print(f"length mismatch {f1} ({len(sent1)}) {f2} ({len(sent2)})")
        continue
    for i, n1 in enumerate(sent1.nodes[1:], start=1):
        n2 = sent2.nodes[i]
        if n1.upos == '_' or n2.upos == '_':
                continue
        if n1.deprel == '_' or n2.deprel == '_':
                continue
#        if n1.upos == 'PUNCT' or n2.upos == 'PUNCT':
#                continue
        pos1.append(n1.upos), pos2.append(n2.upos)
        rel1.append(n1.deprel), rel2.append(n2.deprel)
        if n1.upos == n2.upos: posmatch += 1
        if n1.deprel == n2.deprel: labelmatch += 1
        if n1.head == n2.head:
            headmatch += 1
            if n1.deprel == n2.deprel:
                relmatch += 1
        n += 1

print(f"POS:    {100*posmatch/n:0.2f}%")
kpos = cohen_kappa_score(pos1, pos2)
print(f"POS-κ:  {100*kpos:0.2f} ")
print(f"rlab:   {100*labelmatch/n:0.2f}%")
lpos = cohen_kappa_score(rel1, rel2)
print(f"rlab-κ: {100*lpos:0.2f}%")
print(f"uaa:    {100*headmatch/n:0.2f}%")
print(f"laa:    {100*relmatch/n:0.2f}%")

plabels = sorted(set(pos1)|set(pos2))
cpos = confusion_matrix(pos1, pos2, labels=plabels)
for i, l in enumerate(plabels):
    fmt = "{:3d} " * len(cpos[0])
    print(f"{l:<10}", fmt.format(*cpos[i]))
print()
rlabels = sorted(set(rel1)|set(rel2))
crel = confusion_matrix(rel1, rel2, labels=rlabels)
for i, l in enumerate(rlabels):
    fmt = "{:3d} " * len(crel[0])
    print(f"{l:<10}", fmt.format(*crel[i]))

print(f"{n} tokens.")
# for sent in conllu_sentences(infile):
#     for i in range(len(sent.comment)):
#         if sent.comment[i].startswith('# text = '):
#             tr = translit(sent.comment[i][8:], 'el', reversed=True)
#             sent.comment.insert(i + 1, "# translit = " + tr)
#             break
#     sentences.append(sent)
# 
# for sent in sentences:
#     print(sent)
