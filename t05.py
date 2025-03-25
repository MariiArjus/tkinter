import tkinter as tk

aken = tk.Tk()

# Loo raamid
frame = tk.Frame(aken)
frame.pack(pady=5, padx=5)
frame2 = tk.Frame(aken)
frame2.pack(pady=5, padx=5)
frame3 = tk.Frame(aken)
frame3.pack(pady=5, padx=5)

# Loo silt ja paiguta see raami
label = tk.Label(frame, text="Nimetus:")
label2 = tk.Label(frame2, text="Nimetus2:")
label3 = tk.Label(frame3, text="Nimetus3:")
label.pack(side='left')
label2.pack(side='left')
label3.pack(side='left')



# Loo sisestusväli ja paiguta see raami
entry = tk.Entry(frame)
entry2 = tk.Entry(frame2)
entry3 = tk.Entry(frame3)
entry.pack(side='left')
entry2.pack(side='left')
entry3.pack(side='left')


aken.mainloop()