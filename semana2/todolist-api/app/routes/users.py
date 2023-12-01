from flask import Blueprint, request
from utils import response_success, response_error
from app.models.users import User
from app.models.tasks import Task
from sqlalchemy.exc import IntegrityError
from app.crypt import bcrypt
from app.db import db
from flask_jwt_extended import create_access_token
from datetime import timedelta

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
        # ante de eliminar al usuario vamos a verificar que el no tenga tareas
        tasks_by_user = Task.query.filter_by(user_id=user_id).all()

        if len(tasks_by_user) is 0:
            user = User.query.get(user_id)

            if not user:
                return response_error("User not found")

            db.session.delete(user)
            db.session.commit()

            return response_success("User deleted")
        return response_success("El usuario no puede ser eliminado porque tiene tareas pendientes")

    except Exception as e:
        return response_error(str(e))


@user_route.route("/login", methods=['POST'])
def login():
    try:
        body = request.get_json()
        email = body.get("email")
        password = body.get("password")

        user = User.query.filter_by(email=email).first()

        if not user:
            return response_error("Email y/o Password incorrectos")
        # parametro 1: es el password encriptado
        # parametro 2: password sin encriptar
        if not bcrypt.check_password_hash(user.password, password):
            return response_error("Email y/o Password incorrectos")

        # nota por defecto el token dura 15 min
        token = create_access_token(identity=user.email, expires_delta=timedelta(weeks=2))
        return response_success({
            'user': user.to_json(),
            'access_token': token
        })
    except Exception as e:
        return response_error(str(e))
