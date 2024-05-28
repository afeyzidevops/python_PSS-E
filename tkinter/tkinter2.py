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



              ############## edit  text box and add List box  wijet to project##########
##################################################################################################################
####
text=Text(root)
text.pack()

Listbox_Label=Label(root,font=12,text="Senarios",bg= "blue",fg="white")
Listbox_Label.pack(anchor=W)
ListBox=Listbox(root,font=12)
ListBox.pack(anchor=W)
ListBox.insert(1,"Senario_01")
ListBox.insert(2,"Senario_02")
ListBox.insert(3,"Senario_03")
ListBox.insert(4,"Senario_04")
ListBox.insert(5,"Senario_05")
ListBox.insert(6,"Senario_06")

def SaveSenario():
   with open ("Senario_.text", "w") as F:
      F.write(text.get())
      
def LoadSenario():
   with open("Senario_.text", "r") as F :
       data=F.read()
       
       text.insert(INSERT,data)
       
def ExequteSenario ():
   with open("Senario1","r") as S :
      Senario=S.read()
      text.insert(INSERT,Senario)
      
def AddSenario ():
   with open("Senario1","r") as S :
      Senario=S.read()
      text.insert(INSERT,Senario)
      
Button(root , text="Open",command=LoadSenario).pack()
Button=(root,text="Save senario",command=SaveSenario).pack(anchor=W)
Button=(root,text="Add senario",command=AddSenario).pack(anchor=W)
Button=(root,text="Execute Senario",command=ExequteSenario).pack(anchor=W)
##                                                                                                              ##
##################################################################################################################

root.mainloop()
