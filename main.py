import random
while True:
    correct_rounds = 0
    incorrect_rounds = 0

    # Prompt user to choose a level
    while True:
        try:
            level = int(input("Choose a level between 1 and 3:"))
        except ValueError:
            print("Invalid input - try again")
            continue
        if 0 >= level:
            print("Invalid input - try again")
            continue
        elif level >= 4:
            print("Invalid input - try again")
            continue
        else:
            break

    print('You have chosen level', level)

    def random_function():                       # Generate two random numbers
        if level == 1:
            a, b = random.sample(range(0, 9), 2)
        elif level == 2:
            a, b = random.sample(range(10, 99), 2)
        elif level == 3:
            a, b = random.sample(range(100, 999), 2)
        sum1 = a + b
        return a, b, sum1


    def user_input():                           # Input validation on user sum
        while True:
            try:
                user_sum = int(input(f'What is {a} + {b}?:'))
            except ValueError:
                print("Invalid input - try again")
            else:
                break

        return user_sum


    for i in range(1, 11):                  # for loop for 10 rounds
        a, b, sum1 = random_function()
        print('Round', i)
        x = 3                               # counter for number of trials
        user_sum = user_input()
        if x > 1:                           # checking user sum
            while user_sum != sum1 and x > 1:
                x = x - 1
                print(f'Incorrect - you have {x} attempts remaining\n')
                a, b, sum1 = random_function()
                user_sum = user_input()

            if user_sum == sum1:                
                print('Correct! Next round.\n')
                correct = correct_rounds + 1
            else:
                print('Incorrect - you have failed this round')
                print('Next round.\n')
                incorrect = incorrect_rounds + 1

    print(f'You have completed all 10 rounds.\n\
    You got {correct_rounds} rounds correct.\n\
    You got {incorrect_rounds} rounds correct.\n')

    print('Lets play again.\n')
    continue
