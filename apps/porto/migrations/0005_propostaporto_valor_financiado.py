# Generated by Django 3.0.6 on 2021-03-09 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porto', '0004_propostaporto_mensagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='propostaporto',
            name='valor_financiado',
            field=models.CharField(blank=True, max_length=20, verbose_name='Valor Financiado'),
        ),
    ]
