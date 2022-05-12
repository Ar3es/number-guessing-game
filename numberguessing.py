name = input("What is your name? ")
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        print("Please type a number greater than 0")
        quit()
else:
    print("Type a number next time")
    quit()

from platform import java_ver
import random
number = random.randint(0 , top_of_range)
number_guesses  = 0

print("okay", name , "I am guessing a number between 0 and", top_of_range)

while True:
    number_guesses +=1
    guess = input()
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number next time")
        continue

    if guess == number:
        break
    elif guess > number:
        print("your guess is too high")
    else:
        print("your guess is too low")

if guess == number:
    print("You guessed the number in", str(number_guesses), "guesses")