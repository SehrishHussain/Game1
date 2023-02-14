Math Game
Testing for program structure, logic flow, basic loops, conditionals, exception handling.

-------------------------------------------------------------------------------------------

Ask the user what level to play the game on, the choices are:

1) Level 1
2) Level 2
3) Level 3

An invalid input choice will retry asking the user for a level again, after reporting that they entered invalid input.


There will be 10 rounds of asking the user the answer to the sum of two numbers.

Each round will generate two random numbers to perform a sum.

If the level chosen was 1, the sums will be single digits such as 5 + 5, and 1 + 9. (Numbers from 1 to 9).
If the level chosen was 2, the sums will be double digits such as 15 + 25, and 10 + 19. (Numbers from 10 to 99).
If the level chosen was 3, the sums will be triple digits such as 525 + 127, and 742 + 124. (Numbers from 100 to 999).

For example, the program will generate a question such as:

What is 5 + 5?

The user will then enter the answer.

If the answer is invalid (they did not enter a positive number), then ask them to re-enter and try again.

If the answer is incorrect, you give the user 2 more tries. If they do not guess the number within 3 valid attempts, record that they failed the round and go to the next round (new sum).

If the answer is correct, you go to the next round recording that they successfully got this round correct.

After 10 rounds, report to the user how many rounds they got right, and how many they failed.

After reporting the game result, the game will restart asking for a level to play.

The game must start in a function named "main", which should be called when running the Python file to begin the game.

Here's the example output:

Choose a level between 1 and 3: A
Invalid input - try again.

Choose a level between 1 and 3: 1
You have chosen level 1.

Round 1
What is 5 + 2?: Red
Invalid input - try again.

What is 5 + 2?: 5
Incorrect - you have 2 attempts remaining.

What is 5 + 2?: 9
Incorrect - you have 1 attempt remaining.

What is 5 + 2?: 7
Correct! Next round.

Round 2
What is 9 + 1?: 10
Correct! Next round.

Round 3:
What is 1 + 2?: 5
Incorrect - you have 2 attempts remaining.

What is 1 + 2?: 6
Incorrect - you have 1 attempt remaining.

What is 5 + 2?: 7
Incorrect - you have failed this round.
Next round.

...
etc.
...
You have now completed all 10 rounds.
You got 7 rounds correct.
You got 3 rounds incorrect.

Lets play again.

Choose a level between 1 and 3:


