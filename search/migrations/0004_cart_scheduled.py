# Generated by Django 4.1.6 on 2023-04-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='scheduled',
            field=models.BooleanField(default=False),
        ),
    ]
