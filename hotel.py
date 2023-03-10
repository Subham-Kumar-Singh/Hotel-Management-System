from tkinter import *
# imported from pillow
from PIL import Image, ImageTk
from customer import Cus_Win
from room import Roombooking
from details import DetailRoom

class Home:
    # window name:-root
    # window title:-title
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1350x800+0+0")

        # ***********************FIRST IMAGE*****************************

        # r is used before the link to convert all the forwardlash to backlash
        img1 = Image.open(
            r"E:\Django files\Hotel Managment System\images\hotel.jpg")
        # Antialias converts the low level images to the high level images
        img1 = img1.resize((1350, 90), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Label is taken from the Tkinter module
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        # placing the image in the html page
        lblimg.place(x=0, y=0, width=1350, height=90)

        # ***************************LOGO**********************************
        # r is used before the link to convert all the forwardlash to backlash
        img2 = Image.open(
            r"E:\Django files\Hotel Managment System\images\logo.jpg")
        # Antialias converts the low level images to the high level images
        img2 = img2.resize((230, 90), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Label is taken from the Tkinter module
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        # placing the image in the html page
        lblimg.place(x=0, y=0, width=230, height=90)

        # ********************LABEL*********************************
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=(
            "times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=90, width=1350, height=50)

        # **************************MAIN FRAME*************************
        # This frame is pre-defined in the tkinter module
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        # Taken y==190 because we have taken the label y =140 and height=50
        main_frame.place(x=0, y=130, width=1350, height=620)

        # ***********************MENU*******************************
        lbl_menu = Label(main_frame, text="MENU", font=(
            "times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)
        
        # ***********************buttom Frame**************************
                # This frame is pre-defined in the tkinter module
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        # Taken y==190 because we have taken the label y =140 and height=50
        btn_frame.place(x=0, y=35, width=228, height=124)
        
        
        # in the cust_btn i have used command for the calling of the function that will get started after a click on it 
        cust_btn=Button(btn_frame,text='CUSTOMER',command=self.cust_details,width=22,font=(
            "times new roman", 15, "bold"), bg="black", fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame,text='ROOM',command=self.roombooking ,width=22,font=(
            "times new roman", 15, "bold"), bg="black", fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)
        
        room_details_btn=Button(btn_frame,text='DETAILS',command=self.AddroomDetails,width=22,font=(
            "times new roman", 15, "bold"), bg="black", fg="gold",bd=0,cursor="hand1")
        room_details_btn.grid(row=2,column=0,pady=1)
        
        
        # ******************************RIGHT SIDE IMAGE**************************
        img3 = Image.open(
            r"E:\Django files\Hotel Managment System\images\reception.jpg")
        # Antialias converts the low level images to the high level images
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Label is taken from the Tkinter module
        lblimg = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        # placing the image in the html page
        lblimg.place(x=225, y=0, width=1310, height=590)
        
        # ***********************DOWN IMAGES**********************************
        img4 = Image.open(
            r"E:\Django files\Hotel Managment System\images\reception.jpg")
        # Antialias converts the low level images to the high level images
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        # Label is taken from the Tkinter module
        lblimg = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        # placing the image in the html page
        lblimg.place(x=0, y=160, width=230, height=210)
        
        img5 = Image.open(
            r"E:\Django files\Hotel Managment System\images\reception.jpg")
        # Antialias converts the low level images to the high level images
        img5 = img5.resize((230,190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        # Label is taken from the Tkinter module
        lblimg = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        # placing the image in the html page
        lblimg.place(x=0, y=355, width=230, height=190)
        


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cus_Win(self.new_window)
    
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def AddroomDetails(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailRoom(self.new_window)



if __name__ == '__main__':
    root = Tk()
    obj = Home(root)
    root.mainloop()
