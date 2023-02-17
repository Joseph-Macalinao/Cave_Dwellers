import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="CaveDweller"
)

mycursor = mydb.cursor()

sql = "UPDATE users SET class = 'berserk' WHERE name = 'JosephT'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")
