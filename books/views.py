from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random


def books_info_view(request):
    if request.method == 'GET':
        return HttpResponse('Это приложение Books. Здесь вы найдете информацию о книгах.')

def about_author_view(request):
    if request.method == 'GET':
        return HttpResponse('Меня зовут [Имя Фамилия], и я автор книг в данной библиотеке.')

def hobbies_view(request):
    if request.method == 'GET':
        return HttpResponse('Мои хобби: [Список ваших хобби].')

def current_time_view(request):
    if request.method == 'GET':
        now = datetime.now()
        return HttpResponse(f'Текущее время: {now}')

def random_numbers_view(request):
    if request.method == 'GET':
        random_num = random.randint(1, 100)
        return HttpResponse(f'Случайное число: {random_num}')


