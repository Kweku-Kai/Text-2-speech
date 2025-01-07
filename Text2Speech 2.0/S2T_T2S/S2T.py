import tkinter as tk
from tkinter import *
from tkinter import filedialog
import speech_recognition as sr


#Working part of the code
r= sr.Recognizer()

#this part of the code generates the text of from the audio and needs internet connection to work
def uploadgenerate():
    file_path = filedialog.askopenfilename(title='Select a file')

    with sr.AudioFile(file_path) as source: # this part of the code calls the upload funtion in the code
        audio = r.record(source)
        
        try:
            text_area.delete('0.0', 'end') #this clears the text in the text box
            text = r.recognize_google(audio) #the api converts the audio to text
            text_area.insert('0.0', text) #this inserts the text in the text box
            
        except sr.UnknownValueError: #this error is printed wwhenn the api cannot recognise the audio
            print("Couldn't recognise audio")
            
        except sr.RequestError as e: #this error is printed when there is no internet connection
            print(e)

# this part of the code saves the text file            
def save():
    file_path = filedialog.askopenfilename(title='Select a file')
    with open(file_path, 'w') as file:
        file.write(text_area.get('0.0','end'))

# this part of the code is what uploads the audio file
def record():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source) #Starts Listening
        try:
            text_area.delete('0.0', 'end')
            text = r.recognize_google(audio) #Recognizes audio in English 
            text_area.insert('0.0', text)
        except sr.RequestError as e: #When there is no notable speech
            print(e)

#Graphical part of the code
root=Tk()
root.title("Speech2Text")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#a65adb")


#Top Frame
Top_frame=Frame(root,bg="white",width=900,height=120)
Top_frame.place(x=0,y=0)

Label(Top_frame,text="Speech2Text", font="Forte 20 bold", bg="white",fg="purple").place(x=380,y=45)

###########

text_area=Text(root,font="Montserrat 14",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

btn=Button(root,text="Record",width=10,font="Montserrat 14 bold", command=record)
btn.place(x=550,y=250)

savet=Button(root,text="Save as",width=10,font="Montserrat 14 bold",command=save)
savet.place(x=730,y=250)

btn=Button(root,text="Upload and Generate",width=20,font="Montserrat 14 bold", command=uploadgenerate)
btn.place(x=580,y=300)


root.mainloop()
