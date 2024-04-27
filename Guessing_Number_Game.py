import random as M

m1=int(input("enter the number "))
m2=M.randrange(1,m1)
m3=int(input("enter the number "))
while(True):
    if(m3==0):
        print("game over,player quite the game.")
        break
    elif(m3==m2):
        print("congratulation you are right. the random number was:",m2)
        break
    elif(m3<m2):
        y=int(input("you are near to correct it play some more time"))
    elif(m3>m2):
        y=int(input("your guessing is around to corect.please play more time"))
    else:
        y=int(input("try again"))
        
