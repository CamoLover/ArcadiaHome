from email.mime import image
from inspect import Attribute
from tkinter import *
from tkinter import ttk
from tkinter.tix import IMAGE
from turtle import position, right
from PIL import Image,ImageTk
import os, webbrowser 



#Array game
GameName = ["PacManBTN", "BackroomBTN", "MarioBrosBTN"]
GamePath = ["", "", ""]
GameIMAG = ["PacMan.png", "", "smbNES.jpg"]

#Command :
def pacmancmd():
   webbrowser.open('https://google.com')
def backroomcmd():
   webbrowser.open('https://google.com')
def mariocmd():
   webbrowser.open('https://google.com')


rotationactive = 0

#Configuration windows et BG:
root = Tk()
#root.geometry("650x250")
root.title("Arcadia Main Menu")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#Image var
arrowright = ImageTk.PhotoImage(Image.open("arrowright.png"))
arrowleft = ImageTk.PhotoImage(Image.open("arrowleft.png"))
PacMan = ImageTk.PhotoImage(Image.open("PacMan.png"))
backroom = ImageTk.PhotoImage(Image.open("PacMan.png"))
Mario = ImageTk.PhotoImage(Image.open("smbNES.jpg"))

#Image background:
bg = Image.open("backgroundImage.ppm")
resized_image= bg.resize((screen_width,screen_height), Image.ANTIALIAS)
tk_img = ImageTk.PhotoImage(resized_image)
#Label Canvas base :
label= Label(root, text= "Hello World!", font=('Times New Roman bold',20))
label = ttk.Label(root, image=tk_img)
label.place(x=0, y=0)


btnARROWLEFT = Button(root, image = arrowleft, command=pacmancmd)
btnARROWLEFT.place(x=0, y=350)  
btnARROWRIGHT = Button(root, image = arrowright, command=pacmancmd)
btnARROWRIGHT.place(x=1680, y=350)  
btnPACMAN = Button(root, image = PacMan, command=pacmancmd)
btnPACMAN.place(x=405, y=387)  
btnBACKROOM = Button(root, image = backroom, command=backroomcmd)
btnBACKROOM.place(x=810, y=387)  
btnMARIO = Button(root, image = Mario, command=mariocmd)
btnMARIO.place(x=1215, y=387)  



label.pack(padx=0, pady=0)
frm = ttk.Frame(root, padding=10)
root.attributes('-fullscreen', True)




ttk.Label(frm, text="Arcadia main menu").grid(column=0, row=0)
root.mainloop()