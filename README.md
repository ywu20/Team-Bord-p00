# Bord's Weblog Hosting Site by Team Bord

## Roster with Roles:
Austin Ngan: Creation/editing blogs (Python and Database)

Mark Zhu: Personal blog page and blog pages of others (HTML templates and Flask to connect the database to the webpage)

Roshani Shrestha: Login/Register Page (HTML templates and Flask sessions)

Thomas Yu (Project Manager): Assisting with HTML templates and database work (user accounts and blogs)

## Description of Website/App:
Bord's Weblog Hosting Site that allows the user to create their own blogs and view the blogs of others. To use Bord's Weblog Hosting Site you need an account, so make sure to register! Logging in takes a user to their personal blog page, where they can create a new blog or view and old one. Within each blog they can add, edit, and remove entries. They are also able to edit or remove the blog itself. Lastly, users are able view the blogs and blog entries of other users.

## Launch Codes
Launch Virtual Environment:

To create a virtual environment run the command:

`$ python3 -m venv <path_to_virtual_environment>`

Activate the Virtual Environment:

`$ . <path_to_virtual_environment>/bin/activate`

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
