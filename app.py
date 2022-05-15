from settings import app, engine
from routes.Task import tasks
from routes.User import users
from routes.Static import static
from models.Task import Task
from models.User import User

Task.__table__.create(bind=engine, checkfirst=True)
User.__table__.create(bind=engine, checkfirst=True)

app.register_blueprint(tasks)
app.register_blueprint(users)
app.register_blueprint(static)


if __name__ == '__main__':
    app.run(debug=True)
