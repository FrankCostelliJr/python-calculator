from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text='Look, I clicked!')
    myLabel.pack()


myButton = Button(root, text='Click Me!', command=myClick, fg="blue", bg="black")

myButton.pack()

root.mainloop()
