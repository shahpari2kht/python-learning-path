# تعداد لپ تاپ ها
n = int(input())
laptops = []

for _ in range(n):
    price, quality = map(int, input().split())
    laptops.append((price, quality))

# مرتب‌سازی بر اساس قیمت (صعودی)
laptops.sort()

# اگر کیفیت لپ تاپ با قیمت کمتر بیشتر از لپ تاپ با قیمت بیشتر باشد، happy irsa
for i in range(n - 1):
    if laptops[i][1] > laptops[i + 1][1]:
        print("happy irsa")
        break
else:
    print("poor irsa")
