import tkinter
from random import*
canvas = tkinter.Canvas()
canvas.pack()
slova=[]

def daco2():
    slova=entry1.get()
    
    
   
    for i in range(0,len(slova),1):
        
        
        
        
    
        print(i) 
        canvas.update()
        
        
    canvas.after(1,daco2)
    


entry1 = tkinter.Entry()
entry1.pack()

daco2()
