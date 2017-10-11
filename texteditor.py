import sys

#if python 2.7
#from Tkinter import *
# if python 3.3 <

from tkinter import*
# if python 2.7
#import tkFileDialog

# if python 3.3 <

import tkinter.filedialog as tkFileDialog

root = Tk("Text Editor")

text = Text(root)

text.grid()

def saveas():
	global text

	t = text.get("1.0", "end-1c")
	savelocation = tkFileDialog.asksaveasfilename()

	file1 = open(savelocation, "w+")

	file1.write(t)

	file1.close()

button = Button(root, text="Save", command= saveas)
button.grid()

root.mainloop()
