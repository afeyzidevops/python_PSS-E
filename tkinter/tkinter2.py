from Tkinter import *

root =Tk()
root.title("welcom to PSS/E Asistant software")

#root.minsize(300,400)
#root.maxsize(640,450)
root.geometry("900x750")
root.resizable(width=False, height=False)

Aras_Label=Label(root,text="Aras Simlink asistance",foreground="red",font=("Titr",10),background="Green")
Aras_Label.pack()
Aras_Label.config(fg="brown")


              ################# add text editor wijet to project##########
##################################################################################################################
####

def Save_text():
   with open ("Output.text", "w") as F:
      F.write(text.get(1.0,END))
def load_text():
   with open("Output.text", "r") as F :
       data=F.read()
       text.insert(INSERT,data)
       
text=Text(root)
text.pack()
Button(root , text="Save",command=Save_text).pack()
Button(root , text="Open",command=load_text).pack()
##                                                                                                              ##
##################################################################################################################
root.mainloop()
