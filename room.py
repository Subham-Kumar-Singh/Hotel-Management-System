from tkinter import *
from PIL import Image, ImageTk

# this import is done to import the stylish input form
from tkinter import ttk,messagebox
import mysql.connector

import random

class Roombooking:
    # window name:-root
    # window title:-title
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")
        
        # *********************variables******************
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        
        
        
        # ********************title*********************************
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=(
            "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ***************************LOGO**********************************
        # r is used before the link to convert all the forwardlash to backlash
        img2 = Image.open(
            r"E:\Django files\Hotel Managment System\images\logo.jpg")
        # Antialias converts the low level images to the high level images
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Label is taken from the Tkinter module
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        # placing the image in the html page
        lblimg.place(x=5, y=2, width=100, height=40)

        # **************************LABEL FRAME************************
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details", font=(
            "times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)
        
        
        # **************************LABEL AND ENTRIES****************************
        # cust ref
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact ", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact, width=20,
                              font=("arial", 13, "bold"))
        entry_contact.grid(row=0, column=1,sticky=W)
        
        # Fetch Data Button
        btnFetchData = Button(labelframeleft,command=self.fetch_contact, text="Fetch Data", font=(
            "arial", 8, "bold"), bg="black", fg="gold", width=8)
        btnFetchData.place(x=347,y=4)
        
        # check-in Date
        check_in_date = Label(labelframeleft, text="Check_in Date: ", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft,textvariable=self.var_checkin, width=29,
                              font=("arial", 13, "bold"))
        txtcheck_in_date.grid(row=1, column=1)

        # check_out date
        check_out_date = Label(labelframeleft, text="Check_out Date: ", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)

        txtcheck_out_date = ttk.Entry(labelframeleft,textvariable=self.var_checkout, width=29,
                              font=("arial", 13, "bold"))
        txtcheck_out_date.grid(row=2, column=1)
        
        # Room Type
        label_RoomType = Label(labelframeleft, text="Room Type: ", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        combo_RoomType = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype, font=(
            "arial", 12, "bold"), width=27, state="readonly")
        combo_RoomType['value'] = ("TypeA", "TypeB", "TypeC")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)
        
        # Available Room
        lblRoomAvailable = Label(labelframeleft, text="Available Room: ", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

        txtRoomAvailable = ttk.Entry(labelframeleft,textvariable=self.var_roomavailable, width=29,
                              font=("arial", 13, "bold"))
        txtRoomAvailable.grid(row=4, column=1)
        
        # Meal
        lblMeal = Label(labelframeleft, text="Meal: ", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)

        txtMeal = ttk.Entry(labelframeleft,textvariable=self.var_meal, width=29,
                              font=("arial", 13, "bold"))
        txtMeal.grid(row=5, column=1)
        
        # No of days
        lblNoofDays = Label(labelframeleft, text="No of Days: ", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblNoofDays.grid(row=6, column=0, sticky=W)

        txtNoofDays = ttk.Entry(labelframeleft,textvariable=self.var_noofdays, width=29,
                              font=("arial", 13, "bold"))
        txtNoofDays.grid(row=6, column=1)
        
        # Paid Tax
        lblNoofDays = Label(labelframeleft, text="Paid Tax: ", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblNoofDays.grid(row=7, column=0, sticky=W)

        txtNoofDays = ttk.Entry(labelframeleft,textvariable=self.var_paidtax, width=29,
                              font=("arial", 13, "bold"))
        txtNoofDays.grid(row=7, column=1)
        
        # Sub Total
        lblnoofDays = Label(labelframeleft, text="Sub Total: ", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblnoofDays.grid(row=8, column=0, sticky=W)

        txtnoofDays = ttk.Entry(labelframeleft,textvariable=self.var_actualtotal, width=29,
                              font=("arial", 13, "bold"))
        txtnoofDays.grid(row=8, column=1)
        
        # Total Cost
        lblTotal = Label(labelframeleft, text="Total Cost: ", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblTotal.grid(row=9, column=0, sticky=W)

        txtTotal = ttk.Entry(labelframeleft,textvariable=self.var_total, width=29,
                              font=("arial", 13, "bold"))
        txtTotal.grid(row=9, column=1)
        
        
        # ********************Bill Buttons*************************
        btnBill = Button(labelframeleft,text="Add", font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1,sticky=W)

        
        # **************************btns****************************
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame,text="Add", font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)
        

        # *****************************table Frame Search System**************************
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=(
            "times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Table_Frame, text="Search by: ", font=(
            "arial", 12, "bold"), padx=2, pady=6, bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var=StringVar()
        combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=(
            "arial", 12, "bold"), width=24, state='readonly')
        combo_search["value"] = ("Mobile", "Room")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search=StringVar()
        txtSearch = ttk.Entry(Table_Frame,textvariable=self.txt_search ,width=24,
                              font=("arial", 13, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(Table_Frame, text="Show All", font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=2)
        
        
        # *****************************Show Data Table*************************
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        # This is to get the scroll bar in the x-axis and the y-axis
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, column=("contact", "checkinDate", "checkoutDate", "roomtype", "roomavailable", "meal",
                                                                    "noofdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # this is the way to pack our axis in the x-axis and the y-axis
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        #
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # this is done to show the user what does ref stands for "Refer No"
        self.room_table.heading("contact", text="contact")
        self.room_table.heading("checkinDate", text="check-in")
        self.room_table.heading("checkoutDate", text="check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="NoOfDays")

        # this is used to show all the headings of our table
        self.room_table["show"] = "headings"

        
        # this is used to reduce the width of the spaces between the tables
        self.room_table.column("contact", width=100)
        self.room_table.column("checkinDate", width=100)
        self.room_table.column("checkoutDate", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=100)

        # now we are packing our table
        self.room_table.pack(fill=BOTH, expand=1)
        
    # **********************ALL Data Fetch**************************************
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1511",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","This number not in the Database",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)
                
                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)
                
                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
                
                #************************Gender***********************************
                conn=mysql.connector.connect(host="localhost",username="root",password="1511",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)
                
                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)
                
                # *************************email**************************
                conn=mysql.connector.connect(host="localhost",username="root",password="1511",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblGender=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=60)
                
                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                
                # *************************Nationality***********************
                conn=mysql.connector.connect(host="localhost",username="root",password="1511",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblGender=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=90)
                
                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=90)
                
                # **************************Address*************************
                conn=mysql.connector.connect(host="localhost",username="root",password="1511",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblGender=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=120)
                
                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=120)
        


if __name__ == '__main__':
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()

        
        