#Team Bord: Austin Ngan (Gerald), Thomas Yu (Perry), Mark Zhu (Bob the Third Jr), Roshani Shrestha (Pete)
#SoftDev
#P00

#from flask import Flask             #facilitate flask webserving
#from flask import render_template   #facilitate jinja templating
#from flask import request           #facilitate form submission
#from flask import session           #facilitate session

from flask import Flask, render_template, request, session
import userdb   #enable control of an sqlite database
import os

app = Flask(__name__)    # create Flask object
app.secret_key=os.urandom(32) # generates a secret key

teamBord = "Team Bord: Austin Ngan, Roshani Shrestha, Thomas Yu, Mark Zhu" #TNPG + roster for both landing and response pages

# ================================================================ #

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    '''
    Displays the login page or the user's personal blog page if they are logged in.
    '''
    if "user" in session: # checks if the user is logged in
        return render_template('userblog.html', sessonU = True, heading = teamBord, username = session['user'], listBlog = userdb.findBlogs(session['user']))
    else:
        return render_template( 'login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    '''
    Takes the user to the register page after pressing the button on the login page.
    '''
    return render_template('register.html')

@app.route("/register_auth", methods=['GET', 'POST'])
def register_auth():
    '''
    Checks if the new username and password provided by the user on the register page are valid.
    Uses the database users.db to check if the username exists already.
    Also checks if the user didn't input any username and/or password.
    '''
    if (request.method == 'POST'): # checks if the request method is POST
        tempUser = request.form['username']
        tempPass = request.form['password']
        if (userdb.checkUser(tempUser)): # checks if the username already exists
            error = "Error: Username already exists."
            return render_template('register.html', message = error)
        elif (tempUser == "" and tempPass == ""): # checks if the both the username and password are empty
            error = "Error: No username or password entered."
            return render_template('register.html', message = error)
        elif (tempUser == ""): # checks if only the username is empty
            error = "Error: No username entered."
            return render_template('register.html', message = error)
        elif (tempPass == ""): # checks if only the password is empty
            error = "Error: No password entered."
            return render_template('register.html', message = error)
        else: # last case is that both the username and password are good
            userdb.addUser(tempUser,tempPass)
            return render_template('login.html', message = "You have successfully registered an account.")

@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    '''
    Checks if the username and password provided by the user in the login page are correct.
    Uses the database users.db.
    '''
    error = ""
    if (request.method == 'POST'): # checks if the request method is POST
        tempUser = request.form['username']
        tempPass = request.form['password']
        if (userdb.checkUserPass(tempUser, tempPass)): # checks if the username and password are both correct
            session['user'] = tempUser # adds session data
            return render_template('userblog.html', sessionU = True, heading = teamBord, username = session['user'], listBlog = userdb.findBlogs(request.form['username']))
        else:
            if (not userdb.checkUser(tempUser)): # checks if the username is incorrect
                error = "Error: Username does not exist."
            else: # the last case is that only the password is incorrect
                error = "Error: Password is incorrect."
    return render_template( 'login.html', message = error)

@app.route("/back_login", methods=['GET', 'POST'])
def backtologin():
    '''
    Takes the user back to the login page after they press the button on the register page.
    '''
    return render_template('login.html')

@app.route("/logout", methods=['GET', 'POST'])
def logOut():
    '''
    Logs the user out of the session.
    '''
    session.pop('user', None) # removes the session
    return render_template('login.html', message = 'You have successfully logged out.') # takes the user back to the login page

# temporary
@app.route("/blogpage", methods=['GET', 'POST'])
def blogPage():
    blogs = userdb.findBlogs(session['user'])
    title = request.form['blogsub']
    entries = userdb.findEntries(session['user'], title)
    return render_template('indivBlog.html', blogTitle = title, sessionU = True, username = session['user'], blogDescription = blogs[title], entriesList = entries)

@app.route("/createPost", methods=['GET', 'POST'])
def createPost():
    '''For when the user wants to make a new post'''
    return render_template('createBlog.html')

@app.route("/finishBlog", methods=['GET', 'POST'])
def finishPost():
    '''
    For when the user wants to finish their post
    '''
    title = request.form['title']
    text = request.form['paragraph_text']
    blogKey=os.urandom(32)
    userU=session['user']
    userdb.addBlog(userU, blogKey, title, text)
    # print(request.form['sub1'])
    return render_template('userblog.html', sessionU = True, heading = teamBord, username = userU, listBlog = userdb.findBlogs(session['user']))

@app.route("/displayAll", methods=['GET', 'POST'])
def displayAll():
    return render_template('allBlogs.html', users = userdb.findAllUsers())

@app.route("/userblogs", methods=['GET', 'POST'])
def otherUserPage():
    user = request.form['usersub']
    blogs = userdb.findBlogs(user)
    return render_template('userblog.html', sessionU = False, username = user, listBlog = blogs)

@app.route("/editPost", methods=['GET', 'POST'])
def editPost():
    blogTitle = request.form['blogTitle']
    title = request.form['entrysub']
    entry = userdb.findEntryText(session['user'], blogTitle, title)
    return render_template('editBlog.html', entryTitle = title, entryText = entry, blogTitle = blogTitle)

@app.route("/finishEditPost", methods=['GET', 'POST'])
def finishEditPost():
    '''
    For when the user wants to edit a previous Post
    '''
    userU=session['user']
    title = request.form['title']
    oldTitle = request.form['oldTitle']
    text = request.form['paragraph_text']
    blogTitle = request.form['blogTitle']
    userdb.editEntry(userU, blogTitle, oldTitle, title, text)
    blogs = userdb.findBlogs(userU)
    entries = userdb.findEntries(userU, blogTitle)
    return render_template('indivBlog.html', blogTitle = blogTitle, sessionU = True, username = session['user'], blogDescription = blogs[blogTitle], entriesList = entries)

@app.route("/createEntry", methods=['GET', 'POST'])
def createEntry():
    title = request.form['blogTitle']
    return render_template('createEntry.html', blogTitle = title)

@app.route("/finishEntry", methods=['GET', 'POST'])
def finishEntry():
    blogTitle = request.form['blogTitle']
    title = request.form['title']
    text = request.form['paragraph_text']
    userU=session['user']
    userdb.addEntry(userU, blogTitle, title, text)
    blogs = userdb.findBlogs(userU)
    entries = userdb.findEntries(userU, blogTitle)
    return render_template('indivBlog.html', blogTitle = blogTitle, sessionU = True, username = session['user'], blogDescription = blogs[blogTitle], entriesList = entries)


# ================================================================================ #

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
