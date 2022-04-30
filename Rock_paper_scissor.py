from tkinter import *
import tkinter
from  PIL import Image,ImageTk
#Main window
window=tkinter.Tk()
window.title("Rock paper scissors game")
window.configure(background="#363945")

#Picture
rock_image=ImageTk.PhotoImage(Image.open("rock.jpg"))
rock_comp_image=ImageTk.PhotoImage(Image.open("rock-comp.jpg"))
paper_image=ImageTk.PhotoImage(Image.open("paper.jpg"))
paper_comp_image=ImageTk.PhotoImage(Image.open("paper-comp.jpg"))
scissor_image=ImageTk.PhotoImage(Image.open("scissor.jpg"))
scissor_comp_image=ImageTk.PhotoImage(Image.open("scissor-comp.jpg"))
#insert
comp_label=Label(window,image=scissor_comp_image,bg="orange")
comp_label.grid(row=2,column=0)
user_label=Label(window,image=scissor_image,bg="Black")
user_label.grid(row=2,column=20)
#Score
Playerscore=Label(window,text=0,font=100,bg="#9b59b6",fg="white")
computerscore=Label(window,text=0,font=100,bg="#9b59b6",fg="white")
computerscore.grid(row=1,column=1)
Playerscore.grid(row=1,column=6)


#indicators
user_indicator=Label(window,font=50,text="USER",bg="#363945",fg="White").grid(row=0,column=10)
comp_indicator=Label(window,font=50,text="COMPUTER",bg="#363945",fg="White").grid(row=0,column=2)

#Messages
msg=Label(window,font=50,bg="#363945",fg="White")
msg.grid(row=3,column=2)
#Button
rock=Button(window,width=20,height=2,text="ROCK",bg="#9B2335",fg="White",font=10,command=lambda:updatechoices("rock")).grid(row=5,column=2)
paper=Button(window,width=20,height=2,text="PAPER",bg="#9B2335",fg="White",font=10,command=lambda:updatechoices("paper")).grid(row=5,column=3)
scissor=Button(window,width=20,height=2,text="SCISSOR",bg="#9B2335",fg="White",font=10,command=lambda:updatechoices("scissor")).grid(row=5,column=4)

#update message
def updatemessage(x):
    msg['text']=x

#update user score
def updateuserscore():
    score=int(Playerscore["text"])
    score+=1
    Playerscore["text"]=str(score)

def  updatecompscore():
    score=int(computerscore["text"])
    score+=1
    computerscore["text"]=str(score)
    
#check_winner
def  checkwin(player,computer):
        if(player==computer):
            updatemessage("Its a Tie!!!!!!!!!")
        elif player=="rock":
            if(computer=="paper"):
                updatemessage("You loose")
                updatecompscore()
            else:
                updatemessage("You Win!!!!!!")
                updateuserscore()
        elif player=="paper":
            if computer=="scissor":
                updatemessage("You loose")
                updatecompscore()
            else:
                updatemessage("You win!!!!")
                updateuserscore()
        elif player=="scissor":
            if computer=="rock":
                updatemessage("You loose")
                updatecompscore()
            else:
                updatemessage("You win!!!!!")
                updateuserscore()
        else:
            pass
#update choices
choices=["rock","paper","scissor"]
def updatechoices(x):
    # for computer
    import random
    compchoices=choices[random.randint(0,2)]
    if compchoices=="rock":
        comp_label.configure(image=rock_comp_image)
    elif compchoices=="paper":
        comp_label.configure(image=paper_comp_image)
    else:
        comp_label.configure(image=scissor_comp_image)
    #for user
    if x=="rock":
        user_label.configure(image=rock_image)
    elif  x=="paper":
            user_label.configure(image=paper_image)
    else:
        user_label.configure(image=scissor_image)
    checkwin(x,compchoices)  

    

window.mainloop()



