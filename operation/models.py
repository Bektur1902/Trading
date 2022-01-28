from django.db import models

# Create your models here.


class Company(models.Model):

    title = models.CharField('Название компании', max_length=100)
    manager_name = models.CharField('Имя директора', max_length=50)
    manager_second_name = models.CharField('Фамилия директора', max_length=50)
    manger_last_name = models.CharField('Отчество директора', max_length=50)
    company_adress = models.CharField('Юредический адресс', max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):

    title = models.CharField('Наименование товара', max_length=100)
    product_unit_measure = models.CharField('Единица измерения', max_length=20)
    payment_account = models.ForeignKey('PaymentAccount', on_delete=models.DO_NOTHING, verbose_name='Расчетный счет')

    def __str__(self):
        return self.title


class Sales(models.Model):

    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount = models.DecimalField('Количество', max_digits=5, decimal_places=0)
    sold_date = models.DateTimeField('Дата продажи', auto_now_add=True)

    def __str__(self):
        return self.product


class Price(models.Model):

    price = models.IntegerField('Цена', blank=True)

    def __str__(self):
        return self.price


class ProductPrice(models.Model):

    product = models.ManyToManyField(Product, blank=True)
    price = models.ManyToManyField(Price, blank=True)


class PaymentAccount(models.Model):

    payment_account = models.CharField('Расчетный счет', max_length=100)

    def __str__(self):
        return self.payment_account


class Purchases(models.Model):

    company = models.ManyToManyField(Company)
    product = models.ManyToManyField(Product)
    payment = models.ManyToManyField(PaymentAccount)