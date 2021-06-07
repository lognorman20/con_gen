import re
import string

filename = "data/raw/conspiracy_theories.txt"

def parse_clean(filename):
    '''
    Cleaning tasks:
    -> Remove short comments (less than 170 characters)
    -> Remove comments with links
    -> Remove comments with markdown symbols like > and *
    -> Remove double white space from each comment
    -> Remove non-ASCII characters
    '''
    with open(filename, 'r') as fin:
        with open('data/processed/corpus.txt', 'w') as fout:
            for line in fin:
                if len(line) >= 100:
                    line = line.replace('>', '') 
                    line = line.replace('  ', ' ')
                    line = line.replace('[', '') 
                    line = line.replace(']', '')
                    line = re.sub(r'http\S+', '', line)
                    line = line.replace('*', '')
                    encoded_string = line.encode("ascii", "ignore")
                    line = encoded_string.decode()
                    
                    fout.write(line + '<|endoftext|>')
        
    print("The corpus has been created at '/data/processed/corpus.txt'")

parse_clean(filename)
