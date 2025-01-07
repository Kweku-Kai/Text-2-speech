import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

#The working part of the code
engine = pyttsx3.init()

#This part of the code is what allows for the text to be read out
def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    
    def setvoice():
        if(gender == 'Male'): #This part of the code allows for the choice of the voice of the reader
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if (text): #This part of the code allows for the choice of the speed of the reading
        if(speed == "Fast"):
            engine.setProperty('rate', 250)
            setvoice()
        elif(speed == 'Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

#This part of the code is what allows for the audio to be saved
def download():
    t = text_area.get('0.0', 'end')
    path=filedialog.askdirectory()
    os.chdir(path)
    engine.save_to_file(t, 'text.mp3')
    engine.runAndWait()


#Graphical part of the code
root=Tk()
root.title("Text2Speech")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#a65adb")


#Top Frame
Top_frame=Frame(root,bg="white",width=900,height=120)
Top_frame.place(x=0,y=0)


Label(Top_frame,text="Text2Speech", font="Forte 20 bold", bg="white",fg="purple").place(x=380,y=45)

###########

text_area=Text(root,font="Montserrat 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text="VOICE",font="Montserrat 15 bold", bg="#a65adb", fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="Montserrat 15 bold", bg="#a65adb", fg="white").place(x=760,y=160)

gender_combobox=Combobox(root,values=['Male','Female'],font="Montserrat 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(root,values=['Fast','Normal','Slow'],font="Montserrat 14",state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal') 

btn=Button(root,text="Speak",width=10,font="Montserrat 14 bold",command=speaknow)
btn.place(x=550,y=280)

savet=Button(root,text="Save",width=10,font="Montserrat 14 bold",command=download)
savet.place(x=730,y=280)


root.mainloop()
