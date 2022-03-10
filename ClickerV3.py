import tkinter
root = tkinter.Tk()
root.geometry("250x200")
root.config(bg="grey")
nummerdisplay=0

button = tkinter.Button(root,text="Up", bg="white", width="30")
button.pack(padx=10, pady=30)

nummerlabel = tkinter.Label(root, text=nummerdisplay, bg="white", width="30")
nummerlabel.pack()

button2 = tkinter.Button(root,text="Down", bg="white", width="30")
button2.pack(padx=10, pady=30)

def buttonUp():
    global nummerdisplay
    nummerdisplay = nummerdisplay + 1
    nummerlabel.config(text=nummerdisplay)
    if nummerdisplay >= 1:
        root.config(bg="green")
    if nummerdisplay == 0:
        root.config(bg="grey")
    nummerlabel.bind("<Double-Button-1>", DoubleClickUp)

def ButtonDown():
    global nummerdisplay
    nummerdisplay = nummerdisplay - 1
    nummerlabel.config(text=nummerdisplay)
    if nummerdisplay < 0:
        root.config(bg="red")
    elif nummerdisplay == 0:
        root.config(bg="grey")
    nummerlabel.bind("<Double-Button-1>", DoubleClickDown)

def LeaveLabel(e):
    if nummerdisplay > 0:
        root.config(bg="green")
    if nummerdisplay < 0:
        root.config(bg="red")
    if nummerdisplay == 0:
        root.config(bg="grey")

def EnterLabel(e):
    root.config(bg="yellow")

def DoubleClickUp(e):
    global nummerdisplay
    nummerdisplay = nummerdisplay * 3
    nummerlabel.config(text=nummerdisplay)

def DoubleClickDown(e):
    global nummerdisplay
    nummerdisplay = nummerdisplay / 3
    nummerlabel.config(text=nummerdisplay)

button.config(command=buttonUp)
button2.config(command=ButtonDown)

nummerlabel.bind("<Enter>", EnterLabel)
nummerlabel.bind("<Leave>", LeaveLabel)

root.mainloop()