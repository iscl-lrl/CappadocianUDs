#!/usr/bin/env python3

#import numpy as np
from conllu import conllu_sentences

infile = 'AnnotationsFinal/AnnotationsFinal.conllu'

sentlen = []
postags = []
feats = []
multi = 0
for sent in conllu_sentences(infile):
    sentlen.append(len(sent))
    for tok in sent.nodes[1:]:
        postags.append(tok.upos)
        if tok.feats and tok.feats != '_':
            tokfeats = tok.feats.split('|')
            if tokfeats:
                feats.extend([f.split('=') for f in tokfeats])
        print(tok.form, tok.multi)

print(f"Sentences: {len(sentlen)}")
print(f"Tokens: {len(postags)}")
print(f"Avglen (tokens): {sum(sentlen)/len(sentlen)}")
print(f"Avglen (words): {(sum(sentlen)-multi)/len(sentlen)}")
