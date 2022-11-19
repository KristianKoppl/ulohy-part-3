import tkinter
from random import*
canvas = tkinter.Canvas()
canvas.pack()
slova=[]

def daco1():
    slova=entry1.get()
    
    medzera=20
    medzera1= 140
    plusko=50
    for i in range(len(slova)):
        
        
        canvas.create_text(medzera+20,medzera1-plusko,text=slova[i],font='Arial 20',fill='blue')
        medzera+=20
        
        if medzera1 ==140:
            medzera1-=20
        else:
            medzera1+=20
        print(medzera1)

    


entry1 = tkinter.Entry()
entry1.pack()

button1 = tkinter.Button(text='ok', command=daco1)
button1.pack()
