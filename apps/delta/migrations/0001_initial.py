# Generated by Django 3.0.6 on 2020-08-11 21:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CapitalGiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300, verbose_name='Nome completo')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=300, verbose_name='Telefone')),
                ('prazo', models.PositiveSmallIntegerField(help_text='1x a 24x', validators=[django.core.validators.MaxValueValidator(24)], verbose_name='Prazo')),
                ('cnpj', models.CharField(max_length=100, verbose_name='CNPJ')),
                ('faturamento_anual', models.CharField(choices=[('200-500', '200 mil - 500 mil'), ('500-1', '500 mil - 1 milhão'), ('1-2', '1 milhão - 2 milhões'), ('2-5', '2 milhões - 5 milhões'), ('5-10', '5 milhões - 10 milhões'), ('10-20', '10 milhões - 20 milhões'), ('20-30', '20 milhões - 30 milhões'), ('30-50', '30 milhões - 50 milhões'), ('50-', 'acima de 50 milhões')], max_length=100, verbose_name='Faturamento anual da empresa')),
                ('valor_emprestimo', models.CharField(help_text='Máximo de 800 mil', max_length=100, verbose_name='Valor do emprestimo')),
            ],
            options={
                'verbose_name': 'Capital de Giro',
                'verbose_name_plural': 'Capitais de Giro',
            },
        ),
        migrations.CreateModel(
            name='CartaoCredito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=254, verbose_name='Nome completo')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=50, verbose_name='Telefone')),
                ('cpf', models.CharField(max_length=100, verbose_name='CPF')),
                ('pessoa', models.CharField(choices=[('fisica', 'Pessoa Física'), ('juridica', 'Pessoa Jurídica')], max_length=100, verbose_name='Pessoa')),
                ('bandeira', models.CharField(choices=[('visa', 'Visa'), ('master', 'Master')], max_length=100, verbose_name='Bandeira')),
                ('sexo', models.CharField(choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')], max_length=100, verbose_name='Sexo')),
                ('data_de_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('nome_mae', models.CharField(max_length=254, verbose_name='Nome da mãe')),
                ('endereco', models.CharField(max_length=254, verbose_name='Endereço Residencial')),
                ('cep', models.CharField(max_length=12, verbose_name='CEP')),
                ('vencimento', models.CharField(choices=[('1', '1'), ('5', '5'), ('10', '10'), ('15', '15'), ('20', '20'), ('25', '25'), ('30', '30')], max_length=2, verbose_name='Dia do Vencimento')),
            ],
            options={
                'verbose_name': 'Cartão de Crédito',
                'verbose_name_plural': 'Cartões de Crédito',
            },
        ),
        migrations.CreateModel(
            name='FinanciamentoVeiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_do_veiculo', models.CharField(max_length=100, verbose_name='Valor do Veículo')),
                ('entrada', models.CharField(max_length=100, verbose_name='Valor de Entrada')),
                ('cpf', models.CharField(max_length=100, verbose_name='CPF')),
                ('telefone', models.CharField(max_length=100, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'Financiamento de Veículo',
                'verbose_name_plural': 'Financiamentos de Veículos',
            },
        ),
        migrations.CreateModel(
            name='Proposta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('simulado_em', models.DateTimeField(blank=True, null=True)),
                ('enviado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(auto_now=True)),
                ('session_hash', models.CharField(max_length=40, unique=True, verbose_name='Código Interno')),
                ('stage', models.CharField(default='1', max_length=10, verbose_name='Estágio')),
                ('valores_parcelas', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Valores das parcelas')),
                ('valor_do_veiculo', models.CharField(blank=True, help_text='<h2>Veículo</h2><h3>Preencha os dados do financiamento</h3>', max_length=20, verbose_name='Valor do Veículo')),
                ('valor_de_entrada', models.CharField(blank=True, max_length=20, verbose_name='Valor de Entrada')),
                ('cpf', models.CharField(blank=True, help_text='<h2>Cliente</h2><h3>Preencha com o CPF do seu Cliente</h3>', max_length=20, verbose_name='CPF')),
                ('prazo', models.CharField(choices=[('12', '12x'), ('24', '24x'), ('36', '36x'), ('48', '48x'), ('60', '60x')], max_length=3, verbose_name='Prazo')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('data_de_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=100, verbose_name='Sexo')),
                ('numero_do_rg', models.CharField(blank=True, max_length=100, verbose_name='Número do RG')),
                ('orgao_expedidor', models.CharField(blank=True, max_length=100, verbose_name='Órgão Expedidor')),
                ('nome_da_mae', models.CharField(blank=True, max_length=100, verbose_name='Nome da Mãe')),
                ('local_de_nascimento', models.CharField(blank=True, max_length=100, verbose_name='Local de Nascimento')),
                ('uf_de_nascimento', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=2, verbose_name='UF de Nascimento')),
                ('cep', models.CharField(blank=True, max_length=100, verbose_name='CEP')),
                ('endereco', models.CharField(blank=True, max_length=100, verbose_name='Endereço (Rua/Avenida/Alameda)')),
                ('numero', models.CharField(blank=True, max_length=100, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('bairro', models.CharField(blank=True, max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, max_length=100, verbose_name='Cidade')),
                ('uf', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=2, verbose_name='UF')),
                ('telefone_fixo', models.CharField(blank=True, max_length=100, verbose_name='Telefone Fixo')),
                ('celular', models.CharField(blank=True, max_length=100, verbose_name='Celular')),
                ('email', models.CharField(blank=True, max_length=100, verbose_name='Email')),
                ('tipo_de_renda', models.CharField(blank=True, choices=[('assalariado', 'assalariado'), ('autonomo', 'autonomo'), ('empresario', 'empresario'), ('aposentado', 'aposentado')], help_text='<h2>Informe a renda do seu cliente</h2><h3>Essas informações são essenciais para análise de crédito do financiamento</h3>', max_length=100, verbose_name='Tipo de Renda')),
                ('renda_mensal_pessoal', models.CharField(blank=True, max_length=100, verbose_name='Renda Mensal Pessoal')),
                ('profissao_assalariado', models.CharField(blank=True, choices=[('ADMINISTRADORES / ECONOMISTAS', 'ADMINISTRADORES / ECONOMISTAS'), ('ANALISTAS', 'ANALISTAS'), ('CONSULTOR', 'CONSULTOR'), ('DIRETOR DE EMPRESA', 'DIRETOR DE EMPRESA'), ('FUNCIONÁRIO DE EMPRESAS PUBLICAS', 'FUNCIONÁRIO DE EMPRESAS PUBLICAS'), ('GERENTE', 'GERENTE'), ('OPERADOR EM GERAL', 'OPERADOR EM GERAL'), ('OUTRAS PROFISSÕES DA INDUSTRIA', 'OUTRAS PROFISSÕES DA INDUSTRIA'), ('OUTRAS PROFISSÕES NO COMÉRCIO', 'OUTRAS PROFISSÕES NO COMÉRCIO'), ('PROFESSORES', 'PROFESSORES'), ('PROMOTOR', 'PROMOTOR'), ('VENDEDORES / REPRESENTANTES / INTERMEDIÁRIOS', 'VENDEDORES / REPRESENTANTES / INTERMEDIÁRIOS'), ('OUTROS', 'OUTROS')], max_length=100, verbose_name='Profissão')),
                ('profissao_liberal', models.CharField(blank=True, choices=[('ADVOGADOS', 'ADVOGADOS'), ('ARQUITETOS', 'ARQUITETOS'), ('ENGENHEIROS', 'ENGENHEIROS'), ('MÉDICOS E CIRURGIÕES DENTISTAS', 'MÉDICOS E CIRURGIÕES DENTISTAS'), ('PROFESSORES', 'PROFESSORES'), ('OUTROS', 'OUTROS')], max_length=100, verbose_name='Profissão')),
                ('cep_da_empresa', models.CharField(blank=True, max_length=100, verbose_name='CEP da Empresa')),
                ('endereco_comercial', models.CharField(blank=True, max_length=100, verbose_name='Endereço Comercial')),
                ('numero_empresa', models.CharField(blank=True, max_length=100, verbose_name='Número')),
                ('complemento_empresa', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('bairro_empresa', models.CharField(blank=True, max_length=100, verbose_name='Bairro')),
                ('cidade_empresa', models.CharField(blank=True, max_length=100, verbose_name='Cidade')),
                ('uf_empresa', models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=2, verbose_name='UF')),
                ('inicio_da_atividade', models.CharField(blank=True, max_length=100, verbose_name='Início da Atividade')),
                ('telefone_fixo_da_empresa', models.CharField(blank=True, max_length=100, verbose_name='Telefone Fixo da Empresa')),
                ('tempo_de_empresa', models.CharField(blank=True, max_length=100, verbose_name='Tempo de Empresa (anos)')),
                ('razao_social_da_empresa', models.CharField(blank=True, max_length=100, verbose_name='Razão Social da Empresa')),
                ('cnpj_da_empresa', models.CharField(blank=True, max_length=100, verbose_name='CNPJ da empresa')),
                ('tempo_de_atividade', models.CharField(blank=True, max_length=100, verbose_name='Tempo de Atividade')),
                ('tempo_de_aposentadoria', models.CharField(blank=True, max_length=100, verbose_name='Tempo de Aposentadoria')),
                ('outras_rendas', models.CharField(blank=True, max_length=100, verbose_name='Outras Rendas')),
                ('ano_de_fabricacao', models.CharField(blank=True, help_text='Veículo', max_length=100, verbose_name='Ano de Fabricação')),
                ('ano_do_modelo', models.CharField(blank=True, max_length=100, verbose_name='Ano do Modelo')),
                ('marca', models.CharField(blank=True, max_length=100, verbose_name='Marca')),
                ('modelo', models.CharField(blank=True, max_length=100, verbose_name='Modelo')),
                ('versao', models.CharField(blank=True, max_length=100, verbose_name='Versão')),
                ('combustivel', models.CharField(blank=True, max_length=100, verbose_name='Combustível')),
                ('cambio', models.CharField(blank=True, max_length=100, verbose_name='Câmbio')),
                ('motor', models.CharField(blank=True, max_length=100, verbose_name='Motor')),
                ('dados_placa', models.CharField(blank=True, choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=100, verbose_name='VOCÊ POSSUI OS DADOS DE PLACA / CHASSI / RENAVAM DESTE VEÍCULO?')),
                ('placa', models.CharField(blank=True, max_length=100, verbose_name='Placa')),
                ('renavam', models.CharField(blank=True, max_length=100, verbose_name='Renavam')),
                ('chassi', models.CharField(blank=True, max_length=100, verbose_name='Chassi')),
                ('nome_operador', models.CharField(blank=True, max_length=100, verbose_name='Nome do Operador')),
            ],
        ),
    ]
