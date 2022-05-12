from flask import Blueprint, request, Response
from models.Task import Task
from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()
tasks = Blueprint('tasks', __name__, template_folder='templates')


@tasks.route('/tasks/<task_id>', methods=['POST'])
def edit_task(task_id):
    type_json = json.loads(request.get_data())
    action_type = type_json['type']
    if action_type == 'change':
        task = Task.query.get(task_id)
        task.done = not task.done
        db.session.add(task)
        db.session.commit()
        response = Response(
            status=200,
        )
        return response
    if action_type == 'delete':
        task = Task.query.get(task_id)
        db.session.delete(task)
        db.session.commit()
        response = Response(
            status=200,
        )
        return response


@tasks.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    tasks_json = []
    for task in tasks:
        tasks_json.append({
            'id': task.id,
            'user_id': task.user_id,
            'task': task.task,
            'priority': task.priority,
            'done': task.done,
            'created_at': task.created_at.strftime("%d/%m/%Y, %H:%M:%S")
        })
    response = Response(
        response=json.dumps(tasks_json),
        status=200,
        mimetype='application/json'
    )
    return response


@tasks.route('/tasks', methods=['POST'])
def add_task():
    task_json = json.loads(request.get_data())
    new_task = Task(user_id=task_json['user_id'], task=task_json['task'],
                    priority=task_json['priority'], done=False)
    db.session.add(new_task)
    db.session.commit()
    response = Response(
        response=str(new_task.id),
        status=200,
        mimetype='text/plain'
    )
    return response
