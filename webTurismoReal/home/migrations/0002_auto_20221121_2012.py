# Generated by Django 3.2.15 on 2022-11-21 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conductor',
            name='status',
            field=models.CharField(choices=[('1', 'Activo'), ('2', 'Inactivo')], default='1', max_length=13),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='status',
            field=models.CharField(choices=[('1', 'Activa'), ('2', 'Cancelada'), ('3', 'Terminada')], default='1', max_length=12),
        ),
    ]
