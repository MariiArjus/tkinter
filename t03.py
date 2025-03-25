import tkinter as tk


def main():
    aken = tk.Tk()
    aken.geometry("300x300")

    # Funktsioon, mis kuvab sisestused
    def kuva_sisestus():
        laenusumma = int(sisestus1.get())  # Võtab esimese sisestuse
        kuuintressimäär = float(sisestus2.get())/12/100  # Võtab teise sisestuse
        maksete_arv = int(sisestus3.get())*12
        
        igakuine_makse = laenusumma * kuuintressimäär / (1 - (1 + kuuintressimäär) ** -maksete_arv)
        print(igakuine_makse)
        
        vastus = tk.Label(aken, text=f"igakuine makse: {maksete_arv:.2f}")
        vastus.pack()

    # Esimene sisestusväli
    sisestus1 = tk.Entry(aken, text="laenusumma (€)".pack(pady=(10, 0)))
    sisestus1 = tk.Entry(aken)
    sisestus1.pack()
   
    # Teine sisestusväli
    sisestus2 = tk.Entry(aken, text="Aastane intressimäär (%)".pack(pady=(10, 0)))
    sisestus2 = tk.Entry(aken)
    sisestus2.pack()
   
    sisestus3 = tk.Entry(aken, text="Laenuperiood (aastates)".pack(pady=(10, 0)))
    sisestus3 = tk.Entry(aken)
    sisestus3.pack()
   
    # Nupp, mis käivitab funktsiooni kuva_sisestus
    nupp = tk.Button(aken, text="Vajuta mind", command=kuva_sisestus)
    nupp.pack()

    aken.mainloop()

if __name__ == "__main__":
    main()