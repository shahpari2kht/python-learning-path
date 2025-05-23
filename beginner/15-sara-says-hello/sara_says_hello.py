word = input().strip()
target = 'hello'
j = 0

for ch in word:
    if ch == target[j]:
        j += 1
        if j == len(target):
            break

if j == len(target):
    print('YES')
else:
    print('NO')
