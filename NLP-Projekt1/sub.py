import re

with open('resources/dict.tsv', 'r') as f:
    programs_names = [r.split() for r in f]

subDict = { re.sub('\|', ' ',k[0]): k[1] for k in programs_names }

def subs(string):
    if string in subDict:
        string = subDict[string]
    return string

dict = {
    'ą' : 'a',
    'ę' : 'e',
    'ć' : 'c',
    'ł' : 'l',
    'ń' : 'n',
    'ó' : 'o',
    'ś' : 's',
    'ź' : 'z',
    'ż' : 'z'
}

def polishDel(sentence):
    output = ''
    for words in sentence:
        for char in words:
            if char in dict:
                char = dict[char]
            output = output + char
    return output