from random import * 

def heslo ():
    j=randrange(0,9)
    h=randrange(0,9)
    a=[]
   
    g=[]
    
        
    for i in range(0,8):
        s=randrange(97,123)
        a.append(chr(s))


    for i in range(0,1):
        c=randrange(65,91)
    a[j]=chr(c)
    
    
    
        
        
    print(a)
heslo()
