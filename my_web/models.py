from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя Фамилия автора') 
    
    def __str__(self):
        return self.name

    
    
class Book(models.Model):
    headline = models.ManyToManyField(Author)
    
    year = models.PositiveIntegerField(verbose_name='Год издания')
    title = models.CharField(max_length=200, verbose_name='Название книги')

    def __str__(self):
        return self.title

    def dict(self):
        obj = {
            'headline': self.headline,
            'year': self.year,
            'title': self.title,
        }
        return obj