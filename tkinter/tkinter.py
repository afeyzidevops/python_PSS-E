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
##                                                                                                              ##
counter=0
def counter():
   global counter
   counter +=1
   #print counter
   Buttom_solve.config(text="count: %s "%counter)
   
Button(window,text="Solve",command=counter ,font=('TITR',10),bg="yellow", fg="blue").pack()
Buttom_solve=Label(window,text="count: ")
Buttom_solve.pack()
##                                                                                                              ##
##################################################################################################################



##################################################################################################################
##                                                                                                              ##
open_sav_Label=Label(window,text="Aras Simlink asistance",foreground="red",font=("Titr",20),background="Green")
open_sav_Label.pack()

def open_sav():
   open_sav_Label.config(fg="green")
   Buttom_solve.config(text="file opened: %s ", bg='green')

Button(window,text="open **.sav file",command=open_sav ,font=('TITR',10),bg="yellow", fg="blue").pack()
##                                                                                                              ##
##################################################################################################################

window.mainloop()
