# Generate a random number
#loop
    # Ask the user to make a guess
    # If not a valid number, print error
    # If number < guess, print too low
    #If number > guess, print too high
    # else, print well done


import random

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input('Guess the number between 1 and 100:'))
        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too high!')
        else:
            print('you guessed the number')
            break
    except ValueError:
        print('Please enter a valid number')




