from tkinter import *
from tkinter import Radiobutton


from PIL import ImageTk, Image
import mysql.connector
import random





def submit():
    con = mysql.connector.connect(host='localhost', port='3308', user='root', password='', db='hotel')
    c = con.cursor()
    name=E_Name.get()
    no=str(E_No.get())
    adds=str(E_Add.get())
    r_no=E_rno.get()
    if m.get() == 1:
        text = 1000
    elif m.get() == 2:
        text = 700
    else:
        text = 400
    if m.get() == 1:
        config="Delux"
    elif m.get() == 2:
        config="General"
    else:
        text = 400
        config="Budget"
    if r.get() ==1:
        run="AM"
    else:
        run="PM"
    check_inn=str(E_time.get())
    roomtype= config
    t_bill = int(r_no)*text

    ran_num= random.randrange(1,70,1)
    room_no=ran_num


    c.execute('insert into hotel_table values(%s,%s,%s,%s,%s,%s,%s,%s)',[room_no,name,no,adds,roomtype,r_no,check_inn,t_bill])
    con.commit()
    con.close()
    E_Name.delete(0, END)
    E_No.delete(0, END)
    E_Add.delete(0, END)
    E_rno.delete(0, END)

    note_text=(f"(Thank you so much for register {name} your checkout time is {check_inn} {run} after {str(r_no)} days)")
    Label(root,text=note_text,fg="red",bg='black',font=("TimesNewRoman", 10, "italic")).grid(row=20,column=7,pady=5)

    show_button= Button(root, text="Check", font=("TimesNewRoman", 17, "italic"),width=15,activeforeground="black",activebackground="green",command=display)
    show_button.grid(row=21,column=7,pady=12)
def display():
    win = Toplevel(root)
    win.geometry("1200x667")
    win.configure(bg="light blue")
    #Label(win,text="Check IN", fg="light blue",bg="green", font=("Courier", 19, "bold")).grid(row=0,column=6,padx=6)

    con = mysql.connector.connect(host='localhost', port='3308', user='root', password='', db='hotel')
    c = con.cursor()
    c.execute("select * from hotel_table")
    val = c.fetchall()
    rows = len(val)
    column = len(val[0])
    Label(win,text="Room NO",width=10, font=('arial',12,'bold')).grid(row=0,column=0,padx=10)
    Label(win, text="Name", width=10, font=('arial', 12, 'bold')).grid(row=0, column=1, padx=10)
    Label(win, text="Mobile No", width=10, font=('arial', 12, 'bold')).grid(row=0, column=2, padx=10)
    Label(win, text="Address", width=10, font=('arial', 12, 'bold')).grid(row=0, column=3, padx=10)
    Label(win, text="Room Type", width=10, font=('arial', 12, 'bold')).grid(row=0, column=4, padx=10)
    Label(win, text="No Of Days", width=10, font=('arial', 12, 'bold')).grid(row=0, column=5, padx=10)
    Label(win, text="CheckIn Time", width=10, font=('arial', 12, 'bold')).grid(row=0, column=6, padx=10)
    Label(win, text="Total Bill", width=10, font=('arial', 12, 'bold')).grid(row=0, column=7, padx=10)
    for i in range(rows):
        for j in range(column):
            e= Entry(win, bg="white", fg="green",width=20,borderwidth=2,highlightbackground="green",highlightthickness=2)
            e.grid(row=i+1,column=j)
            e.insert(END, val[i][j])



    con.commit()
    con.close()
    win.mainloop()



root = Tk()
root.title("Hotel Management System")
root.geometry("1000x667")
root.configure(bg='light blue')



L_main = Label(root, text="Check IN", fg="light blue", font=("Courier", 16, "bold"))
L_main.grid(row=2, column=0)
frame1= LabelFrame(root, width=400, height=70, background="light blue", highlightbackground="green",highlightthickness=3)
frame1.grid(row=5, column=7)
img = ImageTk.PhotoImage(Image.open("D:\Coding\Python\Test\Hotel management\Asset\pic1.jpg"))
frane_label= Label(root,text="🅶🆁🅰🅽🅳 🅷🅾🆃🅴🅻",font=(30))
frane_label.grid(row=5, column=7)

