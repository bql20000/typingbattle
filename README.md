# Typing Battle - University Web Application Project

A special assignment of Web Application course at university.
The application provides 3 sections: a typing area for users to practice, a shopping area with a collection of keyboards, user registration and authentication system.
To have a deeper understanding of Typing Battle, please have a look at the [PROJECT REPORT](https://docs.google.com/document/d/1d-4XXpHI4Wi4N8-HKsQA6gPPJQUqTAXVNQBnbvRkiLM/edit?usp=sharing). <br>

Teck Stack: <br>
- Architecture: REST
- Design: Single Page Application
- Database: MySQL
- Front-end: HTML5, CSS, Javascript, Ajax, Bootstrap, jQuery
- Back-end: Python, Flask, Flask-SQLALchemy, JWT


## Installation 
#### 1. Prerequisites
- Python 3.0 or later is required. If you haven't installed it, please visit https://www.python.org/downloads/. (version 3.8.6 is recommended since it was used during the development process).
- <code>pip</code> (package installer for Python). Follow the instructions in https://pypi.org/project/pip/ to get the lastest version.

#### 2. Download the project
- This could be easily down via download button on GitHub or you can use <code>git clone</code> if you prefer.

#### 3. Setting up a virtual environment
To avoid environmental conflicts, let's set up a virtual environment to run the application
- Download the virtualenv package:
> $ pip install virtualenv 
- Now direct to the root folder of Catalog, creat a new virtual environment with specific python version (here I use python 3.8). You can also change the name of the environment if you want (here I set its name is <code>venv</code>).
> $ virtualenv venv --python=python3.8
- Now activate the environment:
> $ source venv/bin/activate 

#### 4. Installing third-party libraries
All the required packages have been listed in <code>requirements.txt</code>. In the terminal, run the following command to install them:
> $ pip install -r requirements.txt
>
Some of the main packages you might want to have a look at:
- [Flask](https://flask.palletsprojects.com/en/1.1.x/): Micro web framework
- [Flask-SQLALchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/): Object-relational mapping (ORM)
- [pyJWT](https://pyjwt.readthedocs.io/en/latest/): Encoding and decoding the JSON Web Token. 
- [marshmallow](https://marshmallow.readthedocs.io/en/stable/): Validating request data
- [flask-hashing](https://flask-hashing.readthedocs.io/en/latest/): Hashing user's password
- [pytest](https://docs.pytest.org/en/stable/): Writing unit tests

#### 5. Setting up SQL server
- Login into MySQL and create 3 databases: **typing_battle**, **typing_battle_development** and **typing_battle_test**
for *production*, *development* and *testing* environment respectively. This can be done by logging in to the MySQL server, then open a WorkBench Query Tab and execute the following statement:
> CREATE DATABASE typing_battle;
>
> CREATE DATABASE typing_battle_development;
>
> CREATE DATABASE typing_battle_testing;

- All the tables will be automatically generated when we first run the application, thus we don't have to do it manually. 
However, you will need to tell the application the URI of your SQL server. 
To do this, look for the <code>config.ini</code> file in the <code>config</code> folder, 
set the attributes of the environment you want to work with. 
For example, if you are running mysql on a local machine with development environment:
<br>
<code>[mysql-development]<br>
host = localhost<br>
database = typing_battle_development<br>
user = root<br>
password = 123456<br></code>


#### 6. Some configuration
In <code>config</code> folder, you can change these following configuration: 
- <code>SECRET_KEY</code>: secret key used for authorization system. 
- <code>JWT_EXPIRATION_PERIOD</code>: the length of expiration period of JWT access token.

## Setting up a local host web server
- From the terminal, declare the environment variables:
> $ export ENVIRONMENT=development
- Then, run the application
> $ ENVIRONMENT=development python run.py
- Now, all the tables have been created in the database. 
We need to init some data for the application. 
Open an IDE, then execute 3 following files in <code>main/data</code>: <br>
    - save_common_english_words.py
    - save_products.py
    - save_units.py

- The application is now ready at localhost: <code>http://127.0.0.1:5000</code>.


## Testing
- [Postman](https://www.postman.com): You can use postman to create custom requests to our local host.
- [Pytest](https://docs.pytest.org/en/stable/): I wrote several tests in the <code>tests</code> folder. You can write some test by your own, there are functions in <code>helpers.py</code> may help you simplify the work. But first, let's switch to testing environment:
> $ export FLASK_ENV=testing

- After that, run this command to obtain the testing results:
> $ pytest --cov
