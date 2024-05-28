
from Tkinter import *
from Tkinter.ttk import *
root = Tk()
# Style() padding adds pixels inside the Button. The widget’s position is not changed.
ttk.Style().configure("TButton", padding=5, relief="flat")
button1 = ttk.Button(text="Button Example")
# pack() padding adds pixels outside the TButton. The widget’s position is changed.
button1.pack(side = BOTTOM, padx=<x_coordinate, pady=<y_coordinate>)
root.mainloop()
