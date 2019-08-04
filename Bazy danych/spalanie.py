import tkinter
from tkinter import messagebox
def iloczyn():
    try:
        a = int(a_entry.get())
        b = float(b_entry.get())
        c = int(c_entry.get())
        wynik = (c/100) * a * b
        wynik_label.configure(text=wynik)
    except ValueError:
        messagebox.showerror("Błędne dane !", "Musisz wprowadzic dane liczbowe")

root = tkinter.Tk()
root.columnconfigure(1, weight= 1)

a_label = tkinter.Label(master=root, text="spalanie l/100 km")
a_label.grid(row=2, column=0)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=2, column=1)
b_label = tkinter.Label(master=root, text="cena paliwa")
b_label.grid(row=1, column=0)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=1, column=1)
c_label = tkinter.Label(master=root, text="dystans")
c_label.grid(row=0, column=0)
c_entry = tkinter.Entry(master=root)
c_entry.grid(row=0, column=1)
sum_buttom = tkinter.Button(master=root, text="oblicz spalanie", command=iloczyn)
sum_buttom.grid(row=4, column=0)


wynik_label = tkinter.Label(master=root, text = "Wynik: - ")
wynik_label.grid(row=3, column=0)

root.mainloop()