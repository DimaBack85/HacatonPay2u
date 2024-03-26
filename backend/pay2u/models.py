import uuid

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import CustomUser

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class Rate(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        editable=False, 
        default=uuid.uuid4, 
        unique=True,
    )
    titel = models.IntegerField(
        verbose_name='Тариф',
    )
    price = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        verbose_name='Стоимость'
    )


class Services(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        editable=False, 
        default=uuid.uuid4, 
        unique=True,
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=50,
        blank=False,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    url = models.URLField(
        verbose_name='Адрес',
        blank=False
    )


class Subscription(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        editable=False, 
        default=uuid.uuid4, 
        unique=True,
    )
    service = models.ForeignKey(
        'Services',
        verbose_name='Сервис',
        on_delete=models.CASCADE,
    )
    rate = models.ForeignKey(
        'Rate',
        verbose_name='Тариф',
        on_delete=models.PROTECT
    )
    name = models.CharField(
        verbose_name='Название подписки',
        max_length=50,
        blank=False,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    refund = models.DecimalField(
        max_digits=2,
        decimal_places=0,
        validators=PERCENTAGE_VALIDATOR
    )


class Cashback(models.Model):
    STATUS_CASHBACK = (
        ('expected','ожидается'),
        ('accrued', 'начислен'),
    )

    id = models.UUIDField(
        primary_key=True, 
        editable=False, 
        default=uuid.uuid4, 
        unique=True,
    )
    amount = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        verbose_name='Сумма'
    )
    status = models.CharField(
        max_length=9, 
        choices=STATUS_CASHBACK, 
        default='ожидается'
    )


class Payments(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        editable=False, 
        default=uuid.uuid4, 
        unique=True,
    )
    amount = models.DecimalField(
        max_digits=6, 
        decimal_places=2,
        verbose_name='Сумма',
    )
    datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата платежа',
    )


class Notification(models.Model):
    id = models.UUIDField(
        primary_key=True, 
        editable=False, 
        default=uuid.uuid4, 
        unique=True,
    ),
    text = models.TextField(
        max_length=100,
        verbose_name='Текст сообщения',
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата сообщения',
    )


class UserSubscription(models.Model):
    STATUS_SUB = (
        ('active', 'активная'),
        ('inactive', 'не активна'),
    ) 

    subscription = models.ManyToManyField(
        'Subscription',
        verbose_name='Подписка',
        related_name='subscription',
    )
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    date_beginning = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата начала',
    )
    date_ending = models.DateTimeField(
        verbose_name='Дата окончания',
    )
    status = models.CharField(
        max_length=8, 
        choices=STATUS_SUB, 
        default='active',
    )
    cashback = models.ForeignKey(
        'Cashback',
        on_delete=models.PROTECT,
        verbose_name='Кэшбэка',
        related_name='cashback',
    )
    payments = models.ForeignKey(
        'Payments',
        on_delete=models.PROTECT,
        verbose_name='Платежи',
        related_name='payments',
    )
    notification = models.ForeignKey(
        'Notification',
        on_delete=models.PROTECT,
        verbose_name='Сообщения',
        related_name='notification',
    )
