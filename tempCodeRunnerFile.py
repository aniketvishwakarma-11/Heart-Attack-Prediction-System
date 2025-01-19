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




























