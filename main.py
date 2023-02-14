import random

while True:
    try:
        level = int(input("Choose a level between 1 and 3:"))
    except ValueError:
        print("Incorrect input - try again")
        continue
    if 0 >= level:
        print("Incorrect input - try again")
        continue
    elif level >= 4:
        print("Incorrect input - try again")
        continue
    else:
        break

if 1 <= level <= 3:
    print('You have chosen level', level)
else:
    pass
if level == 1:
    a, b = random.sample(range(0, 9), 2)
elif level == 2:
    a, b = random.sample(range(10, 99), 2)
elif level == 3:
    a, b = random.sample(range(100, 999), 2)

sum1 = a + b

for i in range(1, 11):
    print('Round', i)
    x = 3
    user_sum = int(input(f'What is {a} + {b}?:'))
    if sum1 == user_sum:
        print('Correct! Next round.')
    elif sum1 != user_sum:
        x = x - 1
        print(f'Incorrect - you have {x} attempts remaining.')


