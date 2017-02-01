from db_connection import db


class User(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    name = db.Column(db.String)
    password = db.Column(db.String)
    photo = db.Column(db.LargeBinary)
    agenda = db.relationship("Agenda", backref="users", cascade="all, delete-orphan", lazy='dynamic')

    def __init__(self, username, email, password, name,  photo):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.photo = photo

    def update(self, username, email, password, name, photo):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.photo = photo
