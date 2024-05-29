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
          
tk.Button(root,text="Delete Senario",command=DeleteSenario).pack()
##                                                                                                              ##
##################################################################################################################


              ############## add top level window by insert text box and scroll bar in it ##########
##################################################################################################################
####

def topLevel_1():
   
   top1=tk.Toplevel()
   top1.geometry("800x900")
   top1.title("Senario")
   label_1=tk.Label(top1,text="Senario_01") 
   text_1=tk.Text(top1,bg="Yellow")
   Scrollbar=tk.Scrollbar(top1)
   Scrollbar.config(command=text_1.yview)
   Scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)
   #for line in range(200):
    #  text_1.insert(tk.INSERT,"this is a text   " + str(line) + "\n")
#------------------------------------------------------------------------------OpenSenario
   def Open_senario():
      with open("Senario_01.text", "r") as F :
         data=F.read()    
         text_1.insert(tk.INSERT,data)
   Open_Senario=tk.Button(top1,text="Open Senario",command=Open_senario)
#------------------------------------------------------------------------------SaveSenario
   def SaveSenario():
      with open ("Senario_01.text", "w") as F:
         F.write(text_1.get(1.0,tk.END))
         F.close()
   Save_btn=tk.Button(top1,text="Save senario",command=SaveSenario)

   
   Close_btn=tk.Button(top1,text="Close",command= top1.destroy)
   
   label_1.pack
   text_1.pack(expand=True,fill=tk.BOTH)
   Open_Senario.pack()
   Save_btn.pack()
   Close_btn.pack()
   

   
   top1.mainloop()
   
#------------------------------------------------------------------------------LoadSenario

tk.Button(root,text="Load Senario",command=topLevel_1).pack()   





##                                                                                                              ##
##################################################################################################################


root.mainloop()
