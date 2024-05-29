import Tkinter as tk

root =tk.Tk()
root.title("welcom to PSS/E Asistant software")

root.geometry("1920x1080")
root.resizable(width=False, height=False)

Menu_Paned=tk.PanedWindow(root,bg="White",bd=4,orient="vertical")
Menu_Paned.pack(fill="both",expand=True)
Menu_Label=tk.Label(Menu_Paned,text="Menu bar")



slct_rgn_lbl=tk.Label(Menu_Paned,text="Please select a regional: ",font=("Titr",10))
slct_rgn_lbl.pack()
def Select_region():
   
   if   Ardabil_region_Rbtn.get()==1 and  Moghan_region_Rbtn.get()==0:
        region="Ardabil"
   elif Ardabil_region_Rbtn.get()==0 and  Moghan_region_Rbtn.get()==1:
        region="Moghan"
   elif Ardabil_region_Rbtn.get()==1 and  Moghan_region_Rbtn.get()==1:
        region="unknown"
   else :
        region="unknown"
   slct_rgn_lbl.config(text="selected regional is: {} ".format(region))
   
Rg_btn=tk.Button(Menu_Paned,text='select a regional',command=Select_region,font=('TITR',10),bg="red", fg="yellow",bd="5")
Rg_btn.pack()
Ardabil_region_Rbtn=tk.IntVar()
ch_01=tk.Checkbutton(Menu_Paned,text="Ardabil regional",variable=Ardabil_region_Rbtn)
ch_01.pack()
Moghan_region_Rbtn=tk.IntVar()
ch_02=tk.Checkbutton(Menu_Paned,text="Moghan regional",variable=Moghan_region_Rbtn)
ch_02.pack()


Menu_Paned.add(Menu_Label)
Menu_Paned.add(Rg_btn)
Menu_Paned.add(ch_01)
Menu_Paned.add(ch_02)
Menu_Paned.add(slct_rgn_lbl)



              ############## edit  text box and add List box  wijet to project##########
##################################################################################################################
####
Tapchanger=tk.Spinbox(root,from_=0,to_=19)
Tapchanger.pack()

def Get_Tapchanger():
   tap_step=Tapchanger.get()
   print tap_step

tk.Button(root,text="Get_Tapchanger",command=Get_Tapchanger).pack()
##                                                                                                              ##
##################################################################################################################

root.mainloop()
