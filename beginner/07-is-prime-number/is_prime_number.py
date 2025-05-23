num=int(input())
n=0
for i in range(1,num):
    if (num % i == 0):
        n += 1
if (n == 1):
    print("prime")
else:
    print("not prime")
