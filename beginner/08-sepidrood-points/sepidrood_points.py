sum1 = 0
win_counter = 0

for i in range(30):
    vorudi = int(input())
    sum1 += vorudi
    if vorudi == 3:
        win_counter += 1
    elif vorudi != 0 and vorudi != 1 and vorudi != 3:
        print("error")

print(sum1, " ", win_counter)
