#-*- coding: utf-8 -*-

words = []

with open('PoliMorf-0.6.7.tab', encoding='utf-8') as file:
    for row in file:
        word = row.split()[0]
        words.append(word)


string = "trwatostraszniedługoaledziała"
tokens = []

i = 0
while i < len(string):
    najdlusze = ""
    for j in range(i, len(string)):
        slowo = string[i:j + 1]
        if slowo in words and len(slowo) > len(najdlusze):
            najdlusze = slowo
    i = i + len(najdlusze)
    tokens.append(najdlusze)

print(tokens)