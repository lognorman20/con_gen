import re
import string
### Functions in this file ###
# 1. load_corpus
# 2. parse_and_clean
# 2. load_full_text
# 3. get_vocab
# 4. get_tensor_dataset

# Load raw corpus
def load_corpus(filename):
    file = open(filename, 'r') # open the file as read only
    text = file.read() # read all text
    file.close() # close the file
    return text

# Parse & Clean Function Testing
# Parse & Clean Function Testing
def parse_and_clean(input):
    with open('../data/processed/corpus.txt', 'w') as fout:
        text = load_corpus(input)
        text = re.sub(r'http\S+', '', text) # removes hyperlinks
        text = text.replace('_', "") # removes underscores
        text = text.replace('  (', "") # removes empty parentheses
        text = text.replace('* ', "") # removes * characters
        text = text.replace('"', "") # removes * characters

        fout.write(text)
        return text

def get_tokens(input):
    text = parse_and_clean(input) # read & clean data
    
    tokens = text.split() # create tokens
    table = str.maketrans('', '', string.punctuation)
    tokens = [w.translate(table) for w in tokens]
    tokens = [word for word in tokens if word.isalpha()] # remove remaining tokens that are not alphabetic
    tokens = [word.lower() for word in tokens] # make lower case

    return tokens