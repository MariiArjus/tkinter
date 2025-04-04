import tkinter as tk
import ctypes


def main():
    # DPI teadlikkuse seadistamine kõrge DPI ekraanide jaoks
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception as e:
        print(e)

    aken = tk.Tk()
    aken.title("Mario ülesanded")
    aken.geometry("400x400")
   
    label = tk.Label(aken, text="Mario ülesanded").pack()
    button = tk.Button(aken, text="Sulge", command=aken.destroy).pack()
    
    aken.resizable(True, False)
   
    aken.mainloop()

if __name__ == "__main__":
    main()
    
    