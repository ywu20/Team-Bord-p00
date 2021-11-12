# Bord's Weblog Hosting Site by Team Bord

## Roster with Roles:
Austin Ngan: Creation/editing blogs (Python and Database)

Mark Zhu: Personal blog page and blog pages of others (HTML templates and Flask to connect the database to the webpage)

Roshani Shrestha: Login/Register Page (HTML templates and Flask sessions)

Thomas Yu (Project Manager): Assisting with HTML templates and database work (user accounts and blogs)

## Description of Website/App:
Bord's Weblog Hosting Site allows the user to register with a username and password. Then, they can log into their personal blog page, where they will have the
opportunity to create a new blog. They can also view and edit their blogs as well as create new entries. The user can edit their past entries. They also have the
opportunity to view other users' blogs. 

## Launch Codes
Launch Virtual Environment:

To create a virtual environment run the command:

`$ python3 -m venv ~/blog`

Activate the Virtual Environment:

`$ . ~/blog/bin/activate`

If your machine uses Windows, replace `bin` with `Scripts`


Clone the Repository:

`$ git clone https://github.com/thomasyu21/Team-Bord-p00.git`


Change Directory and Install Requirements

With a virtual environment launched, run the commands:

`$ cd Team-Bord-p00`

`$ pip3 install -r requirements.txt`


Change Directory and Run Python Script:

`$ cd app`

`$ python3 __init__.py`


Open webpage at http://127.0.0.1:5000/
