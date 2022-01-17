# Subtasks

- [ ] Make it postgreSQL

# What I learned

- ".flaskenv" in order to configure the terminal examlpe, flask_env and flask_app

- SQLAlchemy is an extension of flask. So, it makes it easier to handle databasae queries

- The refresh token serves at least two purposes. First, the refresh token is a kind of 'proof' that an OAuth2 Client has already received permission from the user to access their data, and so can request a new access token again without requiring the user to go through the whole OAuth2 flow.

- BLUEPRINTS ARE MEANT TO GROUP RELATED DFUNCTIONALITY. Blueprint will have code that are related to each other.

# ERRORS & Solution (Optional)

- Failed to find Flask application or factory in module "flaskr". Use """FLASK\*APP=flaskr:name""" to specify one. (Sol) write "return app" at the end inside the creat*app class which is inside"""* _init_ \_.py"""

- (Unable to install "<PACKAGE>": snap "<PACKAGE>" has "install-snap" change in progress.)[https://askubuntu.com/questions/1029117/unable-to-install-package-snap-package-has-install-snap-change-in-pro]

- (How to fix "ModuleNotFoundError: No module named 'validators'")[https://copypaste.guru/WhereIsMyPythonModule/how-to-fix-modulenotfounderror-no-module-named-validators]

# Commands

#2

- pip install flask

#3

- pip3 install python-dotenv

#5

- pip install -U Flask-SQLAlchemy

#7

- pip install validators

#8

- pip install flask-jwt-extended
