import tkinter as tk

def main():

    def kuva_varv(v):
        vastus.config(text=v)

    aken = tk.Tk()
    aken.geometry("400x100")
    aken.title("Värvi nupud")
   
    nupp1 = tk.Button(aken, bg="red", fg="red", font=("Arial", 16), command = lambda: kuva_varv("puane")) 
    nupp2 = tk.Button(aken, bg="orange", fg="orange", font=("Arial", 16), command = lambda: kuva_varv("oranz"))
    nupp3 = tk.Button(aken, bg="yellow", fg="yellow", font=("Arial", 16), command = lambda: kuva_varv("kollane"))
    nupp4 = tk.Button(aken, bg="green", fg="green", font=("Arial", 16), command = lambda: kuva_varv("roheline"))
    nupp5 = tk.Button(aken, bg="blue", fg="blue", font=("Arial", 16), command = lambda: kuva_varv("sinine"))
    
    vastus = tk.Label(aken, text=f"siia tuleb vastus")
    vastus.pack(side = "bottom", expand = True, fill="x")
    
    nupp1.pack(side="left", expand=True, fill="x")
    nupp2.pack(side="left", expand=True, fill="x")
    nupp3.pack(side="left", expand=True, fill="x")
    nupp4.pack(side="left", expand=True, fill="x")
    nupp5.pack(side="left", expand=True, fill="x")

    aken.mainloop()


if __name__ == "__main__":
    main()