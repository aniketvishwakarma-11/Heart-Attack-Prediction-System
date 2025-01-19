from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
import os

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt


background="#f0ddd5"
framebg="#62a7ff"
framefg="#fefbfb"

root=Tk()
root.title("Heart Attack Prediction System")
root.geometry("1450x730+60+80")
root.resizable(False, False)
root.config(bg=background)




#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#icon1
image_icon=PhotoImage(file="Images/Icon.png")
root.iconphoto(False,image_icon)


##header section 2
logo=PhotoImage(file="Images/Header.png")
myimage=Label(image=logo,bg=background)
myimage.place(x=0,y=0)



## <<<<<< frame 3
Heading_entry=Frame(root,width=800,height=190,bg="#df2d4b")
Heading_entry.place(x=600,y=20)

Label(Heading_entry, text="Registration No.", font="arial 13",bg="#df2d4b", fg=framefg).place
Label(Heading_entry, text="Date", font="arial 13",bg="#df2d4b",fg=framefg).place(x=430,y=0)

Label(Heading_entry, text="Patient Name", font="arial 13",bg="#df2d4b",fg=framefg).place(x=30,y=90)
Label(Heading_entry, text="Birth Year", font="arial 13",bg="#df2d4b",fg=framefg).place(x=430,y=90)


Entry_image=PhotoImage(file="Images/Rectangle.png")
Entry_image2=PhotoImage(file="Images/Rectangle.png")
Label(Heading_entry, image=Entry_image,bg="#df2d4b").place(x=20,y=30)
Label(Heading_entry, image=Entry_image,bg="#df2d4b").place(x=430,y=30)

Label(Heading_entry, image=Entry_image2,bg="#df2d4b").place(x=20,y=120)
Label(Heading_entry, image=Entry_image2,bg="#df2d4b").place(x=430,y=120)

Registration=IntVar()
reg_entry= Entry(Heading_entry, textvariable=Registration, width=30, font="arial 15",bg="#0e5363", fg="white",bd=0)
reg_entry.place(x=30,y=45)

Date =StringVar()
today = date. today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(Heading_entry, textvariable=Date,width=15, font='arial 15',bg="#0e5363",fg="white",bd=0)
date_entry.place(x=500,y=45)
Date.set(d1)

Name=StringVar()
name_entry= Entry(Heading_entry, textvariable=Name,width=20, font="arial 20",bg="#ededed",fg="#222222",bd=0)
name_entry.place(x=30,y=130)

DOB=IntVar()
dob_entry= Entry(Heading_entry, textvariable=DOB,width=20, font="arial 20",bg="#ededed",fg="#222222",bd=0)
dob_entry.place(x=450,y=130)



#######################################################body hai ye sab code ko haath mat laga ##################################
Detail_entry=Frame(root,width=490,height=260,bg="#dbe0e3")
Detail_entry.place(x=30,y=450)


#########radio button ############ 5
Label(Detail_entry, text="sex:", font="arial 13",bg=framebg, fg=framefg).place(x=10,y=10)
Label(Detail_entry, text="fbs:", font="arial 13",bg=framebg, fg=framefg).place(x=180,y=10)
Label(Detail_entry, text="exang: ", font="arial 13",bg=framebg, fg=framefg).place(x=335,y=10)

def selection():
 if gen.get() == 1:
    Gender=1
    return(Gender)
    print(Gender)
 elif gen.get() == 2:
    Gender=0
    return(Gender)
    print(Gender)
 else:
    print(Gender)

def selection2():
 if fbs.get() == 1:
    Fbs=1
    return(Fbs)
    print(Fbs)
 elif fbs.get() == 2:
    Fbs=0
    return(Fbs)
    print(Fbs)
 else:
    print(Fbs)

def selection3():
 if exang.get() == 1:
    Exang=1
    return(Exang)
    print(Exang)
 elif exang.get() == 2:
    Exang=0
    return(Exang)
    print(Exang)
 else:
    print(Exang)

gen = IntVar()
R1 = Radiobutton(Detail_entry, text='Male', variable=gen, value=1,command=selection)
R2 = Radiobutton(Detail_entry, text="Female", variable=gen, value=2,command=selection)
R1.place(x=43,y=10)
R2.place(x=93,y=10)


fbs = IntVar()
R3 = Radiobutton(Detail_entry, text='True', variable=fbs, value=1,command=selection)
R4 = Radiobutton(Detail_entry, text="False",variable=fbs, value=2,command=selection)
R3.place(x=213,y=10)
R4.place(x=263,y=10)

exang = IntVar()
R5 = Radiobutton(Detail_entry, text='Yes', variable=exang, value=1,command=selection)
R6 = Radiobutton(Detail_entry, text="No", variable=exang, value=2,command=selection)
R5.place(x=387,y=10)
R6.place(x=430, y=10)






###########################################combo box###################################

Label(Detail_entry,text="cp:",font="arial 13",bg=framebg, fg=framefg).place(x=10,y=50)
Label(Detail_entry, text="restecg",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=90)
Label(Detail_entry, text="slope:", font="arial 13",bg=framebg, fg=framefg).place(x=10,y=130)
Label(Detail_entry, text="ca:", font="arial 13",bg=framebg, fg=framefg).place(x=10,y=170)
Label(Detail_entry, text="thal:",font="arial 13",bg=framebg, fg=framefg).place(x=10,y=210)


