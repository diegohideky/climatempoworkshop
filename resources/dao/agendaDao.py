from db_connection import db
from resources.model.agenda import Agenda


def getAgenda(id):
    return Agenda.query.get(id)


def getAgendas(id):
    return db.session.query(Agenda).filter(Agenda.user_id==id).order_by(Agenda.date.desc(), Agenda.work_start).all()


def update(agenda):
    db.session.add(agenda)
    db.session.commit()


def delete(agenda):
    db.session.delete(agenda)
    db.session.commit()
