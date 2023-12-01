class Config:
    SECRET_KEY = "customsecretkey"
    # SQL
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/codigo_15_flask"
    SQLALCHEMY_TRACKS_MODIFICATIONS = False
    # JWT
    JWT_SECRET_KEY = "super-secret"

