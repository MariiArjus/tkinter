import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import messagebox

aken = ttk.Window(themename="darkly")
aken.title("Pitsa tellimisvorm")
aken.geometry("400x450")

def show_selection():
    print("Nupp on vajutatud!")


var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

def show_selection():
    if selected_option.get()=="kuller":
        UnicodeTranslateError = 3
    else:
        trans = 0
    kokku = var1.get() + var2.get() + var3.get() + int(suurus.get())+ trans
    messagebox.showinfo("pitsa hind", f"sinu pitsa hind on: {kokku}€")

# vaikimisi pitsa suurus
suurus = tk.StringVar(value = 12)

#id
label = tk.Label(aken, text="kasutaja id", font="Arial 16").pack(pady=10)
sisestus = tk.Entry(aken).pack()

# Loome raadionupud
label = tk.Label(aken, text="vali suurus", font="Arial 16").pack(pady=10)
radio_red = tk.Radiobutton(aken, text="Väike", variable=suurus, value=5)
radio_green = tk.Radiobutton(aken, text="Suur", variable=suurus, value=8)
radio_blue = tk.Radiobutton(aken, text="Pere", variable=suurus, value=12)
radio_red.pack()
radio_green.pack()
radio_blue.pack()

#lisandid
label = tk.Label(aken, text="vali lisandid", font="Arial 16").pack(pady=10)

checkbox1 = tk.Checkbutton(aken, text="juust", variable=var1, onvalue=2, offvalue=0).pack()
checkbox2 = tk.Checkbutton(aken, text="pepperoni", variable=var2, onvalue=2, offvalue=0).pack()
checkbox3 = tk.Checkbutton(aken, text="seen", variable=var3, onvalue=2, offvalue=0).pack()

#transport
label = tk.Label(aken, text="vali kättetoimetamine", font="Arial 16").pack(pady=10)

# Valikute määramine ja valitud väärtuse hoidja
valikud = ["tulen ise järgi", "kuller"]
selected_option = tk.StringVar()
selected_option.set("Vali transpordivalik")

# Dropdown menüü loomine
dropdown = tk.OptionMenu(aken, selected_option, *valikud)
dropdown.pack()


btn_confirm = tk.Button(aken, text="Arvuta hind", command=show_selection)
btn_confirm.pack()


aken.mainloop()

