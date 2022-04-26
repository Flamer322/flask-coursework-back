from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine, inspect
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:#kUjnQ_1@localhost:5432/coursework"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    user_sub = db.Column(db.String(80), unique=False, nullable=False)
    task = db.Column(db.String(255), unique=False, nullable=False)
    done = db.Column(db.Boolean, unique=False, nullable=False)

    def __init__(self, user_sub, task, done):
        self.user_sub = user_sub
        self.task = task
        self.done = done

    def __repr__(self):
        return '<Task %r>' % self.task


engine = create_engine("postgresql://postgres:#kUjnQ_1@localhost:5432/coursework")
if not inspect(engine).has_table("tasks"):
    db.create_all()


@app.route('/tasks', methods=['POST'])
def add_user():
    task_json = json.loads(request.get_data())
    new_task = Task(user_sub=task_json['sub'], task=task_json['newTask'], done=False)
    db.session.add(new_task)
    db.session.commit()
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)
