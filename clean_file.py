from os import listdir
from os.path import isfile, join

file = 'lyrics.txt'

def remove_brackets(text):
    
    cleaned_text = ''
    in_bracket = False

    for char in text:

        if in_bracket:
            if char == ']':
                in_bracket = False
            
            continue

        if char == '[':
            in_bracket = True
            continue

        if char == '.' or char == ',' or char == '"' or char == '-' or char == '(' or char == ')' or char == '?' or char == '!' or char == '&' or char == ':' or char == ';': 
            continue

        cleaned_text = cleaned_text + char

    return cleaned_text

with open(file, 'r', encoding='Latin-1') as myfile:
    data = myfile.read()

data = '\n'.join([x for x in data.splitlines() if x.strip()])
data = remove_brackets(data)

with open(file, 'w') as myfile:
    myfile.write(data)

print('cleaned ' + file)