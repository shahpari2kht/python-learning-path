def count_divisors(n):
    """Returns the number of divisors of n."""
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

max_num = 0
max_divisors = 0

for _ in range(20):
    num = int(input())
    divisors = count_divisors(num)
    if divisors > max_divisors or (divisors == max_divisors and num > max_num):
        max_num = num
        max_divisors = divisors

print(f"{max_num} {max_divisors}")
