#!/usr/bin/env python
import math
import re
def tokenizeDoc(cur_doc):
    return re.findall('\\w+',cur_doc)

import sys

dictlist = {}
Y = {}
Y_wstar = {}
Y_star = 0

vocab = []
for line in sys.stdin:
    doc = line.split('\t')
    doc_id = doc[0]
    label = doc[1]
    labels = label.split(',')
    for label in labels:
        sys.stdout.write("Y=")
        sys.stdout.write(label)
        sys.stdout.write("\t")
        sys.stdout.write("1")
        sys.stdout.write("\n")

        sys.stdout.write("Y=*")
        sys.stdout.write("\t")
        sys.stdout.write("1")
        sys.stdout.write("\n")

    features = tokenizeDoc(doc[2])
    w_star = len(features)
    for label in labels:
        for feature in features:
            sys.stdout.write("Y=")
            sys.stdout.write(label)
            sys.stdout.write(",W=")
            sys.stdout.write(feature)
            sys.stdout.write("\t")
            sys.stdout.write("1")
            sys.stdout.write("\n")

        sys.stdout.write("Y=")
        sys.stdout.write(label)
        sys.stdout.write(",W=*")
        sys.stdout.write("\t")
        sys.stdout.write(str(w_star))
        sys.stdout.write("\n")

