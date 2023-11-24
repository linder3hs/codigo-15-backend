from flask import Blueprint
from utils import response_success, response_error
from app.models.users import User
from app.db import db

user_route = Blueprint('user_route', __name__)


@user_route.route("/users")
def get_users():
    try:
        users = User.query.all()
        serialized_users = [user.to_json() for user in users]
        return response_success(serialized_users)
    except Exception as e:
        return response_error(str(e))
