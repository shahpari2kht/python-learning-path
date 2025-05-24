n = int(input())
females = []
males = []

for _ in range(n):
    entry = input().strip().split('.')
    if len(entry) < 3:
        continue
    gender, name, language = entry[0], entry[1], entry[2]
    name_std = name.capitalize()
    language_std = language  # just in case, you can use .lower() if needed
    record = (name_std, language_std)
    if gender.lower() == 'f':
        females.append(record)
    elif gender.lower() == 'm':
        males.append(record)

females.sort()
males.sort()

for name, lang in females:
    print(f"f {name} {lang}")
for name, lang in males:
    print(f"m {name} {lang}")
