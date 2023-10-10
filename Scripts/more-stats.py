#!/usr/bin/env python3

#import numpy as np
from conllu import conllu_sentences
from collections import Counter

infile = 'AnnotationsFinal/AnnotationsFinal.conllu'

sentlen = []
postags = []
feats = []
multi = 0
for sent in conllu_sentences(infile):
    sentlen.append(len(sent))
    multi += len(sent.multi)
    for tok in sent.nodes[1:]:
        postags.append(tok.upos)
        if tok.feats and tok.feats != '_':
            tokfeats = tok.feats.split('|')
            if tokfeats:
                feats.extend([tuple([tok.upos] + f.split('=')) for f in tokfeats])

print(f"Sentences: {len(sentlen)}")
print(f"Tokens: {len(postags)}")
nfeatval = len(set(feats))
nfeat = len(set([fv[0] for fv in feats]))
print(f"Avglen (tokens): {sum(sentlen)/len(sentlen)}")
print(f"Avglen (words): {(sum(sentlen)-multi)/len(sentlen)}")

#print(f"Features: ", Counter([(fv[0], fv[1]) for fv in feats]).most_common())
for p, f in sorted(set([(fv[0], fv[1]) for fv in feats])):
    print(p, f)
print(f"Features/values: ", Counter(feats).most_common())
