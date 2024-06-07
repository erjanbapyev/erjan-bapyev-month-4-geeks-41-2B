from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    image = models.ImageField(upload_to='images/')
    about_emp = models.TextField()
    programming_status = models.CharField(max_length=255)
    rezume = models.FileField(upload_to='resumes/')
    date_of_birth = models.DateField()
    github = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
