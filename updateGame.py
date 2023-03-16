import mysql.connector


def updateStats(user_name, win_num, loss_num, xp_amount):
    # Connect to DB
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="CaveDweller"
    )
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE stats SET wins = win_num, losses = loss_num, xp = xp_amount WHERE name = user_name")
    mydb.commit()
    return


def updateAchievements(user_name, l1, l2, l3, l4, l5):
    # Connect to DB
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="CaveDweller"
    )
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE achievements SET lvl1 = l1, lvl2 = l2, lvl3 = l3, lvl4 = l4, lvl5 = l5 "
                     "WHERE name = user_name")
    mydb.commit()
    return


def updateInventory(user_name, heal_num, weapon_num, armor_num, shield_num):
    # Connect to DB
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="CaveDweller"
    )
    mycursor = mydb.cursor()
    mycursor.execute("UPDATE inventory SET heal = heal_num, weapon = weapon_num, armor = armor_num, "
                     "shield = shield_num WHERE name = user_name")
    mydb.commit()
    return
