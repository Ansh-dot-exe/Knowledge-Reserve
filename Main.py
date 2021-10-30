from tkinter import *
from tkinter import ttk
import mysql.connector

root = Tk()

#======================================================initiate
root.geometry("1280x720")
root.title("Knowledge reserve")
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)

#============================================================Connect to database
db = mysql.connector.connect(
    host="brbjmpkm2lgsjfy1lfhx-mysql.services.clever-cloud.com",
    user="ukc8u9srhpdpi6qv",
    passwd="VPG7dB5QxCWQvMyUaWIw",
    database="brbjmpkm2lgsjfy1lfhx"
)
mycursor = db.cursor()
      

#===================================================Functions
def login(frame):
    username = Email_entry.get()
    password = Password_entry.get()
    mycursor.execute("Select password, username FROM accounts WHERE username = %s", (username,))
    result = mycursor.fetchall()
    if (password,username) in result:
        frame.tkraise()
    else:
        invalid = Label(frame1, text="The credentials are invalid", font=("Roboto", 16), fg = "Red", bg ="#FE9959")
        invalid.place(x = 510, y = 620)


def sign_up(frame):
    email = (Email_entryS.get())
    username = UN_textS.get()
    password = Password_entryS.get()
    entry = (email, password, username)
    mycursor.execute("SELECT username FROM accounts")
    SQLformula = "INSERT INTO accounts (email, password, username) VALUES (%s, %s, %s)"
    result = mycursor.fetchall()
    if (username,) in result:
        print("This username already exists")
        alrexists = Label(frame2, text="This username already exists", font=("Roboto", 16), fg = "Red", bg ="#FE9959")
        alrexists.place(x = 490, y = 650)
    else: 
        mycursor.execute(SQLformula,entry)
        frame.tkraise()
        db.commit()
    

def show_frame(frame):
    frame.tkraise()

def reset_text(frame,e, text):
    frame.tkraise()
    e.delete(0,END)
    e.insert(0,text)
    return


def book_result(bookname):
    bookframe = Frame(frame5, bg="#E6E6EA", width="470", height="240")
    bookframe.place(x = 705, y = 100, width=470, height=240)
    ba = Label(bookframe, text="Availability: yes", font=("roboto", 18, "bold"), bg="#E6E6EA")
    sn = Label(bookframe, text="Seller name: Mukesh Ambani", font=("roboto", 18, "bold"), bg="#E6E6EA")
    bn = Label(bookframe, text = "Book name: " + bookname, font=("roboto", 18, "bold"), bg="#E6E6EA")
    contact_button = Button(bookframe, text="Contact", font=("Roboto", 15, "bold"), bg ="#2AB7CA", fg="White", borderwidth=0)
    ba.place(x=140, y = 60)
    bn.place(x=55, y = 10)
    sn.place(x=65, y = 110)
    contact_button.place(x=150, y=170, width=160, height=50)

#=========================================Frames
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)
frame5 = Frame(root)


#display
for frame in (frame1, frame2, frame3, frame4, frame5):
    frame.grid(row = 0 , column = 0, sticky = "nsew")

#=======================================================Login page code

lgbg = PhotoImage(file = "Login_BG.png")
sign_in_pagepic = PhotoImage(file = "Sign_pg.png")
Login_bg = Label(frame1, image = lgbg)
Login_bg.place(x = -2,y = -2)

Email_text = StringVar()
Email_text.set("Username")
Email_entry = Entry(frame1, textvariable = Email_text, font=("Roboto", 16), fg = "white", bg = "#F4A08E", justify='center', borderwidth=0)
Email_entry.place(x = 450, y = 350, width = 390, height = 50)

Password_text = StringVar()
Password_text.set("Password")
Password_entry = Entry(frame1,textvariable = Password_text, font=("Roboto", 16), fg = "white", bg = "#F4A08E", justify='center', borderwidth=0)
Password_entry.place(x = 450, y = 420, width = 390, height = 50)

Login_bt = Button(frame1, text="Login", font=("Roboto", 15, "bold"), bg ="#2AB7CA", fg="White", borderwidth=0, command=lambda:[login(frame3)])
Login_bt.place(x = 560, y = 500, width=160, height=50)

Signin_pagebt = Button(frame1, image=sign_in_pagepic, borderwidth=0, highlightthickness = 0, bd = 0, activebackground="#FE8D56", command=lambda:[reset_text(frame2,Email_entry, "Username"), reset_text(frame2,Password_entry, "Password")])
Signin_pagebt.place(x = 710, y = 580)


#=======================================================Sign_up page code
spbg = PhotoImage(file = "Sign_BG.png")
login_in_pagepic = PhotoImage(file = "Login_pg.png")
SignUp_bg = Label(frame2, image = spbg)
SignUp_bg.place(x = -2,y = -2)

Email_textS = StringVar()
Email_textS.set("Email")
Email_entryS = Entry(frame2, textvariable = Email_textS, font=("Roboto", 16), fg = "white", bg = "#F4A08E", justify='center', borderwidth=0)
Email_entryS.place(x = 450, y = 396, width = 390, height = 50)