label = Label(frame1, image = img)
label.pack()






L_Name = Label(root, text="Name", fg="black",bg="light blue",borderwidth=4, font=("TimesNewRoman", 13, "italic"))
L_Name.grid(row=12, column=6)
E_Name = Entry(root, bg="white", fg="black",width=30,borderwidth=6)
E_Name.grid(row=12, column=7, padx=18,pady=20)

L_No = Label(root, text="Mobile NO", fg="black",bg="lightblue",borderwidth=4, font=("TimesNewRoman", 13, "italic"))
L_No.grid(row=13, column=6, padx=12)

E_No = Entry(root, bg="white",fg="black",width=30,borderwidth=6)
E_No.grid(row=13, column=7, padx=18, pady=3)

L_Add = Label(root, text="Address", fg="black",bg="light blue",borderwidth=4, font=("TimesNewRoman", 13, "italic"))
L_Add.grid(row=14, column=6, padx=12,pady=7)
E_Add = Entry(root, bg="white", fg="black",width=30,borderwidth=6)
E_Add.grid(row=14, column=7, padx=18,pady=10)


L_rno = Label(root,text="No Of Days", fg="black",bg="light blue", borderwidth=4,font=("TimesNewRoman", 13, "italic"))
L_rno.grid(row=15, column=6, padx=12,pady=7)

E_rno = Entry(root, bg="white", fg="black",width=30,borderwidth=6)
E_rno.grid(row=15, column=7, padx=18,pady=17)

L_time = Label(root,text="Checkin Time", fg="black",bg="light blue", borderwidth=4,font=("TimesNewRoman", 13, "italic"))
L_time.grid(row=16, column=6, padx=12,pady=7)


#E_time = Entry(root, bg="white", fg="black",width=30,borderwidth=6)

E_time = Spinbox(root, from_ = 1, to = 12)
E_time.grid(row=16, column=7, padx=18,pady=17)

r= IntVar()
r.set(1)
rb= Radiobutton(root, text="AM", fg="black", bg="light blue",font=("TimesNewRoman", 10, "italic"),variable=r, value=1,)
rb.grid(row=16, column=8,pady=5)
rb2 =Radiobutton(root, text="PM", fg="black",bg="light blue", font=("TimesNewRoman", 10, "italic"),variable=r, value=2,)
rb2.grid(row=16, column=9,pady=5,)


Lb = Label(root, text="Room Type", fg="black", bg="light blue",borderwidth=4,font=("TimesNewRoman", 13, "italic"))
Lb.grid(row=17, column=6)

m=IntVar()
m.set(1)




Cb= Radiobutton(root, text="Delux", fg="black", bg="light blue",font=("TimesNewRoman", 13, "italic"),variable=m, value=1,)
Cb.grid(row=17, column=7,pady=5)
Cb2 =Radiobutton(root, text="General", fg="black",bg="light blue", font=("TimesNewRoman", 13, "italic"),variable=m, value=2,)
Cb2.grid(row=17, column=8,pady=5,)
Cb3 = Radiobutton(root, text="Budget", fg="black",bg="light blue", font=("TimesNewRoman", 13, "italic"),variable=m, value=3,)
Cb3.grid(row=17, column=9,padx=100,pady=5)

Label(root,text="(1000₹ per day)",fg="red",bg='light blue',font=("TimesNewRoman", 10, "italic")).grid(row=18,column=7)
Label(root,text="(700₹ per day)",fg="red",bg='light blue',font=("TimesNewRoman", 10, "italic")).grid(row=18,column=8)
Label(root,text="(400₹ per day)",fg="red",bg='light blue',font=("TimesNewRoman", 10, "italic")).grid(row=18,column=9)



submit_btn=Button(root, text="Submit", font=("TimesNewRoman", 13, "italic"),activeforeground="white",activebackground="black",command=submit)
submit_btn.grid(row=19,column=7,pady=12)








root.mainloop()
