from tkinter import*
root=Tk()
root.geometry("800x500")
root.title("Bill Management System")
root.resizable(True,True)

def Reset():
    entry_Tea.delete(0,END)
    entry_Coffee.delete(0,END)
    entry_Cookies.delete(0,END)
    entry_Pastry.delete(0,END)
    entry_Bread.delete(0,END)
    entry_Lemonade.delete(0,END)

def Total():
    try:a1=int(Tea.get())
    except:a1=0

    try:a2=int(Coffee.get())
    except:a2=0

    try:a3=int(Cookies.get())
    except:a3=0

    try:a4=int(Pastry.get())
    except:a4=0

    try:a5=int(Bread.get())
    except:a5=0

    try:a6=int(Lemonade.get())
    except:a6=0

# define cost of each item per quantity
    c1=20*a1
    c2=30*a2
    c3=60*a3
    c4=50*a4
    c5=60*a5
    c6=20*a6

    lbl_total=Label(f2,font=("calibri",20,"bold"),text="Total",width=16,fg="lightblue",bg="silver")
    lbl_total.place(x=0,y=50)

    entry_total=Entry(f2,font=("calibri",20,"bold"),textvariable=Total_bill,bd=6,width=15,bg="lightblue")
    entry_total.place(x=5,y=50)

    totalcost=c1+c2+c3+c4+c5+c6
    string_bill="Rs.",str('%.2f' %totalcost)
    Total_bill.set(string_bill)
    
Label(text="Bill Management",bg="black",fg="white",font=("calibri",40),width="200",height="2").pack()
#MENU CARD
f=Frame(root,bg="silver",height=300,width=240)
f.place(x=5,y=135)

Label(f,text="Menu",font=("calibri",30,"bold"),fg="white",bg="black").place(x=80,y=0)
Label(f,font=("calibri",15,"bold"),text="Tea.............Rs.20/Cup",fg="black",bg="silver").place(x=5,y=80)
Label(f,font=("calibri",15,"bold"),text="Coffee........Rs.30/Cup",fg="black",bg="silver").place(x=5,y=110)
Label(f,font=("calibri",15,"bold"),text="Cookies......Rs.60/Pack",fg="black",bg="silver").place(x=5,y=140)
Label(f,font=("calibri",15,"bold"),text="Pastry.........Rs.50/Piece",fg="black",bg="silver").place(x=5,y=170)
Label(f,font=("calibri",15,"bold"),text="Bread..........Rs.60/Pack",fg="black",bg="silver").place(x=5,y=200)
Label(f,font=("calibri",15,"bold"),text="Lemonade...Rs.20/Glass",fg="black",bg="silver").place(x=5,y=230)

#Bill
f2=Frame(root,bg="lightgrey",highlightbackground="black",highlightthickness=1,height=310,width=240)
f2.place(x=550,y=140)

Bill=Label(f2,text="Bill",font=("calibri",25),bg="black",fg="white")
Bill.place(x=92,y=2)








#ENTRY SECTION
f1=Frame(root,bg="lightgrey",height=300,width=260,relief=RAISED)
f1.place(x=200,y=740)
f1.pack()

Tea=StringVar()
Coffee=StringVar()
Cookies=StringVar()
Pastry=StringVar()
Bread=StringVar()
Lemonade=StringVar()
Total_bill=StringVar()

#Label
lbl_Tea=Label(f1,font=("calibri",20,"bold"),text="(Qty) Tea",width=12,fg="blue")
lbl_Coffee=Label(f1,font=("calibri",20,"bold"),text=" Coffee",width=12,fg="blue")
lbl_Cookies=Label(f1,font=("calibri",20,"bold"),text=" Cookies",width=12,fg="blue")
lbl_Pastry=Label(f1,font=("calibri",20,"bold"),text=" Pastry",width=12,fg="blue")
lbl_Bread=Label(f1,font=("calibri",20,"bold"),text=" Bread",width=12,fg="blue")
lbl_Lemonade=Label(f1,font=("calibri",20,"bold"),text=" Lemonade",width=12,fg="blue")
lbl_Tea.grid(row=1,column=0)
lbl_Coffee.grid(row=2,column=0)
lbl_Cookies.grid(row=3,column=0)
lbl_Pastry.grid(row=4,column=0)
lbl_Bread.grid(row=5,column=0)
lbl_Lemonade.grid(row=6,column=0)

#Entry
entry_Tea=Entry(f1,font=("calibri",20,"bold"),textvariable=Tea,bd=5,width=8,bg="white")
entry_Coffee=Entry(f1,font=("calibri",20,"bold"),textvariable=Coffee,bd=5,width=8,bg="white")
entry_Cookies=Entry(f1,font=("calibri",20,"bold"),textvariable=Cookies,bd=5,width=8,bg="white")
entry_Pastry=Entry(f1,font=("calibri",20,"bold"),textvariable=Pastry,bd=5,width=8,bg="white")
entry_Bread=Entry(f1,font=("calibri",20,"bold"),textvariable=Bread,bd=5,width=8,bg="white")
entry_Lemonade=Entry(f1,font=("calibri",20,"bold"),textvariable=Lemonade,bd=5,width=8,bg="white")
entry_Tea.grid(row=1,column=1)
entry_Coffee.grid(row=2,column=1)
entry_Cookies.grid(row=3,column=1)
entry_Pastry.grid(row=4,column=1)
entry_Bread.grid(row=5,column=1)
entry_Lemonade.grid(row=6,column=1)

#Buttons

btn_reset=Button(f1,fg="black",bg="lightblue",font=("calibri",16,"bold"),width=10,text="RESET",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total=Button(f1,fg="black",bg="lightblue",font=("calibri",16,"bold"),width=10,text="TOTAL",command=Total)
btn_total.grid(row=8,column=1)







root.mainloop()
