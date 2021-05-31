import re
import string

### Functions in this file ###
# 1. load_corpus - reads in raw data
# 2. parse_and_clean - cleans raw corpus for tokenization

# Cleaning tasks:
#     -> Remove short comments (less than 170 characters)
#     -> Remove image links (, .jpg, .png)
#     -> Remove comments that are just a link
#     -> Remove comments with more than three links
#     -> Remove comments using quote notation (">" or ">>" markdown symbols)
#     -> Remove trailing, starting, and double white space from each comment
#     -> Remove non-ASCII characters

# Load raw corpus
def load_corpus(filename):
    '''
    This functions reads in the raw data file to be processed.
    '''
    file = open(filename, 'r') # open the file as read only
    text = file.read() # read all text
    file.close() # close the file
    return text

def remove_shorties(filename):
    '''
    Removes short comments (less than 170 characters)
    '''
    with open(filename, 'r') as fin, open('../data/interim/corpus.txt', 'w') as fout:
        for line in fin:
            if len(line) > 170:
                fout.write(line)

