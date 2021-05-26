import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from data import make_corpus as tp

corpus = tp.load_corpus('/Users/logno/Documents/GitHub/conspiracy_generation/data/processed/seqs.txt')
