from datetime import datetime


def now():
    return datetime.now()


def hours():
    lista = []
    for i in range(24):
        lista.append(reformat(i))
    return lista


def minutes():
    lista = []
    for i in range(60):
        lista.append(reformat(i))
    return lista


def reformat(i):
    if i < 10:
        return '0' + str(i)
    return i


def timeFormat(time):
    return datetime.strptime(time, "%H:%M").time()

