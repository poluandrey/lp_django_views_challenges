import calendar
from django.http import HttpResponse, HttpResponseNotFound

"""
Вьюха get_month_title_view возвращает название месяца по его номеру. 
Вся логика работы должна происходить в функции get_month_title_by_number.

Задания:
    1. Напишите логику получения названия месяца по его номеру в функции get_month_title_by_number
    2. Если месяца по номеру нет, то должен возвращаться ответ типа HttpResponseNotFound c любым сообщением об ошибке
    3. Добавьте путь в файле urls.py, чтобы при открытии http://127.0.0.1:8000/month-title/тут номер месяца/ 
       вызывалась вьюха get_month_title_view. Например http://127.0.0.1:8000/month-title/3/ 
"""


def get_month_title_by_number(month_number: int) -> str:
    if month_number > 13:
        raise ValueError
    return calendar.month_name[month_number]


def get_month_title_view(request, month_number: int):
    # код писать тут
    try:
        return HttpResponse(get_month_title_by_number(month_number))
    except ValueError:
        return HttpResponseNotFound('Месяца с таким номером не существует')
