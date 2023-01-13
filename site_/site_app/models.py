from django.db import models

class Task(models.Model):
    type = models.CharField('Тип', max_length=40)
    title = models.CharField('Название', max_length=40)
    task = models.TextField('Описание')
    priority = models.CharField('Приоритет', max_length=40)
    deadline = models.CharField('Сроки выполнения', max_length=40)


    def __str__(self):
        return self.title
