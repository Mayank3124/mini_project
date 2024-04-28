import random as M

r = M.choice(['rock', 'scissor', 'paper'])
m = input("Choose only one 'rock, paper, scissor': ")

if m == 'rock':
    if r == 'rock':
        print("Match draw")
    elif r == 'paper':
        print("Computer wins")
    elif r == 'scissor':
        print("You win")

elif m == 'scissor':
    if r == 'scissor':
        print("Match draw")
    elif r == 'rock':
        print("Computer wins")
    elif r == 'paper':
        print("You win")

elif m == 'paper':
    if r == 'paper':
        print("Match draw")
    elif r == 'rock':
        print("We lose")
    elif r == 'scissor':
        print("We win")
