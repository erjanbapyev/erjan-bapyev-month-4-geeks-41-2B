from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail_view(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/book_detail.html', {'book': book})





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


