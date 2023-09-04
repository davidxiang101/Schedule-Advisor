# Generated by Django 4.1.6 on 2023-04-16 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_cart_scheduled'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('catalog_nbr', models.IntegerField()),
                ('descr', models.CharField(max_length=200)),
                ('days', models.CharField(max_length=200)),
                ('start_time', models.CharField(max_length=200)),
                ('end_time', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]