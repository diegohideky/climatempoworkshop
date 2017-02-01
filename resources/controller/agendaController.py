from flask.globals import session
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from resources.dao import agendaDao, userDao
from resources.helper import date, time
from resources.model.agenda import Agenda


def index(user_id):
    agendas = agendaDao.getAgendas(user_id)
    user = userDao.getId(user_id)
    return render_template('agenda.html', agendas=agendas, post='/user/agenda/add', user=user,
                           days=date.days(), monthes=date.monthes(), years=date.years(), today=date.today(),
                           now=time.now(), hours=time.hours(), minutes=time.minutes())


def add(request):
    agendaDao.update(Agenda(date.dateFormat(request.form['date']),
                            time.timeFormat(request.form['workStart']), time.timeFormat(request.form['workEnd']),
                            time.timeFormat(request.form['restStart']), time.timeFormat(request.form['restEnd']),
                            request.form['user_id']))
    return redirect(url_for('index'))


def edit(request, id):
    agenda = agendaDao.getAgenda(id)
    if request.method == 'POST':
        agenda.update(date.dateFormat(request.form['date']),
                            time.timeFormat(request.form['workStart']), time.timeFormat(request.form['workEnd']),
                            time.timeFormat(request.form['restStart']), time.timeFormat(request.form['restEnd']))
        agendaDao.update(agenda)
        return redirect(url_for('index'))
    user = userDao.getId(session['user_id'])
    agendas = agendaDao.getAgendas(session['user_id'])
    return render_template('agenda.html', agenda=agenda, agendas=agendas, post='/user/agenda/edit/'+str(agenda.id),
                           user=user, days=date.days(), monthes=date.monthes(), years=date.years(),
                           today=date.today(), now=time.now(), hours=time.hours(), minutes=time.minutes())


def delete(id):
    agenda = agendaDao.getAgenda(id)
    agendaDao.delete(agenda)
    return redirect(url_for('index'))

