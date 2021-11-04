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
    blogKey TEXT NOT NULL
    blogText TEXT NOT NULL)'''

def addUser(username, password):
    c.execute("INSERT INTO logins VALUES(?, ?)", (username, password))


def addBlog(username, blogKey, text):
	c.execute("INSERT INTO blogs VALUES(?, ?)", (username, blogKey)

#addUser("hello", "123123a")

db.commit()
db.close()

