import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="cat911",
)

mycursor = mydb.cursor()

#mycursor.execute("Create database mydatabase")
mycursor.execute("Show databases")

for db in mycursor:
  print(db)
