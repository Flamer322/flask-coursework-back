from settings import app
from routes.Task import tasks
from routes.User import users

app.register_blueprint(tasks)
app.register_blueprint(users)


if __name__ == '__main__':
    app.run(debug=True)
