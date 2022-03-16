import tkinter as tk

teller = 0

def omhoog():
    global teller, laatstHoogGedrukt, laatstLaagGedrukt
    teller += 1
    stringVar.set(teller)
    kleurVeranderen("")

def omlaag():
    global teller, laatstLaagGedrukt, laatstHoogGedrukt
    teller -= 1
    stringVar.set(teller)
    kleurVeranderen("")

def kleurVeranderen(event):
    if teller < 0:
        label.config(bg = "red")
        window.config(bg = "red")
    elif teller == 0:
        label.config(bg = "grey")
        window.config(bg = "grey")
    else:
        label.config(bg = "green")
        window.config(bg = "green")

def geelMaken(event):
    window.config(bg = "yellow")
    label.config(bg = "yellow")


window = tk.Tk()
window.config(
    padx = 30,
    pady = 30,
)

stringVar = tk.StringVar(value = teller)

label = tk.Label()

label.config(
    textvariable = stringVar,
)

buttonHoog = tk.Button(
    text = "+1",
    padx = 50,
    pady = 2,
    command = omhoog,
)


buttonLaag = tk.Button(
    text = "-1",
    padx = 50,
    pady = 2,
    command = omlaag,
)

label.bind('<Enter>', geelMaken)
label.bind('<Leave>', kleurVeranderen)

buttonHoog.pack()
label.pack()
buttonLaag.pack()

window.mainloop()
