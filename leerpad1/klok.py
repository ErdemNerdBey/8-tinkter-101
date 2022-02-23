from tkinter import *

from time import strftime

window = Tk()
window.title('klok')

def time():
    string = strftime('%H:%M:%S')
    label.config(text = string)
    label.after(1000, time)
 
label = Label(window, font = ('calibri', 40, 'bold'),
            background = 'cyan',
            foreground = 'green')

label.pack()
time()
 
window.mainloop()