# Generated by Django 3.2.15 on 2022-10-17 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_reserva_total_reserva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='total_reserva',
            field=models.IntegerField(default=0),
        ),
    ]
