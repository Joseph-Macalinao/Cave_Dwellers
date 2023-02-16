import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  # Username of the db
  user="root",
  # Password of the db
  password="cat911",
)

mycursor = mydb.cursor()


def userCreation():
    if mydb:
        cmd = input("Continue or New")
        if cmd != "Continue" or "New":
            cmd = input("Please reenter Continue or New")
    else:
        cmd = input("Input new username")
        mycursor.execute("CREATE database CaveDweller")
        mycursor.execute("CREATE TABLE users (name VARCHAR(255) PRIMARY KEY, class VARCHAR(255))")
    if cmd == "Continue":
        # list the previous users and have them select
    elif cmd == "New":
        # create a new row in the table users
