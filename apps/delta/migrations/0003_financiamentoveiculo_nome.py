# Generated by Django 3.0.6 on 2021-02-23 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0002_auto_20210216_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='financiamentoveiculo',
            name='nome',
            field=models.CharField(max_length=300, null=True, verbose_name='Nome'),
        ),
    ]
