import tkinter as tk

teller = 0


def omhoog():
    global teller
    teller += 1
    stringVar.set(teller)
    kleurVeranderen()

def omlaag():
    global teller
    teller -= 1
    stringVar.set(teller)
    kleurVeranderen()

def kleurVeranderen():
    if teller < 0:
        window.config(bg = "red")
    elif teller == 0:
        window.config(bg = "grey")
    else:
        window.config(bg = "green")
      

window = tk.Tk()
window.config(
    padx = 30,
    pady = 30,
)

stringVar = tk.StringVar(value = teller)

label = tk.Label(
    padx = 49,
    pady = 2,
)

buttonHoog = tk.Button(
    padx = 50,
    pady = 2,
    command = omhoog,
)

buttonLaag = tk.Button(
    padx = 50,
    pady = 2,
    command = omlaag,
)

buttonHoog.pack()

label.config(
    textvariable = stringVar,
)

label.pack()

buttonLaag.pack()

window.mainloop()
