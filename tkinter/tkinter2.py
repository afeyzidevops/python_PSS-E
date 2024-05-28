import Tkinter as tk

root =tk.Tk()
root.title("welcom to PSS/E Asistant software")

root.geometry("1080x750")
root.resizable(width=False, height=False)


              ############## edit  text box and add List box  wijet to project##########
##################################################################################################################
####
text=tk.Text(root)
text.pack()

#Listbox_Label=Label(root,font=10,text="Senarios",bg= "blue",fg="white")
#Listbox_Label.pack(anchor=W)
ListBox=tk.Listbox(root,font=10)
ListBox.pack()
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
       text.insert(tk.INSERT,data)
tk.Button(root,text="Open",command=LoadSenario).pack()
#------------------------------------------------------------------------------SaveSenario
def SaveSenario():
   with open ("Senario_01.text", "w") as F:
      F.write(text.get(1.0,tk.END))
      F.close()
tk.Button(root,text="Save senario",command=SaveSenario).pack()
#------------------------------------------------------------------------------AddSenario          
def AddSenario ():
   with open("Senario_01.text") as S :
      Senario=S.read()
      ListBox.insert(tk.END,Senario)
tk.Button(root,text="Add senario",command=AddSenario).pack()
#------------------------------------------------------------------------------ExequteSenario       
def ExequteSenario ():
   with open("Senario1","r") as S :
      Senario=S.read()
      text.insert(tk.INSERT,Senario)      
tk.Button(root,text="Execute Senario",command=ExequteSenario).pack()
#------------------------------------------------------------------------------ExequteSenario       
def DeleteSenario ():
      ListBox.delete(tk.ANCHOR)
      #ListBox.delete(END,1)      
tk.Button(root,text="Delete Senario",command=DeleteSenario).pack()
##                                                                                                              ##
##################################################################################################################

root.mainloop()
