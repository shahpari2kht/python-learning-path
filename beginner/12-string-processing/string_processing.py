text = input()

vowels = set("aeiouAEIOU")
result = ''

for ch in text:
    if ch not in vowels:
        result += '.' + ch.lower()

print(result)
