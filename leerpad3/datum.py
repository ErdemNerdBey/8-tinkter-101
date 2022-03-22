from datetime import date
from tkinter import messagebox
import tkinter as tk

window = tk.Tk()
window.geometry("600x200")

jarenSV = tk.StringVar()
maandenSV = tk.StringVar()
dagenSV = tk.StringVar()

tk.Label(
    window,
    text="kies een datum",
    font="arial"
).place(
    relx=0.42,
    rely=0.05,
)

tk.Label(
    window,
    text="jaren",
    font="arial"
).place(
    relx=0.23,
    rely=0.35,
)

tk.Label(
    window,
    text="maanden",
    font="arial"
).place(
    relx=0.45,
    rely=0.35,
)

tk.Label(
    window,
    text="dagen",
    font="arial"
).place(
    relx=0.72,
    rely=0.35,
)

tk.Spinbox(
    window,
    from_=1,
    to=69696969,
    textvariable=jarenSV,
).place(
    relx=0.15,
    rely=0.55,
)

tk.Spinbox(
    window,
    from_=1,
    to=12,
    textvariable=maandenSV,
).place(
    relx=0.4,
    rely=0.55,
)

tk.Spinbox(
    window,
    from_=1,
    to=31,
    textvariable=dagenSV,
).place(
    relx=0.65,
    rely=0.55,
)


def berekening():
    datumGekozen = date(int(jarenSV.get()), int(maandenSV.get()), int(dagenSV.get()))
    datumVandaag = date.today()

    datumTussen = datumGekozen - datumVandaag

    if datumGekozen == datumVandaag:
        messagebox.showinfo("Uitslag", "Dat is vandaag")
    elif datumVandaag < datumGekozen:
        messagebox.showinfo("Uitslag", f"Dat is over {datumTussen.days} dagen")
    else:
        messagebox.showinfo("uitslag", f"Dat was {datumTussen.days - datumTussen.days * 2} dagen geleden")


tk.Button(
    window,
    text="Berekenen",
    command=berekening,
    font="arial"
).place(
    relx=0.43,
    rely=0.75,
)


window.mainloop()
