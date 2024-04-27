import random as M
r=M.choice(['rock','scissor','paper'])
m=input("choice only one 'rock,papr,scissor':")
if(m=='rock'):
    if(r=='rock'):
        print("match draw")
    elif(r=='paper'):
        print("computer wins")
    elif(r=='scisor'):
        print("you win")
if(m=='scissor'):
    if(r=='scisor'):
        print("match draw")
    elif(r=='rock'):
        print("computer wins")
    elif(r=='paper'):
        print("you wins")
if(m=='paper'):
    if(r=='paper'):
        print("match draw")
    elif(r=='rock'):
        print("we loose")
    elif(r=='scissor'):
        print("we win")
    else:
        print("nobody wins")
    
