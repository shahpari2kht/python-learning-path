# Read and standardize 10 names

names = [input().strip() for _ in range(10)]

for name in names:
    print(name.capitalize())
