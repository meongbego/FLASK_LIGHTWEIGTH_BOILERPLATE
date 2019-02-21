from . import configs
from flask import Flask
import os, psycopg2

app = Flask(__name__)
app.config.from_object(configs.Config)


conn = psycopg2.connect(
    database=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    sslmode=os.getenv('DB_SSL'),
    port=os.getenv('DB_PORT'),
    host=os.getenv('DB_HOST')
)

conn.set_session(autocommit=True)
db = conn.cursor()

# registering controllers
from app.controllers import *


