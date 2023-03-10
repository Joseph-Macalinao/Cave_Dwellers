import mysql.connector
from character_create import createCharacter

# Setup connection to MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)
myCursor = mydb.cursor()

"""
def userCreation():
    user_name = ""
    if mydb:
        # Checks to see if database exists
        cmd = str(input("New, Returning, or Create new user:\n"))
    else:
        # Game requires prior setup of MySQL local host with the following info above
        print("Please setup MySQL database before running")
        return

    if cmd.lower() == "new":
        # Check if user is actually returning
        myCursor.execute("SHOW DATABASES")
        for x in myCursor:
            if x[0] == "cavedweller":
                print("Database already exists! Restart and choose Returning or Create")
                return
        # Creates new schema and new user
        myCursor.execute("CREATE database CaveDweller")
        # Setups use of existing database
        existing_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="CaveDweller"
        )
        new_cursor = existing_db.cursor()
        new_cursor.execute("CREATE TABLE users (name VARCHAR(25) PRIMARY KEY, class VARCHAR(255))")
        new_cursor.execute("CREATE TABLE stats (name VARCHAR(25) PRIMARY KEY, wins INT, losses INT, xp INT)")
        new_cursor.execute("CREATE TABLE achievements (name VARCHAR(25) PRIMARY KEY, lvl1 TINYINT, lvl2 TINYINT, "
                           "lvl3 TINYINT, lvl4 TINYINT, lvl5 TINYINT)")
        new_cursor.execute("CREATE TABLE inventory (name VARCHAR(25) PRIMARY KEY, "
                           "heal INT, weapon INT, armor INT, shield INT, gold INT)")
        print("*** Welcome new player ***")
        user_name = str(input("Input new username:\n"))
        character = createCharacter()
        new_cursor.execute("INSERT INTO users (name, class) VALUES (%s, %s)", (user_name, character.arch))
        new_cursor.execute("INSERT INTO stats (name, wins, losses, xp) VALUES (%s, %s, %s, %s)", (user_name, 0, 0, 0))
        new_cursor.execute("INSERT INTO achievements (name, lvl1, lvl2, lvl3, lvl4, lvl5) "
                           "VALUES (%s, %s, %s, %s, %s, %s)", (user_name, int(True), int(False), int(False), int(False),
                                                               int(False)))
        new_cursor.execute("INSERT INTO inventory (name, heal, weapon, armor, shield, gold) "
                           "VALUES (%s, %s, %s, %s, %s, %s)",(user_name, 0, 0, 0, 0, 0))
        existing_db.commit()

    # Setups use of existing database
    existing_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="CaveDweller"
    )
    new_cursor = existing_db.cursor()

    if cmd.lower() == "returning":
        # Lists the existing users
        new_cursor.execute("SELECT users.name FROM users")
        res = new_cursor.fetchall()
        for x in res:
            print(x[0])
        user_name = str(input("Input existing username:\n"))

    if cmd.lower() == "create":
        # Creates a new user
        user_name = str(input("Input new username:\n"))
        new_cursor.execute("SELECT users.name FROM users")
        res = new_cursor.fetchall()
        for x in res:
            if x[0] == user_name:
                print("Username already exists!")
            else:
                continue
        character = createCharacter()
        new_cursor.execute("INSERT INTO users (name, class) VALUES (%s, %s)", (user_name, character.arch))
        new_cursor.execute("INSERT INTO stats (name, wins, losses, xp) VALUES (%s, %s, %s, %s)", (user_name, 0, 0, 0))
        new_cursor.execute("INSERT INTO achievements (name, lvl1, lvl2, lvl3, lvl4, lvl5) "
                           "VALUES (%s, %s, %s, %s, %s, %s), (user_name, int(True), int(False), int(False), int(False),"
                                                               "int(False)")
        new_cursor.execute("INSERT INTO inventory (name, heal, weapon, armor, shield, gold) "
                           "VALUES (%s, %s, %s, %s, %s, %s), (user_name, 0, 0, 0, 0, 0)")
        existing_db.commit()

    sql = "SELECT * FROM users WHERE users.name = %s"
    new_cursor.execute(sql, (user_name,))
    char = new_cursor.fetchall()
    return char
"""

