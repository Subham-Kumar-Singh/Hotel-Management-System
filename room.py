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




if __name__ == '__main__':
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()

        
        