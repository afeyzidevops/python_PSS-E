from Tkinter import *

root =Tk()
root.title("welcom to PSS/E Asistant software")

root.geometry("1080x750")
root.resizable(width=False, height=False)


              ############## edit  text box and add List box  wijet to project##########
##################################################################################################################
####
text=Text(root)
text.pack(anchor=N)

#Listbox_Label=Label(root,font=10,text="Senarios",bg= "blue",fg="white")
#Listbox_Label.pack(anchor=W)
ListBox=Listbox(root,font=10)
ListBox.pack(anchor=W)
ListBox.insert(1,"Senario_01")
ListBox.insert(2,"Senario_02")
ListBox.insert(3,"Senario_03")
ListBox.insert(4,"Senario_04")
ListBox.insert(5,"Senario_05")
ListBox.insert(6,"Senario_06")
#------------------------------------------------------------------------------LoadSenario
def LoadSenario():
   with open("Senario_01.text", "r") as F :
       data=F.read()    
       text.insert(INSERT,data)
Button(root,text="Open",command=LoadSenario).pack()
#------------------------------------------------------------------------------SaveSenario
def SaveSenario():
   with open ("Senario_01.text", "w") as F:
      F.write(text.get(1.0,END))
      F.close()
Button(root,text="Save senario",command=SaveSenario).pack(anchor=W)
#------------------------------------------------------------------------------AddSenario          
def AddSenario ():
   with open("Senario_01.text") as S :
      Senario=S.read()
      ListBox.insert(END,Senario)
Button(root,text="Add senario",command=AddSenario).pack(anchor=W)
#------------------------------------------------------------------------------ExequteSenario       
def ExequteSenario ():
   with open("Senario1","r") as S :
      Senario=S.read()
      text.insert(INSERT,Senario)      
Button(root,text="Execute Senario",command=ExequteSenario).pack(anchor=W)
##                                                                                                              ##
##################################################################################################################

root.mainloop()
