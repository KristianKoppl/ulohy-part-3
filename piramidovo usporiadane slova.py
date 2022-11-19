import tkinter
from random import*
canvas = tkinter.Canvas()
canvas.pack()
slova=[]

def daco():
    slova=entry1.get()
    
    medzera=50
    for i in range(len(slova)):
        
        
        canvas.create_text(medzera+20,medzera + 50,text=slova[i],font='Arial 20',fill='black')
        medzera+=20
        print(slova[0])

    


entry1 = tkinter.Entry()
entry1.pack()

button1 = tkinter.Button(text='ok', command=daco)
button1.pack()
