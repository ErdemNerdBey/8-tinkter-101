from tkinter import *

grootte = 50
window = Tk()
aftellen = 6
kleuren = ["red", "orange", "yellow", "#bfff00", "green", "cyan",]



def groterMaken():
    global grootte, aftellen, tellen
    window.configure(bg = f"{kleuren[aftellen - 1]}")
    print(aftellen)
    window.geometry(f'{grootte}x{grootte}')

    grootte += 50
    aftellen -= 1
    window.after(2000, groterMaken)
    if aftellen == -1:
        window.configure(bg = f"{kleuren[aftellen - 1]}")
        print("BOOOMMM!")
        window.destroy()
        return
    
groterMaken()




window.mainloop()