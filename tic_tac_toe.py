from tkinter import *
from tkinter import messagebox
import tkinter
######################################################################
gamewindow = Tk()
gamewindow.title('tic tac toe')
gamewindow.geometry('700x700+400+400') 
gamewindow.configure(background='light blue')

topframe=Frame(gamewindow,width=790,height=390,bd=10,bg='pink',relief=RIDGE,padx=2,pady=4)
topframe.grid(row=0,column=0)

downframe=Frame(gamewindow,width=790,height=200,bd=10,bg='silver',relief=RIDGE ,padx=2,pady=4)
downframe.grid(row=1,column=0)

bottomframe=Frame(gamewindow,width=790,height=200,bd=10,bg='silver',relief=RIDGE,padx=2,pady=4)
bottomframe.grid(row=2,column=0)

playerx=IntVar()
playero=IntVar() 

buttons =StringVar()
click=True
########################################################################
def cheker(buttons):
    global click
    if buttons['text']==' 'and click==True :
        buttons['text']="X"
        click=False
        scorekeeper()
    elif buttons['text']==' 'and click==False :
        buttons['text']="O"
        click=True
        scorekeeper()
########################################################################
def colorreturn():
    button1.configure(fg='black')
    button2.configure(fg='black')
    button3.configure(fg='black')
    button4.configure(fg='black')
    button5.configure(fg='black')
    button6.configure(fg='black')
    button7.configure(fg='black')
    button8.configure(fg='black')
    button9.configure(fg='black')
###########################################################################
def scorekeeper():
    if button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X" :
        button1.configure(background="red",fg="green")
        button2.configure(background="red",fg="green")
        button3.configure(background="red",fg="green")
        s=float(playerx.get())
        score =s+1
        playerx.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ X IS WINNER")
        colorreturn()

    if button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" :
        button4.configure(background="red",fg="green")
        button5.configure(background="red",fg="green")
        button6.configure(background="red",fg="green")
        s=float(playerx.get())
        score =s+1
        playerx.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ X IS WINNER")
        colorreturn()

    if button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X" :
        button7.configure(background="red",fg="green")
        button8.configure(background="red",fg="green")
        button9.configure(background="red",fg="green")
        s=float(playerx.get())
        score =s+1
        playerx.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ X IS WINNER")
        colorreturn()

    if button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X" :
        button1.configure(background="red",fg="green")
        button4.configure(background="red",fg="green")
        button7.configure(background="red",fg="green")
        s=float(playerx.get())
        score =s+1
        playerx.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ X IS WINNER")
        colorreturn()

    if button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X" :
        button2.configure(background="red",fg="green")
        button5.configure(background="red",fg="green")
        button8.configure(background="red",fg="green")
        s=float(playerx.get())
        score =s+1
        playerx.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ X IS WINNER")
        colorreturn()
    
    if button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X" :
        button3.configure(background="red",fg="green")
        button6.configure(background="red",fg="green")
        button9.configure(background="red",fg="green")
        s=float(playerx.get())
        score =s+1
        playerx.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ X IS WINNER")
        colorreturn()

    if button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X" :
        button1.configure(background="red",fg="green")
        button5.configure(background="red",fg="green")
        button9.configure(background="red",fg="green")
        s=float(playerx.get())
        score =s+1
        playerx.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ X IS WINNER")
        colorreturn()

    if button3["text"]=="X" and button5["text"]=="X" and button6["text"]=="X" :
        button3.configure(background="red",fg="green")
        button5.configure(background="red",fg="green")
        button6.configure(background="red",fg="green")
        s=float(playerx.get())
        score =s+1
        playerx.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ X IS WINNER")
        colorreturn()

        #دور  أووو 
    
    if button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O" :
        button1.configure(background="red",fg="green")
        button2.configure(background="red",fg="green")
        button3.configure(background="red",fg="green")
        s=float(playero.get())
        score =s+1
        playero.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ O IS WINNER")
        colorreturn()
    
    if button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" :
        button4.configure(background="red",fg="green")
        button5.configure(background="red",fg="green")
        button6.configure(background="red",fg="green")
        s=float(playero.get())
        score =s+1
        playero.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ O IS WINNER")
        colorreturn()
    
    if button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O" :
        button7.configure(background="red",fg="green")
        button8.configure(background="red",fg="green")
        button9.configure(background="red",fg="green")
        s=float(playero.get())
        score =s+1
        playero.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ O IS WINNER")
        colorreturn()

    if button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O" :
        button1.configure(background="red",fg="green")
        button4.configure(background="red",fg="green")
        button7.configure(background="red",fg="green")
        s=float(playero.get())
        score =s+1
        playero.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ O IS WINNER")
        colorreturn()

    if button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O" :
        button2.configure(background="red",fg="green")
        button5.configure(background="red",fg="green")
        button8.configure(background="red",fg="green")
        s=float(playero.get())
        score =s+1
        playero.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ O IS WINNER")
        colorreturn()
    
    if button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O" :
        button3.configure(background="red",fg="green")
        button6.configure(background="red",fg="green")
        button9.configure(background="red",fg="green")
        s=float(playero.get())
        score =s+1
        playero.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ O IS WINNER")
        colorreturn()

    if button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O" :
        button1.configure(background="red",fg="green")
        button5.configure(background="red",fg="green")
        button9.configure(background="red",fg="green")
        s=float(playero.get())
        score =s+1
        playero.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ O IS WINNER")
        colorreturn()

    if button3["text"]=="O" and button5["text"]=="O" and button6["text"]=="O" :
        button3.configure(background="red",fg="green")
        button5.configure(background="red",fg="green")
        button6.configure(background="red",fg="green")
        s=float(playero.get())
        score =s+1
        playero.set(score)
        tkinter.messagebox.showinfo("COGRATULATIONS,^_^ O IS WINNER")
        colorreturn()
