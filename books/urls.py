from django.urls import path
from . import views


urlpatterns = [
    path('books_info/', views.books_info_view),
    path('about_author/', views.about_author_view),
    path('hobbies/', views.hobbies_view),
    path('current_time/', views.current_time_view),
    path('random_numbers/', views.random_numbers_view),
]
