#!/usr/bin/env python3

#import numpy as np
from conllu import conllu_sentences
from collections import Counter
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('input', nargs="*")
ap.add_argument('--output-postposed', '-p')
ap.add_argument('--output-preposed', '-P')
ap.add_argument('--output-leftobj', '-o')
args = ap.parse_args()

if not args.input:
    args.input = ["AnnotationsFinal/AnnotationsFinal.conllu"]

sentlen = []
postags = []
feats = []
multi = 0
nprep, npostp = 0, 0
postposed = []
preposed = []
leftobj = []
gender = []
objvroot, sbjvroot = [0,0], [0,0]
for infile in args.input:
    for sent in conllu_sentences(infile):
        sentlen.append(len(sent))
        multi += len(sent.multi)
        for tok in sent.nodes[1:]:
            postags.append(tok.upos)
            if tok.upos == 'NOUN':
                gender.append(tok.get_feat('Gender'))
            if tok.upos == 'ADP':
                if tok.index > tok.head:
                    npostp += 1
                    if args.output_postposed:
                        postposed.append(sent)
                else:
                    nprep += 1
                    if args.output_preposed:
                        preposed.append(sent)
            if tok.upos == 'VERB' and tok.head == 0:
                for c in sent.children_of(tok):
                    if c.deprel in {'obj', 'ccomp'}: # skipping xcomp
                        if c.index < tok.index: # left object
                            objvroot[0] += 1
                            if args.output_leftobj:
                                leftobj.append(sent)
                        else:
                            objvroot[1] += 1
                    if c.deprel in {'nsubj', 'csubj'}: 
                        if c.index < tok.index: # left subject
                            sbjvroot[0] += 1
                        else:
                            sbjvroot[1] += 1
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

print(f"Prepostions: {nprep}, postpositions: {npostp}")
print(f"Postposition ratio: {npostp/(nprep+npostp)}")

gcount = Counter(gender)
print("Gender distribution: ", gcount.most_common(), sum(gcount.values()))

if args.output_postposed:
    with open(args.output_postposed, 'wt') as fout:
        for sent in postposed:
            print(sent, file=fout)

if args.output_preposed:
    with open(args.output_preposed, 'wt') as fout:
        for sent in preposed:
            print(sent, file=fout)

print("Object distribution (left, right):", objvroot)
print("Left object ratio:", objvroot[0]/sum(objvroot))
print("Subject distribution (left, right):", sbjvroot)
print("Right subject ratio:", sbjvroot[1]/sum(sbjvroot))

if args.output_leftobj:
    with open(args.output_leftobj, 'wt') as fout:
        for sent in leftobj:
            print(sent, file=fout)
