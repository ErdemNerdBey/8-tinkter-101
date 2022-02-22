from os import remove
from tkinter import *
import random
from tkinter.messagebox import showinfo

grabbelItems = [
    "slaafje", 
    "nitraten", 
    "gestolen bankpas", 
    "giftige slang", 
    "teen nagels", 
    "1KG aardappelen", 
    "baksteen", 
    "huis", 
    "Heineken aandeel", 
    "ferrari autoband ventieldopje"
] 

def test():
    if len(grabbelItems) != 0:
        i = random.choice(grabbelItems)
        showinfo(
            "Gefeliciteerd",
            f"Je hebt een {i} gegrabbeld!",
        )
        grabbelItems.remove(i)
        stringVar.set(f"klik op de knop om te grabbelen.\ner zijn {len(grabbelItems)} producten over")
    else:
        button["state"] = DISABLED
        button.configure(
            text = "de grabbelton is leeg",
            bg = "red",
        )
        stringVar.set("de grabbelton is leeg")

window = Tk()
window.geometry("250x250")
window.configure(bg = "cyan")

stringVar = StringVar(value = f"klik op de knop om te grabbelen.\ner zijn {len(grabbelItems)} producten over")

label = Label(window,)
label.configure(
    textvariable = stringVar,
    bg = "#00ffe6"
)

button = Button(
    text = "klik hier om te grabbelen",
    bg = "#00ffe6",
    command = test,
)
label.pack(expand = True)

button.pack(expand = True)


window.mainloop()