from app.db import db


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(255))
    priority = db.Column(db.String(255))
    category = db.Column(db.String(255))
    status = db.Column(db.String(50))
    due_date = db.Column(db.Date())
    is_done = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='tasks', lazy=True)

    def __init__(self, title, priority, category, status, due_date, is_done, user_id):
        self.title = title
        self.priority = priority
        self.category = category
        self.status = status
        self.due_date = due_date
        self.is_done = is_done
        self.user_id = user_id

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'priority': self.priority,
            'category': self.category,
            'status': self.status,
            'due_date': self.due_date,
            'is_done': self.is_done,
            'user': {
                'id': self.user.id,
                'user_name': self.user.username,
                'email': self.user.email
            }
        }
