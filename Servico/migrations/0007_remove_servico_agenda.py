# Generated by Django 4.1.2 on 2022-11-04 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Servico', '0006_servico_agenda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='Agenda',
        ),
    ]
