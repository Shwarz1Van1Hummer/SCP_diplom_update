from django.db import models


class News(models.Model):
    title_new = models.CharField(max_length=255)
    description = models.CharField(max_length=8000)
    date = models.DateTimeField("Время создания", auto_now_add=True)

    def __str__(self):
        return f'Название новости: {self.title_new}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = "Новости"
