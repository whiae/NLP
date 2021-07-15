import nltk

zdanie = input("Podaj zdanie: ").lower()
tokens = nltk.word_tokenize(zdanie)
print(tokens)
tags = []

with open('PoliMorf-0.6.7.tab', encoding='utf-8') as file:
        for row in file:
            for i in range(len(tokens)):
                if tokens[i] == row.split()[0]:
                   tags.append((tokens[i], row.split()[2]))

print(tags)

for j in range(len(tags)):
    if tokens[0] == tags[j][0] and tags[j][1] == 'impt:sg:sec:perf':
        print('Akcja: ' + tags[j][0] + ', Obiekt: ' + ' '.join(map(str, tokens[1:])))
