import tkinter as tk

teller = 0
laatstHoogGedrukt = False
laatstLaagGedrukt = False

def omhoog():
    global teller, laatstHoogGedrukt, laatstLaagGedrukt
    teller += 1
    stringVar.set(teller)
    laatstHoogGedrukt = True
    laatstLaagGedrukt = False
    kleurVeranderen("")

def omlaag():
    global teller, laatstLaagGedrukt, laatstHoogGedrukt
    teller -= 1
    stringVar.set(teller)
    laatstLaagGedrukt = True
    laatstHoogGedrukt = False
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

def dubbelKlik(event):
    global teller
    if laatstLaagGedrukt == True:
        teller /= 3
    else:
        teller *= 3
    teller = int(teller)
    stringVar.set(teller)
    
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
label.bind('<Double-Button-1>', dubbelKlik)

buttonHoog.pack()
label.pack()
buttonLaag.pack()

window.mainloop()
