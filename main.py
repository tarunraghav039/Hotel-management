from tkinter import *
from tkinter import Radiobutton


from PIL import ImageTk, Image
import mysql.connector

top = Tk()
top.geometry("1920x1080")
top.title("Grand Hotel Manager")
bg = PhotoImage(file="D:\Coding\Python\Test\Hotel management\Asset\mail_hotel.png")
label1 = Label(top, image=bg)
label1.place(x=0, y=0)

def customer_details():
    win = Toplevel(top)
    win.geometry("1200x667")
    win.configure(bg="black")
    # Label(win,text="Check IN", fg="Black",bg="green", font=("Courier", 19, "bold")).grid(row=0,column=6,padx=6)



    con = mysql.connector.connect(host='localhost', port='3308', user='root', password='', db='hotel')
    c = con.cursor()
    c.execute("select * from hotel_table")
    val = c.fetchall()
    rows = len(val)
    column = len(val[0])
    Label(win, text="Room NO", width=10, font=('arial', 12, 'bold')).grid(row=0, column=0, padx=10)
    Label(win, text="Name", width=10, font=('arial', 12, 'bold')).grid(row=0, column=1, padx=10)
    Label(win, text="Mobile No", width=10, font=('arial', 12, 'bold')).grid(row=0, column=2, padx=10)
    Label(win, text="Address", width=10, font=('arial', 12, 'bold')).grid(row=0, column=3, padx=10)
    Label(win, text="Room Type", width=10, font=('arial', 12, 'bold')).grid(row=0, column=4, padx=10)
    Label(win, text="No Of Days", width=10, font=('arial', 12, 'bold')).grid(row=0, column=5, padx=10)
    Label(win, text="CheckIn Time", width=10, font=('arial', 12, 'bold')).grid(row=0, column=6, padx=10)
    Label(win, text="Total Bill", width=10, font=('arial', 12, 'bold')).grid(row=0, column=7, padx=10)
    for i in range(rows):
        for j in range(column):
            e = Entry(win, bg="white", fg="green", width=20, borderwidth=2, highlightbackground="green",
                      highlightthickness=2)
            e.grid(row=i + 1, column=j)
            e.insert(END, val[i][j])

    con.commit()
    con.close()
    win.mainloop()


def checkout():
    win2 = Toplevel(top)
    win2.geometry("1200x667")
    win2.title("Checkout")
    bg2 = PhotoImage(file="D:\Coding\Python\Test\Hotel management\Asset\checkout.png")
    label2 = Label(win2, image=bg2)
    label2.place(x=0, y=0)

    def room_no():
        r_no= int(r_entry.get())
        con = mysql.connector.connect(host='localhost', port='3308', user='root', password='', db='hotel')
        c = con.cursor()

        c.execute("delete from hotel_table where roomid=%s ",[r_no])

        thank = Label(win2,text="Hope you enjoyed staying here Thank YOU for Visit again ",fg="red",bg="black",font=(9))
        thank.place(x=400,y=350)


        con.commit()
        con.close()



    r_no2 = Label(win2,text="Room NO: ",bg="black",width=8,height=1,fg="gold",font=(" sunny spells",16,"bold"),borderwidth=3)
    r_no2.place(x=330,y=263)
    r_entry= Entry(win2,bg="white", fg="green",width=40,borderwidth=2,highlightbackground="black",highlightthickness=9)
    r_entry.place(x=500,y=260)
    r_btn = Button(win2,text="OK",bg="black",width=8,fg="gold",font=(" sunny spells",16,"bold"),command=room_no)
    r_btn.place(x=825,y=260)
    win2.mainloop()

def info():
    top.destroy()
    root =Tk()
    root.geometry("1200x700")
    bg2 = PhotoImage(file="D:\Coding\Python\Test\Hotel management\Asset\Mhotel_main.png")
    label2 = Label(root, image=bg2)
    label2.place(x=0,y=0)


    LabelFrame(root, bg="black", width=700, height=150).place(x=280, y=20)
    Label(root, text="Grand hotel", bg="black", width=25, height=2, fg="gold",
                           font=(" sunny spells", 30, "bold"), borderwidth=3).place(x=330, y=40)
    Label(root,text=">Luxurious ambience, relaxing spa treatment, world class facilities and friendly hospitality make The Paul among the best hotels in Bangalore. ",font=("timesnewroman",9,"bold")).place(x=100, y=200)
    Label(root,text= ">It is situated in a picturesque setting without compromising on uniqueness and quality.",font=("timesnewroman",9,"bold")).place(x=100, y=250)
    Label(root,text=">The hotel is 4 miles from railway station and 28 miles from the international airport of Bangalore.",font=("timesnewroman",9,"bold") ).place(x=100, y=300)
    Label(root,text= ">During the stay, guests can take pleasure in oodles of activities like Fitness center, spa and swimming pool. Besides this, they can enjoy having different varieties of cuisines at the award-wining restaurants.",font=("timesnewroman",9,"bold")).place(x=100, y=350)
    root.mainloop()


# Show image using label


main_frame=LabelFrame(top,bg="black",width=700,height=150)
main_frame.place(x=600,y=20)
label_main=Label(top,text="Grand hotel",bg="black",width=25,height=2,fg="gold",font=(" sunny spells",30,"bold"),borderwidth=3)
label_main.place(x=650,y=40)

view_btn = Button(top,text="Customer Detail",bg="black",width=17,height=4,fg="gold",font=(" Rockwell",22,"bold"),borderwidth=3,command=customer_details)
view_btn.place(x=770,y=250)

Checkout_btn = Button(top,text="Checkout",bg="black",width=17,height=4,fg="gold",font=(" Rockwell",22,"bold"),borderwidth=3,command=checkout)
Checkout_btn.place(x=770,y=500)

Checkout_btn = Button(top,text="About Us",bg="black",width=17,height=4,fg="gold",font=(" Rockwell",22,"bold"),borderwidth=3,command=info)
Checkout_btn.place(x=770,y=750)

top.mainloop()
