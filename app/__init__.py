from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = '123456'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'pet_rescue'

mysql = MySQL(app)
