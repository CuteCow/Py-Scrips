from Tkinter import *

root = Tk()
root.attributes('-alpha', 0.1)

maxW = root.winfo_screenwidth()
maxH = root.winfo_screenheight()

root.geometry("{0}x{1}+0+0".format(maxW, maxH))

def callback(event):
    print "clicked at: ", event.x, "and: ", event.y

root.bind("<Button-1>", callback)

def Exit(event):
    root.destroy()
root.bind("<Escape>", Exit)


# root.overrideredirect(True)

root.mainloop()