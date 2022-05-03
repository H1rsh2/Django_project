from django.db import models


class Status(models.Model):
    status_name = models.CharField(max_length=50, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Dish(models.Model):
    name_dish = models.CharField(max_length=50, verbose_name='Название блюда')
    value_dish = models.IntegerField(verbose_name='Количество заказанных блюд')

    def __str__(self):
        return self.name_dish

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class Type(models.Model):
    type_product = models.CharField(max_length=50, verbose_name='Название типа продукции')

    def __str__(self):
        return self.type_product

    class Meta:
        verbose_name = 'Тип продукции'
        verbose_name_plural = 'Тип продукции'


class Food(models.Model):
    food = models.CharField('Продукт', max_length=50)
    food_type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True,  verbose_name="Тип продукции")
    storage = models.IntegerField(verbose_name='Срок хранения')

    def __str__(self):
        return self.food

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Ingredient(models.Model):
    ingredient_dish = models.ForeignKey(Dish, on_delete=models.PROTECT, null=True, blank=True,  verbose_name="Выберите блюдо")
    ingredient_food = models.ForeignKey(Food, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Выберите продукт")
    ingredient_storage = models.IntegerField(verbose_name='Количество')

    def __int__(self):
        return self.ingredient_storage

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class Provider(models.Model):
    name = models.CharField('Название организации',  max_length=50)
    type = models.ForeignKey(Type, on_delete=models.PROTECT, null=True, blank=True,  verbose_name="Тип продуктов")
    inn = models.CharField('ИНН', max_length=12)
    kpp = models.CharField('ОГРН', max_length=15)
    mail = models.EmailField('Почта')
    phone = models.CharField('Номер телефона', max_length=12)
    address = models.TextField('Адрес')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщика'
        verbose_name_plural = 'Поставщики'


class Stock(models.Model):
    name_stock = models.CharField('Название говна', max_length=15)
    title = models.ForeignKey(Provider, on_delete=models.PROTECT, null=True, blank=True,  verbose_name="Поставщик")
    stock = models.ManyToManyField(Food, verbose_name="Продукты", help_text="Выберите продукт для этой поставки")
    stock_status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True, blank=True, verbose_name="Статус")
    dt = models.DateField('Дата поставки', null=True, blank = True)

    def __str__(self):
        return self.name_stock

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'