# ورودی تعداد بازیکنان و تعداد شرکت آنها در مسابقات
n = int(input())
games = list(map(int, input().split()))

# فقط کسانی که حداکثر 2 بار شرکت کرده‌اند
eligible = [g for g in games if g <= 2]

# هر تیم 3 نفره است
max_teams = len(eligible) // 3

print(max_teams)
