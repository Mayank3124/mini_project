import random 
i=1
m1=m2=0
while(i<7):
    s=random.randint(1,6)
    y=int(input("enter the number between 1to 6: "))
    c=input("if you quite type'quite' otherwise type 'n' : ")
    m1+=s
    m2+=y
    if(c=='quite'):
        break
    elif(c=='no'):
        continue
    else:
        print("wrong choice")
        break
        
print("\n")
print("your score is:",m2)
print("the computer score is:",m1)
print("\n")
if(m1>m2):
    print("computer won with score of:",m1)
else:
    print("you won with the score of:",m2)
