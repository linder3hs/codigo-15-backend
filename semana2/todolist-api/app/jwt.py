from flask_jwt_extended import JWTManager
from utils import response_error

jwt = JWTManager()


@jwt.unauthorized_loader
def unauthorized_callback(callback):
    return response_error(callback)
