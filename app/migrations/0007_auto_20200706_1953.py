# Generated by Django 2.2.4 on 2020-07-06 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200706_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='data_registro',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='eventos',
            field=models.BigIntegerField(),
        ),
    ]
