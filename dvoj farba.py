import tkinter
from random import*
canvas = tkinter.Canvas()
canvas.pack()
slova=[]

def daco():
    slova=entry1.get()
    
    medzera=100
    for i in range(len(slova)):
        
        farba=choice(('red','blue'))
        canvas.create_text(medzera+20,150,text=slova[i],font='Arial 20',fill=farba)
        medzera+=20
        print(slova[0])

    


entry1 = tkinter.Entry()
entry1.pack()

button1 = tkinter.Button(text='ok', command=daco)
button1.pack()
