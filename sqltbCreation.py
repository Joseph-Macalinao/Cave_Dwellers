import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="cat911",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE users (name VARCHAR(255) PRIMARY KEY, class VARCHAR(255))")
#mycursor.execute("Show tables")

#for tb in mycursor:
    #print(tb)
