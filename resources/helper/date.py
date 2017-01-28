#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime


def days():
    lista = []
    for i in range(31):
        lista.append(i + 1)
    return lista


def monthes():
    lista = []
    for i in range(12):
        lista.append(i + 1)
    return lista


def years():
    lista = []
    data = datetime.date.today()
    for i in range(100):
        lista.append(data.year - i)
    return lista


def today():
    return datetime.date.today()


def dateFormat(date):
    return datetime.datetime.strptime(date, "%Y-%m-%d").date()


