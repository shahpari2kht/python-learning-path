from collections import OrderedDict

n = int(input())
votes = OrderedDict()

for _ in range(n):
    country = input()
    if country in votes:
        votes[country] += 1
    else:
        votes[country] = 1

# مرتب‌سازی اسامی کشورها به ترتیب حروف الفبا
for country in sorted(votes.keys()):
    print(country, votes[country])
