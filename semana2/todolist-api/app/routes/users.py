from flask import Blueprint, request
from utils import response_success, response_error
from app.models.users import User
from sqlalchemy.exc import IntegrityError
from app.crypt import bcrypt
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


@user_route.route("/users", methods=["POST"])
def add_user():
    try:
        user = User(**request.get_json())
        print(bcrypt.generate_password_hash(user.password))
        # db.session.add(user)
        # db.session.commit()

        return response_success("Usuario creado correctamente", 201)
    except IntegrityError:
        return response_error("El username o email ya existen")
    except Exception as e:
        return response_error(str(e))