Password_textS = StringVar()
Password_textS.set("Password")
Password_entryS = Entry(frame2,textvariable = Password_textS, font=("Roboto", 16), fg = "white", bg = "#F4A08E", justify='center', borderwidth=0)
Password_entryS.place(x = 450, y = 475, width = 390, height = 50)

UN_textS = StringVar()
UN_textS.set("Username")
Un_entryS = Entry(frame2,textvariable = UN_textS, font=("Roboto", 16), fg = "white", bg = "#F4A08E", justify='center', borderwidth=0)
Un_entryS.place(x = 450, y = 322, width = 390, height = 50)

SignIn_bt = Button(frame2, text="Create", font=("Roboto", 15, "bold"), bg ="#2AB7CA", fg="White", borderwidth=0, command=lambda:sign_up(frame3))
SignIn_bt.place(x = 560, y = 550, width=160, height=50)

Login_pagebt = Button(frame2, image=login_in_pagepic, borderwidth=0, highlightthickness = 0, bd = 0, activebackground="#FE8D56", command=lambda:[reset_text(frame1,Email_entryS, "Email"), reset_text(frame1,Password_entryS, "Password"), reset_text(frame1,Un_entryS, "Username")])
Login_pagebt.place(x = 715, y = 624)

#=======================================================Selection page code
slbg = PhotoImage(file = "Selection_BG.png")
Lg_Bk = PhotoImage(file = "Bk_Login.png")
selection_bg = Label(frame3, image = slbg)
selection_bg.place(x = -2,y = -2)

Select1_bt = Button(frame3, text="Select", font=("Roboto", 15), bg ="#2AB7CA", fg="White", borderwidth=0, command=lambda:show_frame(frame5))
Select1_bt.place(x = 830, y = 425, width=160, height=50)

Select2_bt = Button(frame3, text="Select", font=("Roboto", 15), bg ="#2AB7CA", fg="White", borderwidth=0, command=lambda:show_frame(frame4))
Select2_bt.place(x = 280, y = 425, width=160, height=50)

Login_Backbt = Button(frame3, image=Lg_Bk, borderwidth=0, highlightthickness = 0, bd = 0, activebackground="#FE8D56", command=lambda:[reset_text(frame1,Email_entry, "Username"), reset_text(frame1, Password_entry, "Password")])
Login_Backbt.place(x = 10, y = 690)

#=======================================================Book exchange page code
bebg = PhotoImage(file = "Exchange_BG.png")
bts = PhotoImage(file = "BTS_Btt.png")
exchange_bg = Label(frame4, image = bebg)
exchange_bg.place(x = -2,y = -2)

style = ttk.Style()
style.theme_use('classic')
style.configure("TCombobox", fieldbackground = "#2AB7CA", background = "#2AB7CA", arrowcolor="#2AB7CA")
  
n = StringVar()
m = StringVar()
o = StringVar()

dp1 = ttk.Combobox(frame4, width = 17, textvariable=n, font=("Roboto", 15), foreground="white")
dp2 = ttk.Combobox(frame4, width = 17, textvariable = m, font=("Roboto", 15), foreground="white")
dp3 = ttk.Combobox(frame4, width = 17, textvariable = o, font=("Roboto", 15), foreground="white")

dp1['values'] = ('Holts sience textbook', 'Macbeth', 'Oxford Maths book', 'Haese maths book', 'I&S text book')
dp2['values'] = ('Holts sience textbook', 'Macbeth', 'Oxford Maths book', 'Haese maths book', 'I&S text book')
dp3['values'] = ('Holts sience textbook', 'Macbeth', 'Oxford Maths book', 'Haese maths book', 'I&S text book')

dp1.place(x = 132, y = 360, width=200, height=50)
dp2.place(x = 537, y = 360, width=200, height=50)
dp3.place(x = 952, y = 360, width=200, height=50)

AvaBtt = Button(frame4, text="Update account", font=("Roboto", 14, "bold"), bg ="#2AB7CA", fg="White", borderwidth=0)
AvaBtt.place(x = 537, y = 540, width=200, height=50)

bts_btt1 = Button(frame4, image=bts, borderwidth=0, highlightthickness = 0, bd = 0, activebackground="#FE8D56", command=lambda:show_frame(frame3))
bts_btt1.place(x = 10, y = 680)

#===================================================Book Search Screen
sebg = PhotoImage(file = "Search_BG.png")
search_bg = Label(frame5, image = sebg)
search_bg.place(x = -2,y = -2)

s = StringVar()
s.set('Search...')
Search_Bar = ttk.Combobox(frame5, textvariable=s, font=("Roboto", 16), foreground="White")
Search_Bar.place(x = 30, y = 250, width= 475, height=43)

Search_Bar['values'] = ('Holts sience textbook', 'Macbeth', 'Oxford Maths book', 'Haese maths book', 'I&S text book')

book_result("Oxford Maths book")

bts_btt2 = Button(frame5, image=bts, borderwidth=0, highlightthickness = 0, bd = 0, activebackground="#FE8D56", command=lambda:show_frame(frame3))
bts_btt2.place(x = 10, y = 680)



#===========================================END
show_frame(frame1)
root.resizable(False, False)
root.mainloop()

