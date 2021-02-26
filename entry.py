from tkinter import  *



root = Tk()

myEntry = Entry(root)
myEntry.pack()
def myClick():
    myLabel = Label(root,text = "Look! I clicked a Button!")
    myLabel.pack()

myButton = Button(root,text = "Click me!",command = myClick, fg = "blue", bg = "#00000")
myButton.pack()

root.mainloop()