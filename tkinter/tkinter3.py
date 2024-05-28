import Tkinter as tk

root =tk.Tk()
root.title("welcom to PSS/E Asistant software")

root.geometry("1080x750")
root.resizable(width=False, height=False)


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
