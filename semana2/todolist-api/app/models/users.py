from app.db import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255), unique=True)
    address = db.Column(db.String(255))
    password = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())

    def __int__(self, name, lastname, email, username, address, password, phone):
        self.name = name
        self.lastname = lastname,
        self.email = email
        self.username = username
        self.address = address
        self.password = password
        self.phone = phone

    def to_json(self):
        return {
            'id': self.id,
            'full_name': f"{self.name} {self.lastname}",
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
        }
