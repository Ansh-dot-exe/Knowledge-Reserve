import mysql.connector

db = mysql.connector.connect(
    host="brbjmpkm2lgsjfy1lfhx-mysql.services.clever-cloud.com",
    user="ukc8u9srhpdpi6qv",
    passwd="VPG7dB5QxCWQvMyUaWIw",
    database="brbjmpkm2lgsjfy1lfhx"
)

mycursor = db.cursor()


#mycursor.execute("CREATE TABLE booksavailable (userid INTEGER(10), bookslot1 INTEGER(10), bookslot2 INTEGER(10), bookslot3 INTEGER(10), FOREIGN KEY (userid) REFERENCES accounts(userid), FOREIGN KEY (bookslot1) REFERENCES books(bookid), FOREIGN KEY (bookslot2) REFERENCES books(bookid), FOREIGN KEY (bookslot3) REFERENCES books(bookid))")
#mycursor.execute("CREATE TABLE books (bookid INT NOT NULL AUTO_INCREMENT, bookname VARCHAR(255), authorname VARCHAR(255), publishername VARCHAR(255), PRIMARY KEY(bookid))")
#mycursor.execute("CREATE TABLE accounts (userid INT NOT NULL AUTO_INCREMENT, email VARCHAR(255), password VARCHAR(255), username VARCHAR (255), PRIMARY KEY(userid))")
mycursor.execute("DELETE FROM accounts")
#mycursor.execute("INSERT INTO accounts(email, password, username) VALUES ('test@gmail.com', 'iwillnevergethacked', 'test')")
#mycursor.execute("SELECT email FROM accounts")
#myresult = mycursor.fetchall()

#mycursor.execute("SELECT email FROM accounts")


#result = mycursor.fetchall()
#if ('Email',) in result:
 #  print("exists")
   
#print('Email',)
#print(result)

db.commit()