import tkinter
root = tkinter.Tk()
root.geometry("250x200")
root.config(bg="grey")
GetalDisplay=0
e=0

UpButton = tkinter.Button(root,text="Up", bg="white", width="30")
UpButton.pack(padx=10, pady=30)

GetalLabel = tkinter.Label(root, text=GetalDisplay, bg="white", width="30")
GetalLabel.pack()

DownButton = tkinter.Button(root,text="Down", bg="white", width="30")
DownButton.pack(padx=10, pady=30)

def buttonUp(e):
    global GetalDisplay
    GetalDisplay = GetalDisplay + 1
    GetalLabel.config(text=GetalDisplay)
    if GetalDisplay >= 1:
        root.config(bg="green")
    if GetalDisplay == 0:
        root.config(bg="grey")
    GetalLabel.bind("<Double-Button-1>", DoubleClickUp)
    root.bind("<Double-space>", DoubleClickUp)

def ButtonDown(e):
    global GetalDisplay
    GetalDisplay = GetalDisplay - 1
    GetalLabel.config(text=GetalDisplay)
    if GetalDisplay < 0:
        root.config(bg="red")
    elif GetalDisplay == 0:
        root.config(bg="grey")
    GetalLabel.bind("<Double-Button-1>", DoubleClickDown)
    root.bind("<Double-space>", DoubleClickDown)

def LeaveLabel(e):
    if GetalDisplay > 0:
        root.config(bg="green")
    if GetalDisplay < 0:
        root.config(bg="red")
    if GetalDisplay == 0:
        root.config(bg="grey")

def EnterLabel(e):
    root.config(bg="yellow")

def DoubleClickUp(e):
    global GetalDisplay
    GetalDisplay = GetalDisplay * 3
    GetalLabel.config(text=GetalDisplay)

def DoubleClickDown(e):
    global GetalDisplay
    GetalDisplay = GetalDisplay / 3
    GetalLabel.config(text=GetalDisplay)

UpButton.config(command=buttonUp)
DownButton.config(command=ButtonDown)

GetalLabel.bind("<Enter>", EnterLabel)
GetalLabel.bind("<Leave>", LeaveLabel)

root.bind("<Up>", buttonUp)
root.bind("<+>", buttonUp)
root.bind("<minus>", ButtonDown)
root.bind("<Down>", ButtonDown)

root.mainloop()