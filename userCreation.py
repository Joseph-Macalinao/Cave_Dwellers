import mysql.connector
from character_create import createCharacter

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="cat911"
)
myCursor = mydb.cursor()


def userCreation():

    if mydb:
        # Checks to see if database exists
        cmd = str(input("New, Returning, or Create new user:\n"))
    else:
        # Game requires prior setup of MySQL local host with the following info above
        print("Please setup MySQL database before running")
        return

    if cmd == "New":
        # Creates new database and new user
        myCursor.execute("CREATE database CaveDweller")
        # Setups use of existing database
        existing_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="cat911",
            database="CaveDweller"
        )
        new_cursor = existing_db.cursor()
        new_cursor.execute("CREATE TABLE users (name VARCHAR(255) PRIMARY KEY, class VARCHAR(255))")
        print("*** Welcome new player ***")
        user_name = str(input("Input new username:\n"))
        character = createCharacter()
        sql = "INSERT INTO users (name, class) VALUES (%s, %s)"
        val = (user_name, character.arch)
        new_cursor.execute(sql, val)
        existing_db.commit()

    # Setups use of existing database
    existing_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="cat911",
        database="CaveDweller"
    )
    new_cursor = existing_db.cursor()

    if cmd == "Returning":
        # Lists the existing users
        new_cursor.execute("SELECT users.name FROM users")
        myResult = new_cursor.fetchall()
        for x in myResult:
            print(x)
        user_name = str(input("Input existing username:\n"))

    if cmd == "Create":
        # Creates a new user
        user_name = str(input("Input new username:\n"))
        character = createCharacter()
        sql = "INSERT INTO users (name, class) VALUES (%s, %s)"
        val = [(user_name, character.arch)]
        new_cursor.executemany(sql, val)
        existing_db.commit()

    sql = "SELECT * FROM users WHERE users.name = %s"
    new_cursor.execute(sql, (user_name,))
    res = new_cursor.fetchall()
    return res


print(userCreation())
