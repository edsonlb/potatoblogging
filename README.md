Potato Blogging Tool
=========
<br />
<p align="center"><img src="http://edsonlopes.com/arquivos/potato.jpg"></p>
<br />
Project developed for Potato London
<br />
For settings_secret.py, create this file on potatoblogging/settings_secret.py and put this line: 
SECRET_KEY_SETTINGS = 'A secret key for a particular Django installation'
DB_ENGINE = 'Database driver'
DB_NAME = 'Database name'                     
DB_USER = 'Database user'
DB_PASSWORD = 'Database password'
DB_PORT = 'Database connection port'
DB_HOST = 'IP or /cloudsql/GAE_app:GAE_database_id'
<br />

First I developed this project with Django 1.6, but because of the compatibility with GAE I had to end up going back to version 1.5.

Live Demo: http://potatoblogging.appspot.com/
Layout: http://aozora.github.io/bootmetro/


https://github.com/edsonlb