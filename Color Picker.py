from tkinter import *
from tkinter import colorchooser

root=Tk()
root.title("Color Picker")
root.geometry("400x400")

def color():
    my_color = colorchooser.askcolor()
    my_label=Label(root,text="dsifugdsifsd",bg=my_color[1],font=("Helvetica",20)).pack(pady=10)

submit_btn=Button(root,text="Choose Color",command=color).pack()


root.mainloop()