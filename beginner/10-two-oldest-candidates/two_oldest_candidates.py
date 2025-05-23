# دریافت سن کاندیداها و پیدا کردن بیشترین و دومین بیشترین سن

first = 0
second = 0

while True:
    age = int(input())
    if age == -1:
        break
    if 10 <= age <= 90:
        if age > first:
            second = first
            first = age
        elif age > second:
            second = age

print(f"{first} {second}")
