import os
from dotenv import load_dotenv
from flask import *
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, inspect

app = Flask(__name__,
            static_url_path='',
            static_folder='./public')
CORS(app)

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
if not inspect(engine).has_table("tasks"):
    db.create_all()


@app.route('/')
def index():
    return app.send_static_file('index.html')
