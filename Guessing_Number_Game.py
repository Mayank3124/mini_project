import random as r

max_range = int(input("Enter the maximum range for the random number: "))
random_num = r.randrange(1, max_range)
guess_num = int(input("Enter your guess: "))

while True:
    if guess_num == 0:
        print("Game over. You quit the game.")
        break
    elif guess_num == random_num:
        print("Congratulations! You guessed the correct number. The random number was:", random_num)
        break
    elif guess_num < random_num:
        guess_num = int(input("You are close, try a higher number: "))
    elif guess_num > random_num:
        guess_num = int(input("Your guess is high, try a lower number: "))
    else:
        guess_num = int(input("Invalid input, please try again: "))
