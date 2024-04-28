import math
def sum():
    x=int(input("enter value of x: "))
    y=int(input("enter value of y: "))
    sum =x+y
    return sum
def sub():
    x=int(input("enter value of x: "))
    y=int(input("enter value of y: "))
    sub =x-y
    return sub
def mul():
    x=int(input("enter value of x: "))
    y=int(input("enter value of y: "))
    mul =x*y
    return mul
def div():
    x=int(input("enter value of x: "))
    y=int(input("enter value of y: "))
    div =x/y
    return div
def sqrt():
    x=int(input("enter value of x: "))
    sqrt =math.sqrt(x)
    return sqrt
def pow():
    x=int(input("enter value of x: "))
    y=int(input("enter value of y: "))
    pow =x**y
    return pow
def log():
    x=int(input("enter value of x: "))
    log =math.log(x)
    return log
def sin():
    x=int(input("enter the value of x: "))
    sin =math.sin(x)
    return sin
def cos():
    x=int(input("enter the value x: "))
    cos =math.cos(x)
    return cos
def tan():
    x=int(input("enter the value x: "))
    tan =math.tan(x)
    return tan
def exp():
    x=int(input("enter the value x: "))
    
    exp =math.exp(x)
    return exp
def fact():
    x=int(input("enter the value x: "))
    
    fact =math.factorial(x)
    return fact
def mod():
    x=int(input("enter the value x: "))
    y=int(input("enter the value y: "))
    mod =x%y
    return mod
def sqr():
    x=int(input("enter the value x: "))
    sqr =x**2
    return sqr
def cube():
    x=int(input("enter the value x: "))
    cube =x**3
    return cube
while True:
    choice=int(input("enter your choice\n 1->sum\n 2->sub\n 3->div\n 4->mul\n 5->sqrt\n 6->pow\n 7->log\n 8->sin\n 9->cos\n 10->tan\n 11->exp\n 12->fact\n 13->mod\n 14->sqr\n 15->cube\n 16->exit\n:"))
    if choice==1:
       print(sum())
    elif choice==2:
       print(sub())
    elif choice==3:
        print(div())
    elif choice==4:
        print(mul())
    elif choice==5:
        print(sqrt())
    elif choice==6:
        print(pow())
    elif choice==7:
        print(log())
    elif choice==8:
        print(sin())
    elif choice==9:
        print(cos())
    elif choice==10:
        print(tan())
    elif choice==11:
        print(exp())
    elif choice==12:
        print(fact())
    elif choice==13:
        print(mod())
    elif choice==14:
        print(sqr())
    elif choice==15:
        print(cube())
    elif choice==16:
        break
    else:
        print("Invalid choice")
