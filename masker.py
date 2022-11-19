import random
from os import path

def readFile(filename):
    """
    Reads a text file and returns its text content
    """
    with open(path.join('data', filename), 'r') as file:
        text_content = file.read()
    return text_content


def maskText(text, mask_ratio):
    """
    Masks given text content according to the mask ratio given
    """
    N           =   len(text)
    charlocs    =   [i for i, letter in enumerate(text) if letter != ' ']
    Nmask       =   int(mask_ratio*len(charlocs))
    picked      =   random.sample(charlocs, Nmask)
    for pick in picked:
        text    =   text[:pick] +' '+ text[pick+1:]
    return text


def displayText(text,title):
    print(('*'*25+'{}'+'*'*25).format(title))
    print(text)
    print('*'*60)


if __name__ == "__main__":
    mask_ratio      =   0.15  
    text_content    =  readFile('algorithm_wikipedia.txt')
    text_masked     =   maskText(text_content,mask_ratio)
    print('\n\n')
    displayText(text_content, 'Original Text')
    print('\n\n')
    displayText(text_masked, 'Masked Text')
