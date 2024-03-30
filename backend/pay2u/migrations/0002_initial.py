# Generated by Django 3.2 on 2024-03-28 12:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pay2u', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubscription',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='rate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pay2u.rate', verbose_name='Тариф'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pay2u.services', verbose_name='Сервис'),
        ),
    ]