from db_connection import db
from resources.model.user import User


def getUser(id):
    return User.query.get(id)


def getUsers():
    return User.query.all()


def update(user):
    db.session.add(user)
    db.session.commit()


def delete(user):
    db.session.delete(user)
    db.session.commit()
