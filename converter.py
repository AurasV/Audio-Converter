from tkinter import *  # GUI
from tkinter import filedialog  # choose file dialog
import tkinter as tk  # GUI
from tkinter import ttk  # GUI
from pydub import AudioSegment  # audio conversion
import os  # file path

window = Tk()  # main window
window.title("Audio Converter")
window.resizable(False, False)  # deny resizing
frame = ttk.Frame(  # GUI frame
    master=window,
    padding=5
)
frame.grid(sticky="")  # frame alignment system

label1 = tk.Label(
    master=frame,
    text="Choose audio files: "  # first line text
)
label1.grid(column=0, row=0, sticky=W)


def no_file():  # no file selected
    no_file_window = Tk()
    no_file_window.resizable(False, False)
    frame_no_file = ttk.Frame(
        master=no_file_window,
        padding=5
    )
    frame_no_file.grid()
    attention = tk.Label(  # warning for no conversion selected
        master=frame_no_file,
        text="Please select a conversion!"
    )
    attention.grid(column=0, row=0)
    no_file_button = tk.Button(
        master=no_file_window,
        text="Ok",
        command=no_file_window.destroy
    )
    no_file_button.grid(column=0, row=1)
    no_file_window.mainloop()


def finished_popup():  # popup when finished
    finished_window = Tk()
    finished_window.resizable(False, False)
    frame_finished = ttk.Frame(
        master=finished_window,
        padding=5
    )
    frame_finished.grid()
    finished_label = tk.Label(
        master=frame_finished,
        text="Conversion Finished!"
    )
    finished_label.grid(column=0, row=0)
    finished_button = tk.Button(
        master=finished_window,
        text="Ok",
        command=finished_window.destroy
    )
    finished_button.grid(column=0, row=1)
    finished_window.mainloop()


def finished_button(choice, files, progress_bar):  # function for done! button
    total_files = len(files)
    for index, file in enumerate(files):
        file_extension = os.path.basename(file)[-4:].lower()
        try:
            if file_extension == ".mp3":
                song = AudioSegment.from_file(os.path.abspath(file), "mp3")  # mp3 format input
            elif file_extension == ".ogg":
                song = AudioSegment.from_file(os.path.abspath(file), "ogg")  # ogg format input
            elif file_extension == ".wav":
                song = AudioSegment.from_file(os.path.abspath(file), "wav")  # wav format input
            elif file_extension == ".m4a":
                song = AudioSegment.from_file(os.path.abspath(file), "m4a")  # m4a format input
            else:
                continue

            match choice.get():
                case ".mp3":
                    song.export(os.path.abspath(file)[:-4] + ".mp3", format="mp3")  # export path and format mp3
                case ".ogg":
                    song.export(os.path.abspath(file)[:-4] + ".ogg", format="ogg")  # export path and format ogg
                case ".wav":
                    song.export(os.path.abspath(file)[:-4] + ".wav", format="wav")  # export path and format wav
                case ".m4a":
                    song.export(os.path.abspath(file)[:-4] + ".m4a", format="m4a")  # export path and format m4a
                case "":
                    no_file()
        except Exception as e:
            print(f"Error processing file {file}: {e}")
        progress_bar['value'] = (index + 1) / total_files * 100
        progress_bar.update_idletasks()

    finished_popup()


def browse_click():  # when clicking on browse
    files = filedialog.askopenfilenames(  # get file paths
        initialdir="/",  # initial dir = root folder (Windows folder)
        title="Select audio files",  # title of the search window
        filetypes=(  # allowed audio formats
            ("Audio files", "*.mp3 *.ogg *.wav *.m4a"),
        ))
    if files:  # if there are files selected
        display_files = ", ".join([os.path.basename(file) for file in files[:3]])  # show first 3 files
        if len(display_files) > 10:
            display_files = display_files[:10]
        new_text.set(f"{display_files}...")

        choice = StringVar()  # the output choice
        choice.set(".mp3")  # default selection

        for widget in frame.grid_slaves(row=1):
            widget.grid_forget()
        for widget in frame.grid_slaves(row=2):
            widget.grid_forget()
        for widget in frame.grid_slaves(row=3):
            widget.grid_forget()

        options_frame = Frame(frame)
        options_frame.grid(row=1, column=0, columnspan=5, sticky=W)

        Radiobutton(options_frame, text=".mp3", variable=choice, value=".mp3").pack(side=LEFT, padx=(0, 10))
        Radiobutton(options_frame, text=".ogg", variable=choice, value=".ogg").pack(side=LEFT, padx=(0, 10))
        Radiobutton(options_frame, text=".wav", variable=choice, value=".wav").pack(side=LEFT, padx=(0, 10))
        Radiobutton(options_frame, text=".m4a", variable=choice, value=".m4a").pack(side=LEFT, padx=(0, 10))

        progress_bar = ttk.Progressbar(master=frame, length=200, mode='determinate')
        progress_bar.grid(column=0, row=2, columnspan=6, pady=10, sticky=W + E)

        finish = tk.Button(  # when finished
            master=frame,
            text="Convert Files!",
            command=lambda: finished_button(choice, files, progress_bar)
        )
        finish.grid(column=5, row=1, sticky=E)
    else:
        new_text.set("Browse: ")


new_text = tk.StringVar()  # button text
search = tk.Button(
    master=frame,
    textvariable=new_text,
    command=browse_click,
    height=1,
    width=10
)
search.grid(column=1, row=0, sticky=W)
new_text.set("Browse: ")

window.mainloop()
