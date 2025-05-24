import sys

text = input()  # اگر چند خطه بخواهی sys.stdin بخوای راحت تغییر میدم
words = []
for sentence in text.split('.'):
    # هر جمله را پردازش کن
    sentence = sentence.strip()
    if not sentence:
        continue
    tokens = [w.rstrip('.,') for w in sentence.split()]
    if len(tokens) == 0:
        continue
    # کلمات جمله را اضافه کن (به جز اولین کلمه هر جمله)
    words.extend([(token, i+1) for i, token in enumerate(tokens)])

result = []
for idx, (word, position) in enumerate(words):
    # اولین کلمه جمله نباید باشد
    # بررسی بزرگ بودن اولین حرف و عدد نبودن
    if idx == 0 or words[idx-1][0][-1] == '.':
        continue
    if word and word[0].isupper() and not word.isdigit():
        result.append(f"{position}:{word}")

if result:
    for line in result:
        print(line)
else:
    print("None")
