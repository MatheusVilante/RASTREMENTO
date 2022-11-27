# Generated by Django 4.1.2 on 2022-10-31 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=255, verbose_name='Sobrenome')),
                ('cpf', models.IntegerField(unique=True, verbose_name='CPF')),
                ('estado', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], default='PB', max_length=100, verbose_name='Estado')),
                ('cidade', models.CharField(max_length=255, verbose_name='Cidade')),
                ('rua', models.CharField(max_length=255, verbose_name='Rua')),
                ('numero', models.CharField(max_length=255, verbose_name='Número')),
                ('complemento', models.CharField(max_length=255, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=255, verbose_name='Bairro')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'unique_together': {('cpf',)},
            },
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veiculo', models.CharField(max_length=255, verbose_name='Veículo (Marca/Modelo)')),
                ('ano', models.IntegerField(verbose_name='Ano do veículo')),
                ('placa', models.CharField(max_length=255, verbose_name='Placa')),
                ('renavam', models.CharField(max_length=255, verbose_name='Renavam')),
                ('chassi', models.CharField(max_length=255, verbose_name='Chassi')),
                ('cor', models.CharField(max_length=255, verbose_name='Cor')),
                ('Cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clienteveiculo', to='Cliente.cliente', verbose_name='cliente')),
            ],
            options={
                'verbose_name': 'Veículo',
                'verbose_name_plural': 'Veículos',
            },
        ),
    ]
