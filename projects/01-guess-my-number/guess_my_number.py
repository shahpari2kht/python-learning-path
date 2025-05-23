import random
numbers = list(range(1, 99))
while True:
    guess = random.choice(numbers)
    print(guess)
    inp = input('Enter k or b or d: ')
    if inp == 'k':
        del numbers[numbers.index(guess):]
    elif inp == 'b':
        del numbers[:numbers.index(guess) + 1]
    elif inp == 'd':
        print('hooooo!! my guess is True!')
        break
