# Generated by Django 4.1.2 on 2022-11-04 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Servico', '0003_remove_servico_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='Pagamento',
        ),
    ]
