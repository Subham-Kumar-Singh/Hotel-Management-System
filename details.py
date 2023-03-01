from tkinter import *
from PIL import Image, ImageTk

# this import is done to import the stylish input form
from tkinter import ttk,messagebox
import mysql.connector
import random

from time import strftime
from datetime import datetime

class DetailRoom:
    # window name:-root
    # window title:-title
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")
        
        
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
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=(
            "times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)
        
        # Floor
        lbl_floor = Label(labelframeleft, text="Floor ", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W,padx=20)

        self.var_floor=StringVar()
        entry_floor = ttk.Entry(labelframeleft,textvariable=self.var_floor ,width=20,
                              font=("arial", 13, "bold"))
        entry_floor.grid(row=0, column=1,sticky=W)
        
        # Room No
        lbl_RoomNo = Label(labelframeleft, text="Room No ", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W,padx=20)

        self.var_roomNo=StringVar()
        entry_RoomNo = ttk.Entry(labelframeleft,textvariable=self.var_roomNo, width=20,
                              font=("arial", 13, "bold"))
        entry_RoomNo.grid(row=1, column=1,sticky=W)
        
        # Room Type
        lbl_RoomType = Label(labelframeleft, text="Room Type ", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W,padx=20)

        self.var_RoomType=StringVar()            
        entry_RoomType = ttk.Entry(labelframeleft,textvariable=self.var_RoomType, width=20,
                              font=("arial", 13, "bold"))
        entry_RoomType.grid(row=2, column=1,sticky=W)
        
        # **************************btns****************************
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnAdd = Button(btn_frame,command=self.add_data, text="Add",font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame,command=self.update, text="Update",font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.mDelete, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)
        
        
        # *****************************table Frame Search System**************************
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=(
            "times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=600, y=55, width=600, height=350)
        
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(Table_Frame, column=("floor", "roomno", "roomType"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        # this is the way to pack our axis in the x-axis and the y-axis
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        #
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        # this is done to show the user what does ref stands for "Refer No"
        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomType", text="Room type")

        # this is used to show all the headings of our table
        self.room_table["show"] = "headings"

        
        # this is used to reduce the width of the spaces between the tables
        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomType", width=100)

        # now we are packing our table
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
    # ************************Add Data*********************************
    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1511",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                            self.var_floor.get(),
                                                                            self.var_roomNo.get(),
                                                                            self.var_RoomType.get(),
                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong: {str(es)}",parent=self.root)
        
        
    # *************************Ftech Data******************************
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1511",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert('',END,values=i)
            conn.commit()
        conn.close() 


    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]
        
        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_RoomType.set(row[2])
    
    # *****************************Update***************************
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please Enter Floor Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="1511",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                self.var_floor.get(),
                                                                                self.var_RoomType.get(),
                                                                                self.var_roomNo.get()
                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "New Room details has been Updated successfully",parent=self.root)
    
    # ***************************Delete*********************************
    def mDelete(self):
        mdelete=messagebox.askyesno("Hotel Management Systen","Do you want to delete this Room",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="1511",database="management")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")
        






if __name__ == '__main__':
    root = Tk()
    obj = DetailRoom(root)
    root.mainloop()