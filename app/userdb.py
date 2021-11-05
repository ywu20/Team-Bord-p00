import sqlite3   #enable control of an sqlite database

DB_FILE="users.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

command = '''CREATE TABLE IF NOT EXISTS logins(
    username TEXT NOT NULL PRIMARY KEY UNIQUE,
    password TEXT NOT NULL)'''
c.execute(command)

command2 = '''CREATE TABLE IF NOT EXISTS blogs(
    username TEXT NOT NULL PRIMARY KEY UNIQUE,
    blogKey TEXT NOT NULL,
    blogText TEXT NOT NULL)'''
c.execute(command2)

def addUser(username, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO logins VALUES(?, ?)", (username, password))
    db.commit()
    db.close()


def addBlog(username, blogKey, text):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO blogs VALUES(?, ?)", (username, blogKey))
    db.commit()
    db.close()

#def findUsername(uName):
#    db = sqlite3.connect(DB_FILE)
#    c = db.cursor()
#    if ((c.execute("SELECT * FROM logins WHERE username =" + uName))) 
# addUser("hello", "123123a")


