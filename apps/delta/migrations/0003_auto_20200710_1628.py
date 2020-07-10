# Generated by Django 3.0.6 on 2020-07-10 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0002_proposta_bairro_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposta',
            name='cpf',
            field=models.CharField(blank=True, help_text='<h2>Cliente</h2><h3>Preencha com o CPF do seu Cliente</h3>', max_length=20, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='endereco',
            field=models.CharField(blank=True, max_length=100, verbose_name='Endereço (Rua/Avenida/Alameda)'),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='prazo',
            field=models.CharField(choices=[('12x', '12x'), ('24x', '24x'), ('36x', '36x'), ('48x', '48x'), ('60x', '60x')], max_length=3, verbose_name='Prazo'),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='profissao',
            field=models.CharField(blank=True, choices=[('ADMINISTRADORES / ECONOMISTAS', 'ADMINISTRADORES / ECONOMISTAS'), ('ANALISTAS', 'ANALISTAS'), ('CONSULTOR', 'CONSULTOR'), ('DIRETOR DE EMPRESA', 'DIRETOR DE EMPRESA'), ('FUNCIONÁRIO DE EMPRESAS PUBLICAS', 'FUNCIONÁRIO DE EMPRESAS PUBLICAS'), ('GERENTE', 'GERENTE'), ('OPERADOR EM GERAL', 'OPERADOR EM GERAL'), ('OUTRAS PROFISSÕES DA INDUSTRIA', 'OUTRAS PROFISSÕES DA INDUSTRIA'), ('OUTRAS PROFISSÕES NO COMÉRCIO', 'OUTRAS PROFISSÕES NO COMÉRCIO'), ('PROFESSORES', 'PROFESSORES'), ('PROMOTOR', 'PROMOTOR'), ('VENDEDORES / REPRESENTANTES / INTERMEDIÁRIOS', 'VENDEDORES / REPRESENTANTES / INTERMEDIÁRIOS'), ('OUTROS', 'OUTROS')], max_length=100, verbose_name='Profissão'),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='tipo_de_renda',
            field=models.CharField(blank=True, choices=[('assalariado', 'assalariado'), ('autonomo', 'autonomo'), ('empresario', 'empresario'), ('aposentado', 'aposentado')], max_length=100, verbose_name='Tipo de Renda'),
        ),
        migrations.AlterField(
            model_name='proposta',
            name='valor_do_veiculo',
            field=models.CharField(blank=True, help_text='<h2>Veículo</h2><h3>Preencha os dados do financiamento</h3>', max_length=20, verbose_name='Valor do Veículo'),
        ),
    ]
