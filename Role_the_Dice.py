import random 

i = 1
m1 = m2 = 0

while i < 7:
    s = random.randint(1, 6)
    y = int(input("Enter a number between 1 to 6: "))
    c = input("If you want to quit, type 'quit', otherwise type 'n': ")
    
    m1 += s
    m2 += y
    
    if c == 'quit':
        break
    elif c == 'n':
        print("Computer's score:", s)  # Added this line to display computer's score
        continue
    else:
        print("Wrong choice")
        break
        
print("\n")
print("Your score is:", m2)
print("The computer's score is:", m1)
print("\n")
if m1 > m2:
    print("Computer won with a score of:", m1)
else:
    print("You won with a score of:", m2)
