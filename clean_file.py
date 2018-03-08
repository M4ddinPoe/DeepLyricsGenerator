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

def remove_long_lines(text):
    
    cleaned_text = ''
    lines = text.splitlines(keepends=True)

    for line in lines:
        if len(line) < 70:
            cleaned_text = cleaned_text + line

    return cleaned_text

with open(file, 'r', encoding='Latin-1') as myfile:
    data = myfile.read()

data = '\n'.join([x for x in data.splitlines() if x.strip()])
data = remove_long_lines(data)
data = remove_brackets(data)

with open(file, 'w') as myfile:
    myfile.write(data)

print('cleaned ' + file)