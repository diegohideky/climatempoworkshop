from db_connection import db


class Agenda(db.Model):
    __tablename__ = "agendas"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    work_start = db.Column(db.Time)
    work_end = db.Column(db.Time)
    rest_start = db.Column(db.Time)
    rest_end = db.Column(db.Time)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    user = db.relationship('User')

    def __init__(self, date, work_start, work_end, rest_start, rest_end, user_id):
        self.date = date
        self.work_start = work_start
        self.work_end = work_end
        self.rest_start = rest_start
        self.rest_end = rest_end
        self.user_id = user_id


    def update(self, date, work_start, work_end, rest_start, rest_end):
        self.date = date
        self.work_start = work_start
        self.work_end = work_end
        self.rest_start = rest_start
        self.rest_end = rest_end