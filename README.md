# Hotel RestAPI With Swagger

This project was built using Flask Framework and SQLite

## Installation

Clone source code in you server using command in terminal (first verify git cli installation) or you can directly download scouce code

```
git clone https://github.com/tahsinAmin/hotelsrestapi.git
```

## Remaining Setup in the terminal

```
1. pip install -r requirements.txt
2. source venv/bin/activate
3. flask run
```

Then [Click here](http://127.0.0.1:5000/)

## Project Requirements

- [x] Use flask
- [x] Using GET method
- [x] Must use OpenAPI standard with JSON responses
- [ ] Able to search by title, amenities, price, location
- [x] I can sort by price
- [x] Must use JWT Token

<!-- # Links (Postman needed) -->

<!-- ## Show Data (GET) -->

<!-- ```
http://127.0.0.1:5000/api/v1/hotels
```

## Show 1 Hotel by id (GET)

```
http://127.0.0.1:5000/api/v1/hotels/1
```

## Sort by price (GET)

```
http://127.0.0.1:5000/api/v1/hotels/sort
``` -->

## Subtasks

- [x] Login User
- [x] Data created inside
- [x] Retrieve hotel info with id
- [x] Sort by price
- [ ] Search by titles & amenities. (Rest for Swagger UI)
- [x] Adding Swagger UI

- [ ] How to use sql in sqlalchemy
- [ ] Comment the Resgister part in auth
- [ ] Make the login post to something which won't need the post feature for authorization.
- [ ] Make it postgreSQL.
- [ ] See how Marshmallow library can help.
- [ ] See how serialization and deserialization cxan help

## What I learned

- ".flaskenv" in order to configure the terminal examlpe, flask_env and flask_app

- SQLAlchemy is an extension of flask. So, it makes it easier to handle databasae queries

- The refresh token serves at least two purposes. First, the refresh token is a kind of 'proof' that an OAuth2 Client has already received permission from the user to access their data, and so can request a new access token again without requiring the user to go through the whole OAuth2 flow.

- BLUEPRINTS ARE MEANT TO GROUP RELATED DFUNCTIONALITY. Blueprint will have code that are related to each other.

- Need to hit "pip freeze > requirements.txt" command everytime we finish our code at the end of the day.

## ERRORS & Solution (Optional)

- Failed to find Flask application or factory in module "flaskr". Use """FLASK\*APP=flaskr:name""" to specify one. (Sol) write "return app" at the end inside the creat*app class which is inside"""* _init_ \_.py"""

- [Unable to install "<PACKAGE>": snap "<PACKAGE>" has "install-snap" change in progress.](https://askubuntu.com/questions/1029117/unable-to-install-package-snap-package-has-install-snap-change-in-pro)

- [How to fix "ModuleNotFoundError: No module named 'validators'"](https://copypaste.guru/WhereIsMyPythonModule/how-to-fix-modulenotfounderror-no-module-named-validators)

- Postman stopped working. Postman web app worked. Later created an account to work correctly.
