from django.db import models


# Create your models here.
class Factory(models.Model):
    title = models.CharField(max_length=150, verbose_name='название завода')
    head = models.CharField(max_length=150, verbose_name='руководитель')
    address = models.CharField(max_length=150, verbose_name='адрес')
    phone = models.CharField(max_length=150, verbose_name='телефон')
    fax = models.CharField(max_length=150, verbose_name='факс')
    mail = models.EmailField(max_length=150, verbose_name='почта')
    production = models.TextField(verbose_name='продукция')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'
