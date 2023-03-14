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

# Sql queries for:
# Stats (Replace with the correct following values)
user_name = ""
win_num = 0
loss_num = 0
xp_amount = 0
mycursor.execute("UPDATE stats SET wins = win_num, losses = loss_num, xp = xp_amount WHERE name = user_name")
mydb.commit()

# Achievements (Replace with the correct following values)
user_name = ""
l1 = 0
l2 = 0
l3 = 0
l4 = 0
l5 = 0
mycursor.execute("UPDATE achievements SET lvl1 = l1, lvl2 = l2, lvl3 = l3, lvl4 = l4, lvl5 = l5 WHERE name = user_name")
mydb.commit()

# Inventory
user_name = ""
heal_num = 0
weapon_num = 0
armor_num = 0
shield_num = 0
mycursor.execute("UPDATE inventory SET heal = heal_num, weapon = weapon_num, armor = armor_num, shield = shield_num "
                 "WHERE name = user_name")
mydb.commit()
