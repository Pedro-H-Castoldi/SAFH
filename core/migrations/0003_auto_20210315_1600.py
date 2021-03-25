# Generated by Django 3.1.7 on 2021-03-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210315_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='birth_date',
            field=models.DateField(blank=True, verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='consultation_date',
            field=models.DateField(blank=True, verbose_name='Data da consulta'),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='sus',
            field=models.CharField(blank=True, max_length=15, verbose_name='Número do SUS'),
        ),
    ]
