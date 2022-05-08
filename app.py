from flask import *
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine, inspect
import json

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:#kUjnQ_1@localhost:5433/coursework"
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


engine = create_engine("postgresql://postgres:#kUjnQ_1@localhost:5433/coursework")
if not inspect(engine).has_table("tasks"):
    db.create_all()


@app.route('/tasks/<task_id>', methods=['POST'])
def edit_task(task_id):
    type_json = json.loads(request.get_data())
    action_type = type_json['type']
    if action_type == 'change':
        task = Task.query.get(task_id)
        task.done = not task.done
        db.session.add(task)
        db.session.commit()
        response = app.response_class(
            status=200,
        )
        return response
    if action_type == 'delete':
        task = Task.query.get(task_id)
        db.session.delete(task)
        db.session.commit()
        response = app.response_class(
            status=200,
        )
        return response


@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    tasks_json = []
    for task in tasks:
        tasks_json.append({
            'id': task.id,
            'user_sub': task.user_sub,
            'task': task.task,
            'done': task.done
        })
    response = app.response_class(
        response=json.dumps(tasks_json),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/tasks', methods=['POST'])
def add_task():
    task_json = json.loads(request.get_data())
    new_task = Task(user_sub=task_json['user_sub'], task=task_json['newTask'], done=False)
    db.session.add(new_task)
    db.session.commit()
    response = app.response_class(
        response=str(new_task.id),
        status=200,
        mimetype='text/plain'
    )
    return response


if __name__ == '__main__':
    app.run(debug=True)