##########################################################################
def restart():
    button1["text"]=" "
    button2["text"]=" "
    button3["text"]=" "
    button4["text"]=" "
    button5["text"]=" "
    button6["text"]=" "
    button7["text"]=" "
    button8["text"]=" "
    button9["text"]=" "
    button1.configure(background='silver')
    button2.configure(background='silver')
    button3.configure(background='silver')
    button4.configure(background='silver')
    button5.configure(background='silver')
    button6.configure(background='silver')
    button7.configure(background='silver')
    button8.configure(background='silver')
    button9.configure(background='silver')

##########################################################################
def newgame():
    restart()
    playerx.set(0)
    playero.set(0)
   


############################################################################
button1=Button(topframe,text=' ',font=("Times 25 bold"),height=2,width=6,bg="silver",command=lambda:cheker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2=Button(topframe,text=' ',font="Times 25 bold",height=2,width=6,bg="silver",command=lambda:cheker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3=Button(topframe,text=' ',font="Times 25 bold",height=2,width=6,bg="silver",command=lambda:cheker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4=Button(topframe,text=' ',font="Tines 25 bold",height=2,width=6,bg="silver",command=lambda:cheker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5=Button(topframe,text=' ',font="Times 25 bold",height=2,width=6,bg="silver",command=lambda:cheker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6=Button(topframe,text=' ',font="Times 25 bold",height=2,width=6,bg="silver",command=lambda:cheker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7=Button(topframe,text=' ',font="Times 25 bold",height=2,width=6,bg="silver",command=lambda:cheker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8=Button(topframe,text=' ',font="Times 25 bold",height=2,width=6,bg="silver",command=lambda:cheker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9=Button(topframe,text=' ',font="Times 25 bold",height=2,width=6,bg="silver",command=lambda:cheker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)

#----------------------------------------------------------------------------------------------

labelplayerx=Label(downframe,font=("Papyrus",18,"bold"),text="Player X's result ",padx=2,pady=2,bg="pink")
labelplayerx.grid(row=0,column=0)

labelplayero=Label(downframe,font=("Papyrus",18,"bold"),text="Player O's result ",padx=2,pady=2,bg="pink")
labelplayero.grid(row=1,column=0)

resultx = Entry(downframe ,font=("Papyrus",20,"bold"),bd=2,fg="black",textvariable=playerx)
resultx.grid(row=0,column=1)


resulto = Entry(downframe ,font=("Papyrus",20,"bold"),bd=2,fg="black",textvariable=playero)
resulto.grid(row=1,column=1)

newgamebutton=Button(bottomframe,text="new game",font="Times 20 bold",width=10,height=2,bd=2,bg="green",fg="black",command=lambda:newgame())###
newgamebutton.grid(row=0,column=1)

restartgamebutton=Button(bottomframe,text="restart the game",font="Times 20 bold",width=14,height=2,bd=2,bg="green",fg="black",command=lambda:restart())
restartgamebutton.grid(row=0,column=2)

exitgamebutton=Button(bottomframe,text="exit",font="Times 20 bold",width=10,height=2,bd=2,bg="green",fg="black", command=lambda:exit(gamewindow))
exitgamebutton.grid(row=0,column=3)

gamewindow.mainloop()
