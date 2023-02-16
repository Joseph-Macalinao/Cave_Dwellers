import mysql.connector
from character_create import createCharacter

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="cat911",
  database="CaveDweller"
)

mycursor = mydb.cursor()


def userCreation():
    if mydb:
        cmd = input("Continue or New")
        if cmd != "Continue" or "New":
            cmd = input("Please reenter Continue or New")
    else:
        mycursor.execute("CREATE database CaveDweller")
        mycursor.execute("CREATE TABLE users (name VARCHAR(255) PRIMARY KEY, class VARCHAR(255))")
        print("Welcome new player")
        user_name = input("Input new username")
        character = createCharacter()
        sql = "INSERT INTO users (name, class) VALUES (%s, %s)"
        val = [(user_name, character.name)]
        mycursor.executemany(sql, val)
        mydb.commit()
    if cmd == "Continue":
        mycursor.execute("SELECT users.name FROM users")
        mydb.commit()
        print(mycursor.rowcount, "was inserted.")
        user_name = input("Input existing username")
    elif cmd == "New":
        user_name = input("Input new username")
        character = createCharacter()
        sql = "INSERT INTO users (name, class) VALUES (%s, %s)"
        val = [(user_name, character.name)]
        mycursor.executemany(sql, val)
        mydb.commit()


userCreation()
