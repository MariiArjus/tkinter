import tkinter as tk
aken = tk.Tk()

def main():
    aken.title("Profiili sisestamine")
    aken.geometry("300x350")
    label = tk.Label(aken, text="Lisame teksti!")
    label.pack()

# Loo raamid
frame = tk.Frame(aken)
frame.pack(pady=5, padx=5)
frame2 = tk.Frame(aken)
frame2.pack(pady=5, padx=5)
frame3 = tk.Frame(aken)
frame3.pack(pady=5, padx=5)
frame4 = tk.Frame(aken)
frame4.pack(pady=5, padx=5)

# Loo silt ja paiguta see raami
label = tk.Label(frame, text="Nimi")
label2 = tk.Label(frame2, text="Silmade värv")
label3 = tk.Label(frame3, text="Pikkus")
label4 = tk.Label(frame4, text="Kaal")
label.pack(side='left')
label2.pack(side='left')
label3.pack(side='left')
label4.pack(side='left')

# Loo sisestusväli ja paiguta see raami
entry = tk.Entry(frame)
entry2 = tk.Entry(frame2)
entry3 = tk.Entry(frame3)
entry4 = tk.Entry(frame4)
entry.pack(side='left')
entry2.pack(side='left')
entry3.pack(side='left')
entry4.pack(side='left')


nupp = tk.Button(aken, text="Salvesta", padx=10, pady=5)
if __name__ == "__main__":
    main()


aken.mainloop()