n = int(input())
trans_dict = dict()

for _ in range(n):
    entry = input().strip().split()
    if len(entry) == 4:
        main, en, fr, de = entry
        # همه ترجمه‌ها به کلمه اصلی نگاشت داده می‌شوند
        trans_dict[en] = main
        trans_dict[fr] = main
        trans_dict[de] = main

sentence = input().strip().split()
result = []

for word in sentence:
    # بدون توجه به وجود یا عدم وجود در دیکشنری ترجمه می‌کند
    result.append(trans_dict.get(word, word))

print(' '.join(result))
