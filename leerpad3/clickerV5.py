import tkinter as tk

stopper = False
teller = 0
laatstGedrukt = 0


def omhoog():
    global teller, laatstGedrukt
    checkbox.config(state="normal")
    teller += 1
    stringVar.set(str(teller))
    laatstGedrukt = 1
    kleurVeranderen()


def omlaag():
    global teller, laatstGedrukt
    checkbox.config(state="normal")
    teller -= 1
    stringVar.set(str(teller))
    laatstGedrukt = 2
    kleurVeranderen()


def kleurVeranderen():
    if teller < 0:
        label.config(bg="red")
        window.config(bg="red")
    elif teller == 0:
        label.config(bg="grey")
        window.config(bg="grey")
    else:
        label.config(bg="green")
        window.config(bg="green")


def geelMaken():
    window.config(bg="yellow")
    label.config(bg="yellow")


def dubbelKlik():
    global teller, laatstGedrukt
    if laatstGedrukt in [2, 3]:
        teller /= 3
        laatstGedrukt = 3
    else:
        teller *= 3
        laatstGedrukt = 4
    teller = int(teller)
    stringVar.set(str(teller))


def autoClicker():
    global stopper, teller
    if variable.get() != "stoppen":
        if laatstGedrukt == 1:
            teller += 1
        elif laatstGedrukt == 2:
            teller -= 1
        elif laatstGedrukt == 3:
            teller /= 3
        else:
            teller *= 3
        stringVar.set(str(int(teller)))
        window.after(200, autoClicker)


window = tk.Tk()
window.config(
    padx=30,
    pady=30,
)

stringVar = tk.StringVar(value=str(teller))

label = tk.Label()

label.config(
    textvariable=stringVar,
)

buttonHoog = tk.Button(
    text="+1",
    padx=50,
    pady=2,
    command=omhoog,
)

buttonLaag = tk.Button(
    text="-1",
    padx=50,
    pady=2,
    command=omlaag,
)

variable = tk.StringVar()

checkbox = tk.Checkbutton(
    window,
    text='auto click',
    command=autoClicker,
    variable=variable,
    offvalue="stoppen",
    state="disabled"
)

window.bind('<plus>', lambda e: omhoog())
window.bind('<minus>', lambda e: omlaag())
window.bind('<space>', lambda e: dubbelKlik())
label.bind('<Enter>', lambda e: geelMaken())
label.bind('<Leave>', lambda e: kleurVeranderen())
label.bind('<Double-Button-1>', lambda e: dubbelKlik())

buttonHoog.pack()
label.pack()
buttonLaag.pack()
checkbox.pack()

window.mainloop()
