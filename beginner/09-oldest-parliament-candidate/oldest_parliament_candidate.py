max_age = 0
while True:
    age = int(input())
    if age == -1:
        break
    if age > max_age:
        max_age = age
print(max_age)
