#!/usr/bin/env python

import sys, re

def resolve_refs(doc):
    labels = {}
    regex = r'\\label\{(((\w+):)?([^}]+))\}'
    for m in re.finditer(regex, doc):
        group = m.group(3) if len(m.group(2)) else '_'
        if not labels.get(group): labels[group] = []
        labels[group].append(m.group(1))
    
    for group in labels:
        for i, label in enumerate(labels[group]):
            doc = doc.replace('\\ref{%s}' % label, str(i + 1))
            
    return doc

if __name__=='__main__':
    if len(sys.argv) > 1:
        doc = open(sys.argv[1]).read()
    else:
        doc = sys.stdin.read()
    
    sys.stdout.write(resolve_refs(doc))