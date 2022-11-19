import tkinter
from random import*
canvas = tkinter.Canvas()
canvas.pack()
slova=[]

def daco2():
    slova=entry1.get()
    
    medzera=20
   
    for i in range(len(slova)):
        
        
        canvas.create_text(medzera+20,120,text=slova[i],font='Arial 20',fill='blue',angle=i*(-40))
        medzera+=20
        
        
        print(medzera)

    


entry1 = tkinter.Entry()
entry1.pack()

button1 = tkinter.Button(text='ok', command=daco2)
button1.pack()
