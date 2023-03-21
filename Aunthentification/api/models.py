from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название предмета')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    year = models.IntegerField(verbose_name='Возраст')
    items = models.ManyToManyField('Item', verbose_name='Предметы')
    evaluation = models.IntegerField(verbose_name='Оценка')
    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


class Class(models.Model):
    name = models.CharField(max_length=10, verbose_name='Название класса')
    students = models.ManyToManyField('Student', verbose_name='Ученики')
    year = models.IntegerField(verbose_name='Год обучения')
    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

