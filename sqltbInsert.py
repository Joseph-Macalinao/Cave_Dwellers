import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="cat911",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO users (name, class) VALUES (%s, %s)"
val = [
  ('JosephT', 'Wizard'),
  ('JosephM', 'Warrior'),
  ('CarsonH', 'Paladin'),
  #('Eric', 'Prof'),
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
