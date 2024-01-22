from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window
root = Tk()
root.title("rock scissoer paper")
root.configure(background= "#9b59b6")

#picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock1.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper1.png"))
scossor_imgimg_comp = ImageTk.PhotoImage(Image.open("scissors.png"))


# insert picture
user_label = Label(root,image=scissor_img, bg="#9b59b6")
comp_label = Label(root,image=scossor_imgimg_comp, bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)


#scroes
playerScore = Label(root, text=0, font=("Arial",100), bg="#9b59b6", fg="white")
compScore = Label(root, text=0, font=("Arial",100), bg="#9b59b6", fg="white")
compScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

#indicators
user_indicator =Label(root,font=50, text= "USER", bg="#9b59b6", fg="white")
comp_indicator =Label(root,font=50, text= "COMPUTER", bg="#9b59b6", fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#message
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
    msg['text'] = x

# update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)


#update computer score
def updatecompScore():
        score = int(compScore["text"])
        score += 1
        compScore["text"] = str(score)
#check winner
def checkwin(player,computer):
    if player == computer:
        updateMessage("Its a Tie!!!")
    elif player == "Rock":
        if computer == "paper":
            updateMessage("You Loose")
            updatecompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Loose")
            updatecompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "Rock":
            updateMessage("You Loose")
            updatecompScore()
        else:
            updateMessage("You Win")
            updateUserScore()        

choices = ["Rock","scissor","paper"]
#update choices
def updatechoices(x):

#for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "Rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scossor_imgimg_comp)


#for user    
    if x=="Rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkwin(x,compChoice)



#buttons
rock = Button(root,width=20,height=2,text="Rock", 
              bg="#FF3E4D", fg="white",command= lambda:updatechoices("Rock"))
paper = Button(root,width=20,height=2,text="paper",
               bg="#FAD02E", fg="white", command= lambda:updatechoices("paper"))
scissor = Button(root,width=20,height=2,text="scissor",
                 bg="#0ABDE3", fg="white", command= lambda:updatechoices("scissor"))
rock.grid(row=2,column=1)
scissor.grid(row=2,column=2)
paper.grid(row=2,column=3)

root.mainloop()




