from tkinter import *
fen1= Tk()
text = Label( fen1, text= 'bonjour')
text.pack()
musique= StringVar()
bou1= Checkbutton(fen1,text="Musique de fond",variable=musique, onvalue='oui', offvalue='non')
bou1.pack()
if musique.get()=='non':
    but1=Label(fen1, text= 'bonsoir')
    but1.pack()
fen1.mainloop()


    
