# Generated by Django 3.0.6 on 2020-11-11 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loja',
            name='cadastrada',
            field=models.BooleanField(default=False),
        ),
    ]
