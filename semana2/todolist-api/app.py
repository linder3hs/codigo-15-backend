from flask import Flask
from app.routes.tasks import task_route
from app.routes.users import user_route
from app.db import db
from app.config import Config

# instancia de Flaks
app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(task_route)
app.register_blueprint(user_route)

db.init_app(app)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
