# Generated by Django 4.2.13 on 2024-06-11 11:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(default='@gmail.com', max_length=254)),
                ('image', models.ImageField(upload_to='images/')),
                ('about_bk', models.TextField()),
                ('book_status', models.CharField(choices=[('Онгоинг', 'Онгоинг'), ('Анонс', 'Анонс'), ('Завершен', 'Завершен'), ('Приостановлен', 'Приостановлен')], max_length=100, null=True)),
                ('description', models.FileField(upload_to='descriptions/')),
                ('date_of_issue', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'произведение',
                'verbose_name_plural': 'произведения',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewsBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('stars', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reviews_bk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_books', to='books.books_list')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True)),
                ('price', models.PositiveIntegerField(default=110)),
                ('tags', models.ManyToManyField(to='books.tag')),
            ],
        ),
    ]