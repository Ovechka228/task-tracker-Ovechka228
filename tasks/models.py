from django.db import models
from django.urls import reverse


class Task(models.Model):
    STATUS_CHOICES = (
        ('to_do', 'До виконання'),
        ('in_progress', 'В процесі'),
        ('done', 'Виконано'),
        ('suspended', 'Відкладено'),
    )

    PRIORITY_CHOICES = (
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', 'Високий'),
    )

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    desc = models.TextField(max_length=1500, verbose_name='Опис')
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default='to_do', verbose_name='Статус'
    )
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default='medium', verbose_name='Пріоритет'
    )
    due_to = models.DateTimeField(verbose_name='Дедлайн')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks:task-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачі'
        ordering = ['due_to', 'created_at']
