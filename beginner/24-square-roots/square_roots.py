from math import sqrt

n = int(input())
for _ in range(n):
    num = float(input())
    root = sqrt(num)
    # بدون گرد کردن، دقیقا ۴ رقم اعشار:
    print("{:.4f}".format(root))
