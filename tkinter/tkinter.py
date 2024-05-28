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

                    ############## Change counter #######################
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


             ############## Insert Entry to project #######################
##################################################################################################################
##                                                                                                              ##
frame=Frame(root , width=100,height=50 , bd=5)
frame.pack()
open_sav_Label=Label(root,text="Please insert a *.sav file ",foreground="red",font=("Titr",10),background="Green")
open_sav_Label.place(x=10 , y=10, width=300,height=160)
open_sav_Label.pack()
Savfile=Entry(root)

Savfile.pack()
def open_sav():
  open_sav_Label.config(text=Savfile.get(),fg="green",bg="brown")
   

Button(root,text="open **.sav file",command=open_sav ,font=('TITR',10),bg="yellow", fg="blue",bd="5").pack()

##                                                                                                              ##
##################################################################################################################

                    ############## add Check Box to project #######################
##################################################################################################################
##                                                                                                              ##
select_region_label=Label(root,text="Please select a regional: ",font=("Titr",10))
select_region_label.pack(anchor=W)
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
   
Button(root,text='select a regional',command=Select_region,font=('TITR',10),bg="red", fg="yellow",bd="5").pack(anchor=W)
Ardabil_region_Rbtn=IntVar()
Checkbutton(root,text="Ardabil regional",variable=Ardabil_region_Rbtn).pack(anchor=W)
Moghan_region_Rbtn=IntVar()
Checkbutton(root,text="Moghan regional",variable=Moghan_region_Rbtn).pack(anchor=W)
##                                                                                                              ##
##################################################################################################################


                    ############### add radio buttom to select mode of opration in project #################
##################################################################################################################
##                                                                                                              ##
Mode=[("Power Flow","PF"),("Optimal Power Flow","OPF"),("Fault Analys","FA"),("Dynamic Simulation","DS")]
RB_var1=StringVar()
RB_var1.set("PF")
for text,mode in Mode :
   Radiobutton(root,text=text, variable=RB_var1, value=mode).pack(anchor=W)

#Radiobutton(root,text="Power Flow" ,variable=RB_var1).pack(anchor=E)

##                                                                                                              ##
##################################################################################################################

                ############### add Scale wijet in project #################
##################################################################################################################
##                                                                                                              ##

value_S_w1=Label(root,text="Active power: ",foreground="Green",font=("Titr",10),background="Black")
value_S_w1.pack(anchor=S)
MW_S_Entry=Entry(root)
MW_S_Entry.pack()
def get_value_S_w1():
   x=Scale_w1.get()
   value_S_w1.config(text="Active power: {} MW ".format(x))
   
   
Scale_w1=Scale(root,from_=0 ,to=1000,resolution=0.1)
Scale_w1.pack(anchor=S)
Scalb_w1_btn=Button(root,text="Get MW",command=get_value_S_w1)
Scalb_w1_btn.pack(anchor=S)

#------------------------------------------------

value_S_w2=Label(root,text="Reactive power: ",foreground="red",font=("Titr",10),background="Black")
value_S_w2.pack(anchor=S)
MVAR_S_Entry=Entry(root)
MVAR_S_Entry.pack()
def get_value_S_w2():
   x=Scale_w2.get()
   value_S_w2.config(text="Reactive power: {} MVAR ".format(x))
   
Scale_w2=Scale(root,from_=0 ,to=500,orient=HORIZONTAL,resolution=0.1)
Scale_w2.pack(anchor=S)
Scalb_w2_btn=Button(root,text="Get MVAR",command=get_value_S_w2)
Scalb_w2_btn.pack(anchor=S)
##                                                                                                              ##
##################################################################################################################



root.mainloop()
