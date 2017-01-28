from db_connection import db


class User(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    agenda = db.relationship("Agenda", backref="users", cascade="all, delete-orphan", lazy='dynamic')

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update(self, name, email):
        self.name = name
        self.email = email
