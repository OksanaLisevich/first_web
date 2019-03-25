# Generated by Django 2.1.7 on 2019-03-19 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя автора')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия автора')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(verbose_name='Год издания')),
                ('title', models.CharField(max_length=200, verbose_name='Название книги')),
                ('headline', models.ManyToManyField(to='my_web.Author')),
            ],
        ),
    ]
