from django.http import HttpResponse
from datetime import datetime
import random

def personal_info(request):
    name = "Эржан"
    surname = "Бапыев"
    age = 17
    return HttpResponse(f"Имя: {name}, Фамилия: {surname}, Возраст: {age}")

def hobbies(request):
    hobbies_list = "Увлечения: Рсиования, Программирование, Спорт"
    return HttpResponse(hobbies_list)

def current_time(request):
    now = datetime.now().strftime("%H:%M:%S")
    return HttpResponse(f"Текущее время: {now}")

def random_numbers(request):
    numbers = [random.randint(1, 100) for _ in range(5)]
    return HttpResponse(f"Случайные числа: {', '.join(map(str, numbers))}")


def Book_Detail_view(request, id):
    if request.method == "GET":
        bk_id = get_object_or_404(models.Books_list, id=id)
        return render(
            request,
            template_name="books/Book_Detail.html",
            context={
                "bk_id": bk_id
            }
        )


def Book_List_view(request):
    if request.method == 'GET':
        queryset = models.Books_list.objects.filter().order_by('-id')
        return render(
            request,
            template_name='books/Book_List.html',
            context={
                'bk': queryset
            }
        )

def books_tags_view(request):
    if request.method == 'GET':
        teen_tags = models.Products.objects.filter(tags__name='Подростковый').order_by('-id')
        return render(
            request,
            template_name='products/books_tags.html',
            context={'teen_tags': teen_tags}
        )


# all products

def all_books(request):
    if request.method == 'GET':
        products = models.Products.objects.filter().order_by('-id')
        return render(
            request,
            template_name='products/all_books.html',
            context={
                'products': products
            }
        )

def edit_books_view(request, id):
    bk_id = get_object_or_404(models.Employees, id=id)
    if request.method == 'POST':
        form = forms.EmployeeForm(request.POST, instance=bk_id)
        form.save()
        return HttpResponse('<h3>Books updated successfully!</h3>'
                            '<a href="/Books_list/">Список книг</a>')
    else:
        form = forms.Books_list_Form(instance=bk_id)
    return render(
        request,
        template_name='books/edit_books.html',
        context={
            'form': form,
            'bk_id': bk_id
        }
    )


# delete employee
def drop_books_view(request, id):
    bk_id = get_object_or_404(models.Books_list, id=id)
    bk_id.delete()
    return HttpResponse('<h3>Book delete successfully!</h3>'
                        '<a href="/Books_list/">Список книг</a>')


# create employee

def create_books_view(request):
    if request.method == "POST":
        form = forms.Books_list_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3>Book created successfully!</h3>'
                                '<a href="/Books_list/">Список книг</a>')
    else:
        form = forms.Books_list_Form()

    return render(
        request,
        template_name='books/create_books.html',
        context={'form': form}
    )