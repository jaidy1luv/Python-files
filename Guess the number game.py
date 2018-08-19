from random import randint
userName = input('What is your name?\n')
print('Hello', userName, 'I am thinking of a number between 1 & 100.')

guessTaken = 0

value = randint(1,101)
while guessTaken < 10:
    guess = int(input('Guess the number:'))
    guessTaken = guessTaken + 1
    value = int(value)
    guess = int(guess)

    if value - guess > 10:
        print('You are far')

    if value - guess <= 10:
        print('You are close')

    if value == guess:
        break
if value == guess:
    guessTaken = str(guessTaken)
    print('You got the number after', guessTaken, 'attempts. Cheers!')

if value != guess:
    value = str(value)
    print('oops! You have reached the maximum number of try allowed. The number I was thinking is...', value, 'Better luck next time')
      
