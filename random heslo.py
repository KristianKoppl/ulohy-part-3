from random import * 

def heslo ():
    a=[]
    for i in range(0,9):
        s=randrange(97,123)
        a.append(chr(s))
    print(a)
heslo()
