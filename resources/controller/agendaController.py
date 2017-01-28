from datetime import datetime
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
from resources.dao import agendaDao
from resources.helper import date, time
from resources.model.agenda import Agenda


def index(user_id):
    agendas = agendaDao.getAgendas(user_id)
    return render_template('agenda.html', agendas=agendas, post='/user/agenda/add', user_id=user_id,
                           days=date.days(), monthes=date.monthes(), years=date.years(), today=date.today(),
                           now=time.now(), hours=time.hours(), minutes=time.minutes())


def add(request):
    agendaDao.update(Agenda(date.dateFormat(request.form['date']),
                            time.timeFormat(request.form['workStart']), time.timeFormat(request.form['workEnd']),
                            time.timeFormat(request.form['restStart']), time.timeFormat(request.form['restEnd']),
                            request.form['user_id']))
    return redirect(url_for('user_agenda', user_id=request.form['user_id']))


def edit(request, id, user_id):
    agenda = agendaDao.getAgenda(id)
    if request.method == 'POST':
        agenda.update(date.dateFormat(request.form['date']),
                            time.timeFormat(request.form['workStart']), time.timeFormat(request.form['workEnd']),
                            time.timeFormat(request.form['restStart']), time.timeFormat(request.form['restEnd']))
        agendaDao.update(agenda)
        return redirect(url_for('user_agenda', user_id=user_id))
    agendas = agendaDao.getAgendas(user_id)
    return render_template('agenda.html', agenda=agenda, agendas=agendas, post='/user/agenda/edit/'+str(agenda.id)+'/'+str(user_id),
                           user_id=user_id, days=date.days(), monthes=date.monthes(), years=date.years(),
                           today=date.today(), now=time.now(), hours=time.hours(), minutes=time.minutes())


def delete(id, user_id):
    agenda = agendaDao.getAgenda(id)
    agendaDao.delete(agenda)
    return redirect(url_for('user_agenda', user_id=user_id))

