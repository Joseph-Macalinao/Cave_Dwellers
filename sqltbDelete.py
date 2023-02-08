import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="cat911",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM users WHERE name = 'Eric'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")