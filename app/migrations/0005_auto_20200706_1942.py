# Generated by Django 2.2.4 on 2020-07-06 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200706_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='data_registro',
            field=models.DateField(),
        ),
    ]