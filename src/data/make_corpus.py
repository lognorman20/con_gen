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
    # open the file as read only
    file = open(filename, 'r')
    # read all text
    text = file.read()
    # close the file
    file.close()
    return text

# Parse & Clean Function Testing
def parse_and_clean(input):
    with open('../data/processed/corpus.txt', 'w') as fout:
        text = load_corpus(input)
        text = re.sub(r'http\S+', '', text) # removes hyperlinks
        text = text.replace('_', "") # removes underscores
        text = text.replace('  (', "") # removes empty parentheses
        text = text.replace('* ', "") # removes empty parentheses

        fout.write(text)

        tokens = text.split() # create tokens
        table = str.maketrans('', '', string.punctuation)
        tokens = [w.translate(table) for w in tokens]
        tokens = [word for word in tokens if word.isalpha()] # remove remaining tokens that are not alphabetic
        tokens = [word.lower() for word in tokens] # make lower case

        return tokens