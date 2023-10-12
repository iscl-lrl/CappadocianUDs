#!/usr/bin/env python3

#import numpy as np
from conllu import conllu_sentences
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('input')
ap.add_argument('sentid', nargs="*")
args = ap.parse_args()


for sent in conllu_sentences(args.input):
    if args.sentid is None or sent.id in args.sentid:
        sent.to_latex()
        print()
