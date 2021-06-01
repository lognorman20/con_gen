import string
# 3. get_tokens - retrieves tokens from cleaned corpus
# 4. organize_seqs - organize tokens into sequences
# 5. save_doc - save tokens to file, one dialog per line

corpus = '/Users/logno/Documents/GitHub/conspiracy_generation/data/interim/corpus.txt'

def get_tokens(filename):
    '''
    This function tokenizes each word in the cleaned corpus.
    '''
    with open(filename, 'r') as fin:
        text = fin.read()
        tokens = text.split() # create tokens
        table = str.maketrans('', '', string.punctuation)
        tokens = [w.translate(table) for w in tokens]
        tokens = [word for word in tokens if word.isalpha()] # remove remaining tokens that are not alphabetic
        tokens = [word.lower() for word in tokens] # make lower case

    return tokens

def organize_seqs(filename):
    '''
    This function organizes the long list of tokens into sequences of 50 input words and 1 output word.
    The model will use the 50 input words to predict the one output word after this function creates a new
    corpus. This function iterates over the list of tokens from token 51 onwards and taking the prior 50 tokens
    as a sequence, then repeats this process to the end of the list of tokens.
    '''
    tokens = get_tokens(filename)
    length = 50 + 1
    sequences = list()
    for i in range(length, len(tokens)):
        # select sequence of tokens
        seq = tokens[i-length:i]
        # convert into a line
        line = ' '.join(seq)
        # store
        sequences.append(line)
    print('Total Sequences: %d' % len(sequences))
    
    return sequences

def save_doc(filename):
    '''
    This function organizes the sequences into a line by line format and writes each sequence to a new file
    in '../data/processed/seqs.txt' to be passed into the model. Each line is shifted along one word, with a 
    new word at the end to be predicted, creating an overlap between the sequences.

    This function is the culminating function of the above functions. To clean raw data, simply run this function
    on the raw data.
    '''
    lines = organize_seqs(filename)
    data = '\n'.join(lines)
    file = open('/Users/logno/Documents/GitHub/conspiracy_generation/data/processed/seqs.txt', 'w')
    file.write(data)
    file.close()

save_doc(corpus)