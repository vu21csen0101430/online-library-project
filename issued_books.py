from tkinter import *
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code
mypass = "cse1430"
mydatabase = "db"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "books"
issuedBooksTable = "issued_books"  # Table for issued books

def ViewIssuedBooks():
    # Function to view issued books

    root = Tk()  # Creating Tkinter window
    root.title("Library - Issued Books")  # Setting window title
    root.minsize(width=400, height=400)  # Setting minimum window size
    root.geometry("600x500")  # Setting initial window geometry

    # Creating a canvas for the window
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    # Creating a frame for the heading
    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    # Adding heading label
    headingLabel = Label(headingFrame1, text="Issued Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Creating a frame for displaying issued books
    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    # Adding labels for column headers
    Label(labelFrame, text="%-10s%-30s%-30s%-20s%-20s" % ('Issue ID', 'BID', 'Title', 'Student ID', 'Student Name'),
          bg='black', fg='white').place(relx=0.07, rely=0.1)

    # Adding separator line
    Label(labelFrame, text="----------------------------------------------------------------------------------",
          bg='black', fg='white').place(relx=0.05, rely=0.2)

    # SQL query to retrieve issued books along with book and student details
    getIssuedBooks = "SELECT issued_books.issue_id, books.bid, books.title, issued_books.student_id, students.name " \
                     "FROM issued_books INNER JOIN books ON issued_books.book_id = books.bid " \
                     "INNER JOIN students ON issued_books.student_id = students.student_id"

    try:
        cur.execute(getIssuedBooks)  # Executing the query
        con.commit()  # Committing the transaction

        # Iterating through the result set and displaying issued book details
        for i in cur:
            Label(labelFrame,
                  text="%-10s%-30s%-30s%-20s%-20s" % (i[0], i[1], i[2], i[3], i[4]),
                  bg='black', fg='white').place(relx=0.07, rely=y)
            y += 0.1  # Incrementing y-coordinate for next label
    except Exception as e:
        print(e)  # Printing error message
        messagebox.showinfo("Failed to fetch files from database")  # Displaying messagebox

    # Adding Quit button to close the window
    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()  # Running the Tkinter event loop

# Example usage:
ViewIssuedBooks()  # Calling the function to view issued books
