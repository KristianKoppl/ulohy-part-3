from random import * 

def heslo ():
    a=[]
    h=[]
    g=[]
    for i in range(0,3):
        c=randrange(65,91)
        a.append(chr(c))

    for i in range(0,2):
        b=randrange(48,58)
        a.append(chr(b))
        
    for i in range(0,3):
        s=randrange(97,123)
        a.append(chr(s))
    
    
        
        
    print(a)
heslo()
