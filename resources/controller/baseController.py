#!/usr/bin/env python
# -*- coding: utf-8 -*-
from base64 import b64encode
from flask.globals import session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from resources.controller import userController
from resources.dao import userDao
from resources.model.user import User


def login(request):
    erro = None
    if request.method == 'POST':
        user = userController.checkLogin(request.form['username'], request.form['password'])
        
        if user != None:
            session['loggedin'] = True
            session['user_id'] = user.id
            return redirect(url_for('index'))

        erro = 'Usuário ou Senha incorreto!'
    return render_template('login.html', erro=erro)


def signin(request):
    erro = None
    if request.method == 'POST':
        if userDao.getUsername(request.form['username']) != None:
            erro = 'Usuário já existe'
        elif userDao.getEmail(request.form['email']) != None:
            erro = 'Email já existe'
        elif request.form['password'] != request.form['passwordRepeat']:
            erro = 'Senhas diferentes'
        else:
            photo = request.files['photo']
            userDao.update(User(request.form['username'], request.form['email'], request.form['password'],
                                request.form['name'], b64encode(photo.read())))
            user = userDao.lastUser()
            session['loggedin'] = True
            session['user_id'] = user.id
            return redirect(url_for('index'))
    return render_template('/login.html', erro=erro)


def logout():
    session.pop('loggedin', None)
    session.pop('user_id', None)
    return redirect(url_for('index'))


