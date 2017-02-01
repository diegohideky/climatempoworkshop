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


def getUsernamePassword(input, password):
    return db.session.query(User).filter(User.username==input, User.password==password).first()


def getEmailPassword(input, password):
    return db.session.query(User).filter(User.email==input, User.password==password).first()


def lastUser():
    return db.session.query(User).order_by(User.id.desc()).first()


def getUsername(username):
    return db.session.query(User).filter(User.username==username).first()


def getEmail(email):
    return db.session.query(User).filter(User.email==email).first()


def getId(user_id):
    return User.query.get(user_id)
