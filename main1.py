
from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from ViewBooks import *
from register import *
from viewregister import*


# Add your own database name and password here to reflect in the code
mypass = "cse1430"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=400,height=500)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=0.25

# Adding a background image
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((5013, 4634))
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)

Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = 5013, height = 5634)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Gitam Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    
btn1 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn1.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn2 = Button(root,text="Register",bg='black',fg='white',command=regBook)
btn2.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn7 = Button(root,text="View Register",bg='black', fg='white', command = Viewreg)
btn7.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)
    

root.mainloop()
