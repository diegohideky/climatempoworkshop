from db_connection import db
from resources.model.master import Master
from resources.helper import encrypt


def create_db():
    db.create_all()

    db.session.add(Master('diegohideky', 'diegohideky@gmail.com', encrypt.encode('workshopdiego95.')))

    db.session.commit()


