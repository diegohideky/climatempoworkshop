from flask import Flask, request
from create_db import create_db
from db_connection import db
from resources.controller import userController, agendaController

app = Flask(__name__)

app.secret_key = "my precious"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workshop.db'
db.init_app(app)


@app.route('/create')
def create():
    create_db()
    return 'criou'


@app.route('/', methods=['GET'])
def index():
    return userController.index()


@app.route('/user/add', methods=['POST'])
def user_add():
    return userController.add(request)


@app.route('/user/edit/<int:id>', methods=['GET', 'POST'])
def user_edit(id):
    return userController.edit(request, id)


@app.route('/user/delete/<int:id>')
def user_delete(id):
    return userController.delete(id)


@app.route('/user/agenda/<int:user_id>', methods=['GET'])
def user_agenda(user_id):
    return agendaController.index(user_id)


@app.route('/user/agenda/add', methods=['POST'])
def user_agenda_add():
    return agendaController.add(request)


@app.route('/user/agenda/edit/<int:id>/<int:user_id>', methods=['GET', 'POST'])
def user_agenda_edit(id, user_id):
    return agendaController.edit(request, id, user_id)


@app.route('/user/agenda/delete/<int:id>/<int:user_id>')
def agenda_delete(id, user_id):
    return agendaController.delete(id, user_id)


if __name__ == '__main__':
    app.run(debug=True)
