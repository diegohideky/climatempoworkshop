from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from resources.dao import userDao
from resources.model.user import User
from resources.helper import encrypt


def index():
    users = userDao.getUsers()
    return render_template('index.html', users=users, post='/user/add')


def add(request):
    userDao.update(User(request.form['name'], request.form['email']))
    return redirect(url_for('index'))


def edit(request, id):
    user = userDao.getUser(id)
    if request.method == 'POST':
        user.update(request.form['name'], request.form['email'])
        userDao.update(user)
        return redirect(url_for('index'))
    users = userDao.getUsers()
    return render_template('index.html', user=user, users=users, post='/user/edit/'+str(user.id))


def delete(id):
    user = userDao.getUser(id)
    userDao.delete(user)
    return redirect(url_for('index'))


def checkLogin(input, password):
    usuario = userDao.getUsernamePassword(input, encrypt.encode(password))

    email = userDao.getEmailPassword(input, encrypt.encode(password))

    if usuario:
        return usuario
    if email:
        return email
    return None

