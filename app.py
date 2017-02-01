from functools import wraps
from flask import Flask, request, redirect
from flask.globals import session
from flask.helpers import url_for
from create_db import create_db
from db_connection import db
from resources.controller import userController, agendaController, baseController

app = Flask(__name__)

app.secret_key = "my precious"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workshop.db'
db.init_app(app)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'loggedin' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap


@app.route('/create')
def create():
    create_db()
    return 'criou'


@app.route('/login', methods=['GET', 'POST'])
def login():
    return baseController.login(request)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    return baseController.signin(request)


@app.route('/logout')
@login_required
def logout():
    return baseController.logout()


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return agendaController.index(session['user_id'])


@app.route('/user/add', methods=['POST'])
@login_required
def user_add():
    return userController.add(request)


@app.route('/user/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def user_edit(id):
    return userController.edit(request, id)


@app.route('/user/delete/<int:id>')
@login_required
def user_delete(id):
    return userController.delete(id)


@app.route('/user/agenda/<int:user_id>', methods=['GET'])
@login_required
def user_agenda(user_id):
    return agendaController.index(user_id)


@login_required
@app.route('/user/agenda/add', methods=['POST'])
def user_agenda_add():
    return agendaController.add(request)


@login_required
@app.route('/user/agenda/edit/<int:id>', methods=['GET', 'POST'])
def user_agenda_edit(id):
    return agendaController.edit(request, id)


@app.route('/user/agenda/delete/<int:id>')
def agenda_delete(id):
    return agendaController.delete(id)


if __name__ == '__main__':
    app.run(debug=True)
