from flask import Blueprint
from settings import app

static = Blueprint('static', __name__, template_folder='templates')


@static.route('/')
def index():
    return app.send_static_file('index.html')
