word = input().strip()

lower = sum(1 for ch in word if ch.islower())
upper = sum(1 for ch in word if ch.isupper())

if upper > lower:
    print(word.upper())
else:
    print(word.lower())
