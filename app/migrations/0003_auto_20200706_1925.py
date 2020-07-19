# Generated by Django 2.2.4 on 2020-07-06 22:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tarefa_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='data_expiracao',
            new_name='data_registro',
        ),
        migrations.RemoveField(
            model_name='tarefa',
            name='titulo',
        ),
        migrations.AddField(
            model_name='tarefa',
            name='origem',
            field=models.CharField(default=2344535, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarefa',
            name='tipo',
            field=models.CharField(choices=[('P', 'Produção'), ('H', 'Homologação'), ('D', 'Dev')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='descricao',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='prioridade',
            field=models.CharField(choices=[('A', 'All'), ('D', 'Debug'), ('I', 'Info'), ('W', 'Warning'), ('E', 'Error'), ('F', 'Fatal'), ('O', 'Off'), ('T', 'Trace')], max_length=1),
        ),
    ]
