# Generated by Django 3.2 on 2024-03-28 12:55

import uuid

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cashback',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Сумма')),
                ('status', models.CharField(choices=[('expected', 'ожидается'), ('accrued', 'начислен')], default='ожидается', max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=100, verbose_name='Текст сообщения')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата сообщения')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Сумма')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата платежа')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('titel', models.IntegerField(verbose_name='Тариф')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Стоимость')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('url', models.URLField(verbose_name='Адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='Название подписки')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('refund', models.DecimalField(decimal_places=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_beginning', models.DateTimeField(auto_now_add=True, verbose_name='Дата начала')),
                ('date_ending', models.DateTimeField(verbose_name='Дата окончания')),
                ('status', models.CharField(choices=[('active', 'активная'), ('inactive', 'не активна')], default='active', max_length=8)),
                ('cashback', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cashback', to='pay2u.cashback', verbose_name='Кэшбэка')),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='notification', to='pay2u.notification', verbose_name='Сообщения')),
                ('payments', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payments', to='pay2u.payments', verbose_name='Платежи')),
                ('subscription', models.ManyToManyField(related_name='subscription', to='pay2u.Subscription', verbose_name='Подписка')),
            ],
        ),
    ]