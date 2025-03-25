import tkinter as tk
import ctypes
from PIL import Image, ImageTk

def loe_fail(failinimi):
    with open(failinimi, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    aken = tk.Tk()
    aken.title("tinker ülesanded")
    aken.geometry("400x400")
    aken.resizable(False, True)

    pilt = Image.open("norris.jpg")
    p= 0
    pilt = pilt.crop((0+p, 0+p, 200+p, 200+p))
    # pilt = pilt.resize((200, 200))
    foto = ImageTk.PhotoImage(pilt)

    # Pildi kuvamine Label abil
    label = tk.Label(aken, image=foto)
    label.image = foto
    label.pack()

        # Text näide
    tekst = tk.Text(aken, wrap=tk.WORD, font=("Arial", 12), fg="blue")
    scrollbar = tk.Scrollbar(aken, command=tekst.yview)
    tekst.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tekst.pack(expand=True, fill=tk.BOTH)

    failisisu = loe_fail("lorem.txt")
    tekst.insert(tk.INSERT, failisisu)
   
    label = tk.Label(aken, text="Chuck Norris", font= ('Arial', 16, 'bold'), fg="blue").pack()
    button = tk.Button(aken, text="Sulge", command=aken.destroy).pack()
   
    aken.mainloop()

# Käivitame peafunktsiooni
if __name__ == "__main__":
    main()