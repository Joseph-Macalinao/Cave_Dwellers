import mysql.connector


def updateStats(user_name, win_num, loss_num, xp_amount):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="CaveDweller"
    )
    mycursor = mydb.cursor()
    sql = "UPDATE stats SET wins = %s, losses = %s, xp = %s WHERE name = %s"
    val = (win_num, loss_num, xp_amount, user_name)
    mycursor.execute(sql, val)
    mydb.commit()
    return


def updateAchievements(user_name, l1, l2, l3, l4, l5):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="CaveDweller"
    )
    mycursor = mydb.cursor()
    sql = "UPDATE achievements SET lvl1 = %s, lvl2 = %s, lvl3 = %s, lvl4 = %s, lvl5 = %s WHERE name = %s"
    val = (l1, l2, l3, l4, l5, user_name)
    mycursor.execute(sql, val)
    mydb.commit()
    return


def updateInventory(user_name, heal_num, weapon_num, armor_num, shield_num, gold_num):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="CaveDweller"
    )
    mycursor = mydb.cursor()
    sql = "UPDATE inventory SET heal = %s, weapon = %s, armor = %s, shield = %s, gold = %s WHERE name = %s"
    val = (heal_num, weapon_num, armor_num, shield_num, gold_num, user_name)
    mycursor.execute(sql, val)
    mydb.commit()
    return
