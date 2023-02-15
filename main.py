import random
correct = 0
incorrect = 0

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


def random_function():
    if level == 1:
        a, b = random.sample(range(0, 9), 2)
    elif level == 2:
        a, b = random.sample(range(10, 99), 2)
    elif level == 3:
        a, b = random.sample(range(100, 999), 2)
    sum1 = a + b
    return a, b, sum1


def user_input():
    user_sum = int(input(f'What is {a} + {b}?:'))
    return user_sum


for i in range(1, 11):
    a, b, sum1 = random_function()
    print('Round', i)
    x = 3
    user_sum = user_input()
    if x > 1:
        while user_sum != sum1 and x > 1:
            x = x - 1
            print(f'Incorrect - you have {x} attempts remaining\n')
            a, b, sum1 = random_function()
            user_sum = user_input()

        if user_sum == sum1:
            print('Correct! Next round.\n')
            correct = correct + 1
        else:
            print('Incorrect - you have failed this round')
            print('Next round.\n')
            incorrect = incorrect + 1

print('You have completed all 10 rounds.')
print(f'You got {correct} rounds correct.')
print(f'You got {incorrect} rounds correct.')
