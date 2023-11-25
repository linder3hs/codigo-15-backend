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


@user_route.route("/users/<int:user_id>")
def get_user(user_id):
    try:
        user = User.query.get(user_id)

        if not user:
            return response_error("User not found")

        return response_success(user.to_json())
    except Exception as e:
        return response_error(str(e))


@user_route.route("/users", methods=["POST"])
def add_user():
    try:
        user = User(**request.get_json())
        user.password = bcrypt.generate_password_hash(user.password)
        db.session.add(user)
        db.session.commit()

        return response_success("Usuario creado correctamente", 201)
    except IntegrityError:
        return response_error("El username o email ya existen")
    except Exception as e:
        return response_error(str(e))


@user_route.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        user = User.query.get(user_id)

        if not user:
            return response_error("Task not found")

        new_user = request.json
        user.name = new_user.get("name", user.name)
        user.lastname = new_user.get("lastname", user.lastname)
        user.phone = new_user.get("phone", user.phone)
        user.address = new_user.get("address", user.address)
        user.username = new_user.get("username", user.username)
        user.email = new_user.get("email", user.email)

        db.session.commit()

        return response_success("Tarea actualizada correctamente")
    except Exception as e:
        return response_error(str(e))


@user_route.route("/users/<int:user_id>", methods=['DELETE'])
def detele_user(user_id):
    try:
        user = User.query.get(user_id)

        if not user:
            return response_error("User not found")

        db.session.delete(user)
        db.session.commit()

        return response_success("User deleted")
    except Exception as e:
        return response_error(str(e))
