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

app = Flask(__name__)    #create Flask object
app.secret_key=os.urandom(32) #secret key for flask to work

teamBord = "Team Bord: Austin Ngan, Roshani Shrestha, Thomas Yu, Mark Zhu" #TNPG + roster for both landing and response pages
# username = "Username" # will change later

# password = "Password123" # will change later

# ================================================================ #

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    '''The response page that will display a greeting, the username, and the request method used'''
    if "user" in session: # checks if the user is logged in
        #print("***DIAG: session['user'] ***")
        #print(session['user'])
        return render_template('userblog.html', heading = teamBord, username = session['user'])
    else:
        return render_template( 'login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route("/register_auth", methods=['GET', 'POST'])
def register_auth():
    if (request.method == 'POST'): # checks if the request method is POST
        tempUser = request.form['username']
        tempPass = request.form['password']
        # print("***DIAG: request.form ***")
        # print(request.form)
        # print("***DIAG: tempUser ***")
        # print(tempUser)
        # print("***DIAG: tempPass ***")
        # print(tempPass)
        if (userdb.checkUser(tempUser)): # checks if the username already exists
            error = "Error: Username already exists."
            return render_template('register.html', message = error)
        elif (tempUser == "" and tempPass == ""):
            error = "Error: No username or password entered."
            return render_template('register.html', message = error)
        elif (tempUser == ""):
            error = "Error: No username entered."
            return render_template('register.html', message = error)
        elif (tempPass == ""):
            error = "Error: No password entered."
            return render_template('register.html', message = error)
        else:
            userdb.addUser(tempUser,tempPass)
            return render_template('login.html', message = "You have successfully registered an account.")

@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    error = ""
    if (request.method == 'POST'): # checks if the request method is POST
        tempUser = request.form['username']
        tempPass = request.form['password']
        if (userdb.checkUserPass(tempUser, tempPass)): # checks if the username and password are both correct
            session['user'] = tempUser # adds session data
            return render_template('userblog.html', heading = teamBord, username = session['user'])
        else:
            if (not userdb.checkUser(tempUser)): # checks if the username is incorrect
                error = "Error: Username does not exist."
            else: # the last case is that only the password is incorrect
                error = "Error: Password is incorrect."
    return render_template( 'login.html', message = error)

@app.route("/back_login", methods=['GET', 'POST'])
def backtologin():
    '''On the register page for when the user wants to go back to the login page instead'''
    return render_template('login.html')
    
@app.route("/logout", methods=['GET', 'POST'])
def logOut():
    '''For when the user logs out of the session'''
    session.pop('user', None)
    return render_template('login.html', message = 'You have successfully logged out.')

# temporary
@app.route("/blog1", methods=['GET', 'POST'])
def blogPage():
    return render_template('indivBlog.html')

@app.route("/createPost", methods=['GET', 'POST'])
def createPost():
    '''For when the user wants to make a new post'''
    return render_template('editBlog.html')

@app.route("/finishPost", methods=['GET', 'POST'])
def finishPost():
    '''For when the user wants to finish their post'''
    title = request.form['title']
    text = request.form['paragraph_text']
    blogKey=os.urandom(32)
    userU=session['user']
    userdb.addBlog(userU, blogKey, title, text)
    return render_template('userblog.html', heading = teamBord, username = userU)

# ================================================================================ #

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
