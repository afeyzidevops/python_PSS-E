from Tkinter import *

window =Tk()
window.title("welcom to PSS/E Asistant software")

#window.minsize(300,400)
#window.maxsize(640,450)
window.geometry("600x480")
window.resizable(width=False, height=False)

Aras_Label=Label(window,text="Aras Simlink asistance",foreground="red",font=("Titr",20),background="Green")
Aras_Label.pack()
Aras_Label.config(fg="brown")

##################################################################################################################
##
Buttom_solve=Label(window,text="count: ")
Buttom_solve.pack()
counter=0
def Counter():
   global counter
   counter +=1
   #print counter
   Buttom_solve.config(text="count: %i"%counter)
   
Button(window,text="Solve",command=Counter ,font=('TITR',10),bg="yellow", fg="blue").pack()

##                                                                                                              ##
##################################################################################################################



##################################################################################################################
##                                                                                                              ##
open_sav_Label=Label(window,text="Please insert a *.sav file ",foreground="red",font=("Titr",20),background="Green")
open_sav_Label.pack()

def open_sav():
   open_sav_Label.config(text="*.sav file inserted ",fg="green",bg="brown")
   

Button(window,text="open **.sav file",command=open_sav ,font=('TITR',10),bg="yellow", fg="blue").pack()
##                                                                                                              ##
##################################################################################################################

window.mainloop()
