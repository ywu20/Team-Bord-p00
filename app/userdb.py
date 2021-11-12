import sqlite3   #enable control of an sqlite database

DB_FILE="users.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

# PRIMARY KEY UNIQUE
command = '''CREATE TABLE IF NOT EXISTS logins(
    username TEXT NOT NULL,
    password TEXT NOT NULL)'''
c.execute(command)

# PRIMARY KEY UNIQUE
command2 = '''CREATE TABLE IF NOT EXISTS blogs(
    username TEXT NOT NULL,
    blogTitle TEXT NOT NULL,
    blogText TEXT NOT NULL)'''
c.execute(command2)

command3 = '''CREATE TABLE IF NOT EXISTS entries(
    user TEXT NOT NULL,
    blogTitle TEXT NOT NULL,
    entryTitle TEXT NOT NULL,
    entryText TEXT NOT NULL,
    id INTEGER PRIMARY KEY AUTOINCREMENT)'''
c.execute(command3)

db.commit()
db.close()

def addUser(username, password):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO logins VALUES(?, ?)", (username, password))
    db.commit()
    db.close()


def addBlog(username, title, text):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO blogs VALUES(?, ?, ?)", (username, title, text))
    db.commit()
    db.close()

def makeLoginsDict():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT * FROM logins")
    logininfo = c.fetchall()

    loginsinfo = {} # create a dictionary for all the login information

    for login in logininfo:
        loginsinfo[login[0]] = login[1]

    return loginsinfo
    db.commit()
    db.close()

def checkUser(username):
    loginsinfo = makeLoginsDict()
    return username in loginsinfo.keys()

def checkUserPass(username, password):
    loginsinfo = makeLoginsDict()
    return (username in loginsinfo.keys()) and (loginsinfo[username] == password)

def findBlogs(username):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT blogTitle FROM blogs WHERE username = " + "'" + username + "'")
    titles=c.fetchall()
    c.execute("SELECT blogText FROM blogs WHERE username = " + "'" + username + "'")
    text=c.fetchall()
    dictionary={}
    i = 0
    while (i < len(titles)):
        dictionary[titles[i][0]]=text[i][0]
        i += 1
    return dictionary
    db.commit()
    db.close()

def editBlog(UName, title, newTitle, text):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE blogs SET blogText = " + "'" + text + "'" + "WHERE username = " + "'" + UName + "'" + " AND blogTitle = " + "'" + title + "'")
    c.execute("UPDATE blogs SET blogTitle = " + "'" + newTitle + "'" + "WHERE username = " + "'" + UName + "'" + " AND blogTitle = " + "'" + title + "'")
    db.commit()
    db.close()

def findAllBlogs():
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        c.execute("SELECT blogTitle FROM blogs")
        titles=c.fetchall()
        c.execute("SELECT blogText FROM blogs")
        text=c.fetchall()
        dictionary={}
        i = 0
        while (i < len(titles)):
            dictionary[titles[i][0]]=text[i][0]
            i += 1
        return dictionary
        db.commit()
        db.close()

def addEntry(username, blogTitle, entryTitle, entryText):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("INSERT INTO entries(user, blogTitle, entryTitle, entryText) VALUES(?, ?, ?, ?)", (username, blogTitle, entryTitle, entryText))
    db.commit()
    db.close()

def findEntries(username, blogTitle):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("SELECT entryTitle FROM entries WHERE user = "+"'"+username+"'"+"AND blogTitle = "+"'"+blogTitle+"'"+"ORDER BY id DESC")
    entryTitles=c.fetchall()
    c.execute("SELECT entryText FROM entries WHERE user = "+"'"+username+"'"+"AND blogTItle = "+"'"+blogTitle+"'"+"ORDER BY id DESC")
    entryText=c.fetchall()
    dictionary={}
    i = 0
    while (i < len(entryTitles)):
        dictionary[entryTitles[i][0]]=entryText[i][0]
        i += 1
    return dictionary
    db.commit()
    db.close()

def editEntry(UName, blog, title, newTitle, text):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("UPDATE entries SET entryText = " + "'" + text + "'" + "WHERE user = " + "'" + UName + "'" + "AND blogTitle = " + "'"+blog+"'" + " AND entryTitle = " + "'" + title + "'")
    c.execute("UPDATE entries SET entryTitle = " + "'" + newTitle + "'" + "WHERE user = " + "'" + UName + "'" + " AND entryTitle = " + "'" + title + "'")
    db.commit()
    db.close()

def findAllUsers():
        db = sqlite3.connect(DB_FILE)
        c = db.cursor()
        c.execute("SELECT username FROM logins")
        users=c.fetchall()
        dictionary={}
        i = 0
        while (i < len(users)):
            dictionary[users[i][0]]=users[i][0]
            i += 1
        return dictionary
        db.commit()
        db.close()

def removeBlog(UName, title):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("DELETE FROM blogs " + "WHERE username = " + "'" + UName + "'" + "AND blogTitle = " + "'"+title+"'")
    db.commit()
    db.close()

def removeEntry(UName, titleB, titleE):
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    c.execute("DELETE FROM entries " + "WHERE user = " + "'" + UName + "'" + "AND blogTitle = " + "'"+titleB+"'"+"AND entryTitle = " + "'"+titleE+"'")
    db.commit()
    db.close()
