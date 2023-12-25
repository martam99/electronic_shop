from django.db import models


# Create your models here.


class Supplier(models.Model):
    fullname = models.CharField(max_length=150, verbose_name='Поставщик')
    mail = models.EmailField(max_length=150, verbose_name='почта')
    phone = models.CharField(max_length=150, verbose_name='номер телефона')

    objects = models.Manager()

    def __str__(self):
        return f'{self.fullname}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
