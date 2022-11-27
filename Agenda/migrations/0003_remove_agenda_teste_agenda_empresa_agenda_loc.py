# Generated by Django 4.1.2 on 2022-10-30 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Empresa', '0002_alter_empresa_cnpj'),
        ('Agenda', '0002_alter_agenda_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='teste',
        ),
        migrations.AddField(
            model_name='agenda',
            name='Empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empresaagenda', to='Empresa.empresa', verbose_name='empresa'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='loc',
            field=models.CharField(default='Recife', max_length=255, verbose_name='localização'),
            preserve_default=False,
        ),
    ]
