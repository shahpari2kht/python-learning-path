from collections import OrderedDict

n = int(input())
dictionary = OrderedDict()

for _ in range(n):
    key, value = input().split()
    dictionary[key] = value

sentence = input().split()
translated = []

for word in sentence:
    if word in dictionary:
        translated.append(dictionary[word])
    else:
        translated.append(word)

print(' '.join(translated))
