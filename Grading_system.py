name=input("enter the name of student ")
m1=int(input("enter the first subject marks "))
m2=int(input("enter the second subject marks "))
m3=int(input("enter the marks of third subject "))
m4=int(input("enter the marks of forth subject "))
m5=int(input("enter the marks of fifth subject "))
M=m1+m2+m3+m4+m5
percent=M/5
print("your percentage is:",percent)
if(m1>100 or m2>100 or m3>100 or m4>100 or m5>100 or m1<0 or m2<0 or m3<0 or m4<0 or m5<0):
    print("enter the wrong marks criteria")
elif(percent==100):
    print("grade==O")
elif(percent>=90):
    print("grade==A+")
elif(percent>=80):
    print("grade==B+")
elif(percent>=70):
    print("grade==B")
elif(percent>=60):
    print("grade==C")
elif(percent>=50):
    print("grade==D")
else:
    print("the student is fail")