# attempt to adjust user creation to work with pygame, not jsut terminal input
# VVVV

def userCreation(charSelection, action = "create", name = "Player1"):
    """ Function for creating users
    :return res (tuple): row of current user
    """
    user_name = ""
    if mydb:
        # Checks to see if database exists
        pass
    else:
        # Game requires prior setup of MySQL local host with the following info above
        print("Please setup MySQL database before running")
        return

    if action.lower() == "new":
        # Check if user is actually returning
        myCursor.execute("SHOW DATABASES")
        for x in myCursor:
            if x[0] == "cavedweller":
                print("Database already exists! Restart and choose Returning or Create")
                return
        # Creates new schema and new user
        myCursor.execute("CREATE database CaveDweller")
        # Setups use of existing database
        existing_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="CaveDweller"
        )
        new_cursor = existing_db.cursor()
        new_cursor.execute("CREATE TABLE users (name VARCHAR(25) PRIMARY KEY, class VARCHAR(255))")
        new_cursor.execute("CREATE TABLE stats (name VARCHAR(25) PRIMARY KEY, wins INT, losses INT, xp INT)")
        new_cursor.execute("CREATE TABLE achievements (name VARCHAR(25) PRIMARY KEY, lvl1 TINYINT, lvl2 TINYINT, "
                           "lvl3 TINYINT, lvl4 TINYINT, lvl5 TINYINT)")
        new_cursor.execute("CREATE TABLE inventory (name VARCHAR(25) PRIMARY KEY, "
                           "heal INT, weapon INT, armor INT, shield INT, gold INT)")
        print("*** Welcome new player ***")
        user_name = name
        character = createCharacter(charSelection)
        new_cursor.execute("INSERT INTO users (name, class) VALUES (%s, %s)", (user_name, character.arch))
        new_cursor.execute("INSERT INTO stats (name, wins, losses, xp) VALUES (%s, %s, %s, %s)", (user_name, 0, 0, 0))
        new_cursor.execute("INSERT INTO achievements (name, lvl1, lvl2, lvl3, lvl4, lvl5)"
                           "VALUES (%s, %s, %s, %s, %s, %s)",
                           (user_name, int(True), int(False), int(False), int(False), int(False)))
        new_cursor.execute("INSERT INTO inventory (name, heal, weapon, armor, shield, gold)"
                           "VALUES (%s, %s, %s, %s, %s, %s)", (user_name, 0, 0, 0, 0, 0))
        existing_db.commit()

    # Setups use of existing database
    existing_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="CaveDweller"
    )
    new_cursor = existing_db.cursor()

    if action.lower() == "returning":
        # Lists the existing users
        new_cursor.execute("SELECT users.name FROM users")
        res = new_cursor.fetchall()
        for x in res:
            print(x[0])
        user_name = name

    if action.lower() == "create":
        # Creates a new user
        user_name = name
        new_cursor.execute("SELECT users.name FROM users")
        res = new_cursor.fetchall()
        for x in res:
            if x[0] == user_name:
                print("Username already exists!")
            else:
                continue
        character = createCharacter(charSelection)
        new_cursor.execute("INSERT INTO users (name, class) VALUES (%s, %s)", (user_name, character.arch))
        new_cursor.execute("INSERT INTO stats (name, wins, losses, xp) VALUES (%s, %s, %s, %s)", (user_name, 0, 0, 0))
        new_cursor.execute("INSERT INTO achievements (name, lvl1, lvl2, lvl3, lvl4, lvl5) "
                           "VALUES (%s, %s, %s, %s, %s, %s)",
                           (user_name, int(True), int(False), int(False), int(False), int(False)))
        new_cursor.execute("INSERT INTO inventory (name, heal, weapon, armor, shield, gold)"
                           "VALUES (%s, %s, %s, %s, %s, %s)", (user_name, 0, 0, 0, 0, 0))
        existing_db.commit()

    sql = "SELECT * FROM users WHERE users.name = %s"
    new_cursor.execute(sql, (user_name,))
    char = new_cursor.fetchall()
    return char