###
def selection4():
   input=cp_combobox.get()
   if input=="0=typical angina":
      return(0)
   elif input=="1=atypical angina":
      return(1)
   elif input=="2=non-anginal pain":
      return(2)
   elif input=="3=asymptomatic":
      return(3)
   else:
      print(Exang)


def selection5():
   input=slope_combobox.get()
   if input=="0=upsloping":
      return(0)
   elif input=="1=flat":
      return(1)
   elif input=="2=downsloping":
      return(2)
   else:
      print(Exang)

cp_combobox = Combobox(Detail_entry,value=['0=typical angina','1=atypical angina','2=non-anginal pain','3=asymptomatic'],font="arial 12",state ="r",width=11)
restecg_combobox = Combobox(Detail_entry,value=['0','1','2'],font="arial 12",state ="r",width=11)
slope_combobox= Combobox(Detail_entry,value=['0=upsloping','1=flat','2=downsloping'],font="arial 12",state ="r",width=11)
ca_combobox = Combobox(Detail_entry,value=['0','1','2','3','4'],font="arial 12",state ="r",width=11)
thal_combobox = Combobox(Detail_entry,value=['0','1','2','3'],font="arial 12",state ="r",width=11)

cp_combobox.place(x=50,y=50)
restecg_combobox.place(x=80,y=90)
slope_combobox.place(x=70,y=130)
ca_combobox.place(x=50,y=170)
thal_combobox.place(x=50, y=210)




######################Data Entry Box ####################################
Label(Detail_entry,text="Smoking",font="arial 13",width=7,bg="#dbe0e3",fg="black").place(x=240,y=50)
Label(Detail_entry,text="trestbps",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=50)
Label(Detail_entry,text="chol",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=50)
Label(Detail_entry,text="thelach",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=50)
Label(Detail_entry,text="cldpeak",font="arial 13",width=7,bg=framebg,fg=framefg).place(x=240,y=50)

trestbps=StringVar()
chol=StringVar()
thelach=StringVar()
oldpeak=StringVar()

trestbps_entry=Entry(Detail_entry,textvaraible=trestbps,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
chol_entry=Entry(Detail_entry,textvaraible=chol,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
thelach_entry=Entry(Detail_entry,textvaraible=thelach,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
oldpeak_entry=Entry(Detail_entry,textvaraible=oldpeak,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
trestbps_entry.place(x=320,y=90)
chol_entry.place(x=320,y=130)
thelach_entry.place(x=320,y=170)
oldpeak_entry.place(x=320,y=210)


#####################################################################################################################

############################################Report###################################################################

square_report_image=PhotoImage()
report_background= Label(images=square_report_image,bg=backgroung)
report_background.place(x=1120,y=340)

report=Label(root,font="arial 25 bold",bg="white",fg="#8dc63f")
report.place(x=1170,y=550)
report=Label(root,font="arial 10 bold",bg="white",fg="#8dc63f")
report.place(x=1130,y=610)


#########################################################################################################################
###############################################Graph#####################################################################

graph_image=PhotoImage()
Label(images=graph_image).place(x=600,y=270)
Label(images=graph_image).place(x=860,y=270)
Label(images=graph_image).place(x=600,y=500)
Label(images=graph_image).place(x=860,y=500)


###############################################Button######################################################################
analysis_button=PhotoImage(file="Images/Analysis.jpeg")
Button(root,images=analysis_button,bd=0,bg=background,cursor='hand').place(x=1130,y=240)




################################################Info Button################################################################

info_button=PhotoImage(file="Images/Info.jpeg")
Button(root,images=info_button,bd=0,bg=background,cursor='hand').place(x=10,y=240)


################################################Save Button################################################################

save_button=PhotoImage(file="Images/Save.jpeg")
Button(root,images=save_button,bd=0,bg=background,cursor='hand').place(x=1370,y=250)

################################################Smoker Button################################################################

button_mode=True
choice="Smoking"
def changemode():
   global button_mode
   global choice

   if button_mode:
      choice="non_smoking"
      mode.config(image=non_smoking_icon,activatebackgrounds="white")
      button_mode=False
   else:
      choice="smoking"
      mode.config(image=smoking_icon,activatebackgrounds="white")
      button_mode=True
   
   print(choice)

smoking_icon=PhotoImage(file="Images/Smoking.jpeg")
non_smoking_icon=PhotoImage(file="Images/Non-Smoking.jpeg")


mode=Button(root,image=smoking_icon,bg="#dbe0e3",bd=0,cursor="hand2")
mode.place(x=350,y=495)

############################################################################################################################

###########################################################Logout Button ####################################################

logout_icon=PhotoImage(file="Images/Logout.jpeg")
logout_button=Button(root,image=logout_icon,bg="#df2d4b",cursor="hand",bd=0)
logout_button.place(x=1390,y=60)
###########################################################################################################################


root.mainloop()