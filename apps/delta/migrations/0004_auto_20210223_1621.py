# Generated by Django 3.0.6 on 2021-02-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0003_financiamentoveiculo_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financiamentoveiculo',
            name='ano',
            field=models.PositiveSmallIntegerField(default=2010, max_length=4),
        ),
    ]
