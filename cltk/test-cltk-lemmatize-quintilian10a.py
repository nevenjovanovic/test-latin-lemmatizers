#!/usr/bin/env python
"""
SYNOPSIS

    python test-cltk-lemmatize-quintilian10a.py filename

DESCRIPTION

    Read in a list of unique word forms Latin text (in our case, Quintilian's Book 10 of Inst. from the Latin Library corpus, cleaned up from punctuation marks, remains of HTML codes etc), feed it to the Latin lemmatizer, output resulting list as a JSON array for further inspection and improvement.

EXAMPLES

    python test-cltk-lemmatize-quintilian10.py 'q10.txt'

EXIT STATUS

    TODO: List exit codes

AUTHOR

    Neven Jovanovic <neven.jovanovic@ffzg.hr>

LICENSE

    This script is in the public domain, free from copyrights or restrictions. CC-licensed.

VERSION

    $0.1$
"""

import sys, os, traceback, optparse
import time
import json

from cltk.corpus.utils.importer import CorpusImporter
corpus_importer = CorpusImporter('latin')
corpus_importer.import_corpus('latin_models_cltk')
from cltk.stem.latin.j_v import JVReplacer
j = JVReplacer()
from cltk.stem.lemma import LemmaReplacer
lemmatizer = LemmaReplacer('latin')

# Initialize a list for lemmata:
q_l = []

# lemmatize list of words
def wordlem (i):
    for q in tqdm(i):
        lemma = lemmatizer.lemmatize(j.replace(q), return_raw=True)
        q_l.append(lemma)

def main ():

    global options, args

    # Read in file, paragraph by paragraph
    # Inside it are words, each in a new line.
    i = sys.argv[1]
    with open(i) as f:
        content = f.read()
        lines = content.splitlines()
        wordlem(lines)
    with open('q10lemmata.json', 'w') as f: 
        f.write(json.dumps(q_l))
if __name__ == "__main__":
    main()
