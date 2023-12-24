from django.db import models
from django.utils.timezone import now

from SP.models import SP
from factory.models import Factory
from supplier.models import Supplier


# Create your models here.
class Retail(models.Model):
    company_name = models.CharField(max_length=150, verbose_name='название компании')
    sp = models.ForeignKey(SP, on_delete=models.CASCADE, verbose_name='ИП')
    opened_date = models.DateField(verbose_name='Дата создания', default=now)
    factory = models.ForeignKey(Factory, on_delete=models.DO_NOTHING, verbose_name='Завод')

    objects = models.Manager()

    def __str__(self):
        return f'{self.company_name}'

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'


class Store(models.Model):
    company_name = models.ForeignKey(Retail, on_delete=models.CASCADE, verbose_name='компания')
    store_name = models.CharField(max_length=150, verbose_name='название магазина')
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, verbose_name='поставщик')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Задолженность перед поставщиком в RUB')
    creating_date = models.DateTimeField(verbose_name='дата создания', default=now)

    objects = models.Manager()

    def __str__(self):
        return f'{self.store_name}'

    class Meta:
        verbose_name = 'магазин'
        verbose_name_plural = 'магазины'


class Contacts(models.Model):
    mail = models.EmailField(max_length=150, verbose_name='почта')
    country = models.CharField(max_length=150, verbose_name='страна')
    city = models.CharField(max_length=150, verbose_name='город')
    street = models.CharField(max_length=150, verbose_name='улица')
    house_num = models.CharField(max_length=150, verbose_name='номер дома')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='магазин')

    objects = models.Manager()

    def __str__(self):
        return f'{self.mail}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name='продукт')
    model = models.CharField(max_length=150, verbose_name='модель')
    to_market_date = models.DateField(verbose_name='Дата выхода на рынок')
    store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name='магазин')

    objects = models.Manager()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
