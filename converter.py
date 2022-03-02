from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk

file_name = ""
window = Tk()
frame = ttk.Frame(
    master = window,
    padding = 5
    )
frame.grid()
lavel1 = tk.Label(
    master = frame,
    text = "Choose an audio file: "
).grid(column = 0, row = 0)
def browse_click():
    file = filedialog.askopenfilename(
        initialdir= "/",
        title = "Select audio file",
        filetypes = (
            ("mp3","*.mp3"),
            ("ogg","*.ogg"),
            ("aac","*.aac"),
            ("wav","*.wav")
            ))
    if(file != ""):
        new_text.set(file)
        choice = StringVar()
        columnf = -1
        if(file[-4:] != ".mp3"):
            columnf += 1
            Radiobutton(window, text = ".mp3", variable = choice, value = ".mp3").grid(row = 2,column = columnf)
        if(file[-4:] != ".ogg"):
            columnf += 1
            Radiobutton(window, text = ".ogg", variable = choice, value = ".ogg").grid(row = 2,column = columnf)
        if(file[-4:] != ".aac"):
            columnf += 1
            Radiobutton(window, text = ".aac", variable = choice, value = ".aac").grid(row = 2,column = columnf)
        if(file[-4:] != ".wav"):
            columnf += 1
            Radiobutton(window, text = ".wav", variable = choice, value = ".wav").grid(row = 2,column = columnf)
        columnf = -1
    else:
        new_text.set("Browse: ")
    
    

new_text = tk.StringVar()
search = tk.Button(
    master = frame,
    textvariable = new_text,
    command = browse_click,
).grid(column = 1, row = 0)
new_text.set("Browse: ")


window.mainloop()
#TO DO:
#fix the allignment on the radiobuttons
#add button that takes the data from the radiobuttons when pressed
#make everything else besides GUI duh!