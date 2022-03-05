from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
import os


window = Tk()
window.resizable(False, False)
frame = ttk.Frame(
    master = window,
    padding = 5
    )
frame.grid()
lavel1 = tk.Label(
    master = frame,
    text = "Choose an audio file: "
).grid(column = 0, row = 0)


def no_file():
    no_file_window = Tk()
    no_file_window.resizable(False, False)
    frame_no_file = ttk.Frame(
        master = no_file_window,
        padding= 5
    )
    frame_no_file.grid()
    attention = tk.Label(
        master = frame_no_file,
        text = "Please select a conversion!"
    ).grid(column=0, row=0)
    no_file_button = tk.Button(
        master = no_file_window,
        text = "Ok",
        command = no_file_window.destroy
    ).grid(column=0,row=1)
    no_file_window.mainloop()


def finished_button(choice,file):
    print(choice.get())
    if(choice.get() == ""):
        no_file()
    print(os.path.basename(file))


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
        columnf = 0
        if(file[-4:] != ".mp3"):
            columnf += 1
            Radiobutton(window, text = ".mp3", variable = choice, value = ".mp3").grid(row = 0,column = columnf)
        if(file[-4:] != ".ogg"):
            columnf += 1
            Radiobutton(window, text = ".ogg", variable = choice, value = ".ogg").grid(row = 0,column = columnf)
        if(file[-4:] != ".aac"):
            columnf += 1
            Radiobutton(window, text = ".aac", variable = choice, value = ".aac").grid(row = 0,column = columnf)
        if(file[-4:] != ".wav"):
            columnf += 1
            Radiobutton(window, text = ".wav", variable = choice, value = ".wav").grid(row = 0,column = columnf)
        columnf = -1
        finish = tk.Button(
            master = frame,
            text = "Done!",
            command = lambda: finished_button(choice,file)
        ).grid(column=2,row=0)
    else:
        new_text.set("Browse: ")
    

new_text = tk.StringVar()
search = tk.Button(
    master = frame,
    textvariable = new_text,
    command = browse_click,
    height = 1,
    width=10
).grid(column = 1, row = 0)
new_text.set("Browse: ")


window.mainloop()
#TO DO:
#fix the allignment on the radiobuttons
#add button that takes the data from the radiobuttons when pressed
#make everything else besides GUI duh!