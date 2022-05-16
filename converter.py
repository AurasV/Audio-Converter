from tkinter import * #gui
from tkinter import filedialog #choose file dialog
import tkinter as tk #gui
from tkinter import ttk #gui
from pydub import AudioSegment #audio conversion
import os #file path


window = Tk() #main window
window.title("Audio Converter")
window.resizable(False, False) #deny resizing
frame = ttk.Frame( #gui frame
    master = window,
    padding = 5
    )
frame.grid() #frame allignment system
lavel1 = tk.Label(
    master = frame,
    text = "Choose an audio file: " #first line text
).grid(column = 0, row = 0)


def no_file(): #no file selected
    no_file_window = Tk()
    no_file_window.resizable(False, False)
    frame_no_file = ttk.Frame(
        master = no_file_window,
        padding= 5
    )
    frame_no_file.grid()
    attention = tk.Label( #warning for no conversion selected
        master = frame_no_file,
        text = "Please select a conversion!"
    ).grid(column=0, row=0)
    no_file_button = tk.Button(
        master = no_file_window,
        text = "Ok",
        command = no_file_window.destroy
    ).grid(column=0,row=1)
    no_file_window.mainloop()


def finished_button(choice,file): #function for done! button
    match os.path.basename(file)[-4:]:
        case ".mp3":
            try:
                song = AudioSegment.from_file(os.path.abspath(file), "mp3") #mp3 format input
            except:
                song = AudioSegment.from_file(os.path.abspath(file), "m4a") # mp3 format input but aac encoded for some reason
        case ".ogg":
            song = AudioSegment.from_file(os.path.abspath(file), "ogg") #ogg format input
        case ".wav":
            song = AudioSegment.from_file(os.path.abspath(file), "wav") #wav format input
    match choice.get():
        case ".mp3":
            song.export(os.path.abspath(file)[:-4] + ".mp3", format = "mp3") #export path and format mp3
        case ".ogg":
            song.export(os.path.abspath(file)[:-4] + ".ogg", format = "ogg") #export path and format ogg
        case ".wav":
            song.export(os.path.abspath(file)[:-4] + ".wav", format = "wav") #export path and format wav
        case "":
            no_file()
    


def browse_click(): #when clicking on browse
    file = filedialog.askopenfilename( #get file path
        initialdir= "/", #initial dir = root folder (windows folder) 
        title = "Select audio file", #title of the search window
        filetypes = ( #allowed audio formats
            ("mp3","*.mp3"), 
            ("ogg","*.ogg"),
            ("wav","*.wav")
            ))
    if(file != ""): #if there's a file selected
        new_text.set(os.path.basename(file)[:10] + "...")
        choice = StringVar() #the output choice
        columnf = 0
        if(file[-4:] != ".mp3"): #mp3 button
            columnf += 1
            Radiobutton(window, text = ".mp3", variable = choice, value = ".mp3").grid(row = 0,column = columnf)
        if(file[-4:] != ".ogg"): #ogg button
            columnf += 1
            Radiobutton(window, text = ".ogg", variable = choice, value = ".ogg").grid(row = 0,column = columnf)
        if(file[-4:] != ".wav"): #wav button
            columnf += 1
            Radiobutton(window, text = ".wav", variable = choice, value = ".wav").grid(row = 0,column = columnf)
        columnf = -1
        finish = tk.Button( #when finished
            master = frame,
            text = "Done!",
            command = lambda: finished_button(choice,file)
        ).grid(column=2,row=0)
    else:
        new_text.set("Browse: ")
    

new_text = tk.StringVar() #button text
search = tk.Button(
    master = frame,
    textvariable = new_text,
    command = browse_click,
    height = 1,
    width = 10
).grid(column = 1, row = 0)
new_text.set("Browse: ")


window.mainloop()