from Tkinter import *

root =Tk()
root.title("welcom to PSS/E Asistant software")

#root.minsize(300,400)
#root.maxsize(640,450)
root.geometry("900x750")
root.resizable(width=False, height=False)

Aras_Label=Label(root,text="Aras Simlink asistance",foreground="red",font=("Titr",20),background="Green")
Aras_Label.pack()
Aras_Label.config(fg="brown")

##################################################################################################################
##
Buttom_solve=Label(root,text="count: ")
Buttom_solve.pack()
counter=0
def Counter():
   global counter
   counter +=1
   #print counter
   Buttom_solve.config(text="count: %i"%counter)
   
Button(root,text="Solve",command=Counter ,font=('TITR',10),bg="yellow", fg="blue").pack()

##                                                                                                              ##
##################################################################################################################



##################################################################################################################
##                                                                                                              ##
frame=Frame(root , width=100,height=150 , bd=5)
frame.pack()
open_sav_Label=Label(root,text="Please insert a *.sav file ",foreground="red",font=("Titr",20),background="Green")
open_sav_Label.place(x=10 , y=10, width=300,height=160)
open_sav_Label.pack()
Savfile=Entry(root)

Savfile.pack()
def open_sav():
  open_sav_Label.config(text=Savfile.get(),fg="green",bg="brown")
   

Button(root,text="open **.sav file",command=open_sav ,font=('TITR',10),bg="yellow", fg="blue",bd="5").pack()

##                                                                                                              ##
##################################################################################################################


##################################################################################################################
##                                                                                                              ##
select_region_label=Label(root,text="Please select a regional: ",font=("Titr",20))
select_region_label.pack()
def Select_region():
   
   if   Ardabil_region_Rbtn.get()==1 and  Moghan_region_Rbtn.get()==0:
        region="Ardabil"
   elif Ardabil_region_Rbtn.get()==0 and  Moghan_region_Rbtn.get()==1:
        region="Moghan"
   elif Ardabil_region_Rbtn.get()==1 and  Moghan_region_Rbtn.get()==1:
        region="unknown"
   else :
        region="unknown"
   select_region_label.config(text="selected regional is: {} ".format(region))
   
Button(root,text='select a regional',command=Select_region,font=('TITR',10),bg="red", fg="yellow",bd="5").pack()
Ardabil_region_Rbtn=IntVar()
Checkbutton(root,text="Ardabil regional",variable=Ardabil_region_Rbtn).pack()
Moghan_region_Rbtn=IntVar()
Checkbutton(root,text="Moghan regional",variable=Moghan_region_Rbtn).pack()


root.mainloop()
