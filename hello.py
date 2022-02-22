import tkinter

window = tkinter.Tk()
window.title("Hello Tkinter!!")
window.geometry("250x250")
window.configure(bg = "cyan")

Font_tuple = ("Comic Sans MS", 20, "bold")

box1 = tkinter.Label(
    window,
    fon = Font_tuple,
    text = "Hello Tkinter!",
    fg = "green",
    bg = "#bfff00",
)

box1.pack(
    ipadx = 15,
    ipady = 70,
    expand = True,
)

window.mainloop()