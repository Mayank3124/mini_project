m1=int(input("enter the starting point "))
m2=int(input("enter the end point "))
m3=int(input("enter the updation "))

c=input("enter your choice as 'F' for forward printing or 'R' for reverse printing:")
c2=input("enter the choice as 'r' for row printing or 'c' for column printing:")

if c=="F":
    if c2=="r":
        for i in range(m1,m2,m3):
            print(i,end=',')
    elif c2=="c":
        for i in range(m1,m2,m3):
            print(i)
    else:
        print("second choice is not correct. enter the valid choice.")
elif c=="R":
    if c2=="r":
        for i in range(m2,m1,-m3):
            print(i,end=',')
    elif c2=="c":
        for i in range(m2,m1,-m3):
            print(i)
    else:
        print("second choice is not correct. enter a valid choice")
else:
    print("your both choices are wrong")
