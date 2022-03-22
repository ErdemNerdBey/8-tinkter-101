import tkinter as tk
import random
import tkinter.messagebox

knoppen = [
    "w",
    "a",
    "s",
    "d",
    "space",
    "Button-1",
    "Double-Button-1",
    "Triple-Button-1"
]

randomKlik = ""

score = 0

root = tk.Tk()

tk.Label(
    root,
    text="hoeveel secondens wil je spelen?"
).pack()


timeVar = tk.StringVar(value='20')

tk.Entry(root, textvariable=timeVar).pack()

tk.Button(
    root,
    text="ok",
    command=lambda: root.destroy()
).pack()

root.mainloop()
time = int(timeVar.get())

window = tk.Tk()
window.geometry("600x350")

countdown = tk.StringVar(value=str(time))
scoreCount = tk.StringVar(value=f"score : {score}")
textPunten = tk.StringVar(value=randomKlik)


def timeCounter():
    global time, score
    countdown.set(str(time))
    time -= 1
    if time == -1:
        MsgBox = tk.messagebox.askquestion("tijd is over", f"jouw score is {score}.\nwil je overnieuw spelen?",
                                           icon="info")
        if MsgBox == "yes":
            time = 20
            score = 0
            scoreCount.set(str(score))
        else:
            window.destroy()
    timeLabel.after(1000, timeCounter)


def puntenBerekenen():
    global score
    if randomKlik in ["Button-1", "Double-Button-1", "Triple-Button-1"]:
        score += 2
    else:
        score += 1
    scoreCount.set(str(score))
    puntenLabel.destroy()
    window.unbind(f"<{randomKlik}>")
    punten()


def punten():
    global randomKlik, puntenLabel
    randomPosX = random.randint(0, 550)
    randomPosY = random.randint(30, 330)
    randomKlik = random.choice(knoppen)
    textPunten.set(randomKlik)

    puntenLabel = tk.Label(
        textvariable=textPunten,
        bg="black",
        fg="white",
    )
    if randomKlik in ["Button-1", "Double-Button-1", "Triple-Button-1"]:
        puntenLabel.bind(f"<{randomKlik}>", lambda e: puntenBerekenen())
    else:
        window.bind(f"<{randomKlik}>", lambda e: puntenBerekenen())
    puntenLabel.place(
        x=randomPosX,
        y=randomPosY,
    )


bgScoreTimeLabel = tk.Label(
    bg="#C8C8C8",
)

bgScoreTimeLabel.pack(
    ipady=6,
    fill="x"
)

scoreLabel = tk.Label(
    textvariable=scoreCount,
    bg="#DCDCDC",
)

scoreLabel.place(
    relx=0.01,
    y=6,
)

timeLabel = tk.Label(
    textvariable=countdown,
    bg="#DCDCDC",
)

timeLabel.place(
    relx=0.5,
    y=6,
)


def start():
    punten()
    timeCounter()
    button.destroy()


button = tk.Button(
    window,
    text="klik hier om te beginnen",
    command=start,
)
button.place(
    x=240,
    y=150,
)

window.mainloop()
