import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from tkinter import filedialog as fd
from PIL import Image 
import PIL


def open_directory():
    filename = fd.askopenfilename()
    if filename:
        dir_label.config(text=f"Kausta valik õnnestus")
        inputtxt.insert(tk.INSERT, filename)
    else:
        dir_label.config(text="Faili kataloogi avamine ei õnnestunud.")


def save_directory():
    file = fd(filetypes = files, defaultextension = files) 

aken = tk.Tk()
aken.title("pildi suuruse muutmine")
aken.geometry("450x400")


label = tk.Label(aken, text = "Pildi suurus 200x200", font= "Arial 24")
label.pack(pady=10)

inputtxt = tk.Text(aken, height = 10, width = 50)
inputtxt.pack(pady = 10)

open_button = tk.Button(aken, text="vali pildid", command=open_directory)
open_button.pack(pady = 10)

save_button = tk.Button(aken, text="salvesta pildid", command=save_directory)
save_button.pack(pady = 10)

dir_label = tk.Label(aken, text="")
dir_label.pack(pady=10)

aken.mainloop()