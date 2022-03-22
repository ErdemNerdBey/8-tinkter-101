import tkinter as tk

kleur = "#FFF8DC"

window = tk.Tk()
window.geometry("500x500")

canvas = tk.Canvas(window)
canvas.pack(
    expand=True,
    fill='both'
)

for x in range(10):
    for y in range(10):
        if kleur == "#7B3F00":
            kleur = "#FFF8DC"
        else:
            kleur = "#7B3F00"
        canvas.create_rectangle(x*50, y*50, 500, 500, fill=kleur, outline="")

    if kleur == "#7B3F00":
        kleur = "#FFF8DC"
    else:
        kleur = "#7B3F00"

window.mainloop()
