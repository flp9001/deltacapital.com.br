# Generated by Django 3.0.6 on 2020-08-30 19:30
import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="PropostaPorto",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                ("simulado_em", models.DateTimeField(blank=True, null=True)),
                ("enviado_em", models.DateTimeField(blank=True, null=True)),
                ("modificado_em", models.DateTimeField(auto_now=True)),
                (
                    "session_hash",
                    models.CharField(
                        max_length=40, unique=True, verbose_name="Código Interno"
                    ),
                ),
                (
                    "stage",
                    models.CharField(
                        default="1", max_length=10, verbose_name="Estágio"
                    ),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Não simulado"),
                            (2, "Erro"),
                            (3, "Pre Recusado"),
                            (4, "Em Digitação"),
                        ],
                        default=1,
                        verbose_name="Status",
                    ),
                ),
                (
                    "valores_parcelas",
                    models.CharField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="Valores das parcelas",
                    ),
                ),
                (
                    "pre_aprovado",
                    models.CharField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="Crédito pre-aprovado",
                    ),
                ),
                (
                    "valor_do_veiculo",
                    models.CharField(
                        blank=True,
                        help_text="<h2>Veículo</h2><h3>Preencha os dados do financiamento</h3>",
                        max_length=20,
                        verbose_name="Valor do Veículo",
                    ),
                ),
                (
                    "valor_de_entrada",
                    models.CharField(
                        blank=True, max_length=20, verbose_name="Valor de Entrada"
                    ),
                ),
                (
                    "cpf",
                    models.CharField(
                        blank=True,
                        help_text="<h2>Cliente</h2><h3>Preencha com o CPF do seu Cliente</h3>",
                        max_length=20,
                        verbose_name="CPF",
                    ),
                ),
                (
                    "prazo",
                    models.CharField(
                        choices=[
                            ("12", "12x"),
                            ("24", "24x"),
                            ("36", "36x"),
                            ("48", "48x"),
                            ("60", "60x"),
                        ],
                        help_text="Selecione a melhor opção para seu cliente.",
                        max_length=3,
                        verbose_name="Cotação de Financiamento",
                    ),
                ),
                (
                    "nome",
                    models.CharField(blank=True, max_length=100, verbose_name="Nome"),
                ),
                (
                    "data_de_nascimento",
                    models.DateField(
                        blank=True, null=True, verbose_name="Data de Nascimento"
                    ),
                ),
                (
                    "sexo",
                    models.CharField(
                        blank=True,
                        choices=[("Masculino", "Masculino"), ("Feminino", "Feminino")],
                        max_length=100,
                        verbose_name="Sexo",
                    ),
                ),
                (
                    "numero_do_rg",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Número do RG"
                    ),
                ),
                (
                    "orgao_expedidor",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Órgão Expedidor"
                    ),
                ),
                (
                    "nome_da_mae",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Nome da Mãe"
                    ),
                ),
                (
                    "local_de_nascimento",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Local de Nascimento"
                    ),
                ),
                (
                    "uf_de_nascimento",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AC", "AC"),
                            ("AL", "AL"),
                            ("AP", "AP"),
                            ("AM", "AM"),
                            ("BA", "BA"),
                            ("CE", "CE"),
                            ("DF", "DF"),
                            ("ES", "ES"),
                            ("GO", "GO"),
                            ("MA", "MA"),
                            ("MT", "MT"),
                            ("MS", "MS"),
                            ("MG", "MG"),
                            ("PA", "PA"),
                            ("PB", "PB"),
                            ("PR", "PR"),
                            ("PE", "PE"),
                            ("PI", "PI"),
                            ("RJ", "RJ"),
                            ("RN", "RN"),
                            ("RS", "RS"),
                            ("RO", "RO"),
                            ("RR", "RR"),
                            ("SC", "SC"),
                            ("SP", "SP"),
                            ("SE", "SE"),
                            ("TO", "TO"),
                        ],
                        max_length=2,
                        verbose_name="UF de Nascimento",
                    ),
                ),
                (
                    "cep",
                    models.CharField(blank=True, max_length=100, verbose_name="CEP"),
                ),
                (
                    "endereco",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Endereço (Rua/Avenida/Alameda)",
                    ),
                ),
                (
                    "numero",
                    models.CharField(blank=True, max_length=100, verbose_name="Número"),
                ),
                (
                    "complemento",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Complemento"
                    ),
                ),
                (
                    "bairro",
                    models.CharField(blank=True, max_length=100, verbose_name="Bairro"),
                ),
                (
                    "cidade",
                    models.CharField(blank=True, max_length=100, verbose_name="Cidade"),
                ),
                (
                    "uf",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AC", "AC"),
                            ("AL", "AL"),
                            ("AP", "AP"),
                            ("AM", "AM"),
                            ("BA", "BA"),
                            ("CE", "CE"),
                            ("DF", "DF"),
                            ("ES", "ES"),
                            ("GO", "GO"),
                            ("MA", "MA"),
                            ("MT", "MT"),
                            ("MS", "MS"),
                            ("MG", "MG"),
                            ("PA", "PA"),
                            ("PB", "PB"),
                            ("PR", "PR"),
                            ("PE", "PE"),
                            ("PI", "PI"),
                            ("RJ", "RJ"),
                            ("RN", "RN"),
                            ("RS", "RS"),
                            ("RO", "RO"),
                            ("RR", "RR"),
                            ("SC", "SC"),
                            ("SP", "SP"),
                            ("SE", "SE"),
                            ("TO", "TO"),
                        ],
                        max_length=2,
                        verbose_name="UF",
                    ),
                ),
                (
                    "telefone_fixo",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Telefone Fixo"
                    ),
                ),
                (
                    "celular",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Celular"
                    ),
                ),
                (
                    "email",
                    models.CharField(blank=True, max_length=100, verbose_name="Email"),
                ),
                (
                    "tipo_de_renda",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("assalariado", "assalariado"),
                            ("autonomo", "autonomo"),
                            ("empresario", "empresario"),
                            ("aposentado", "aposentado"),
                        ],
                        help_text="<h2>Informe a renda do seu cliente</h2><h3>Essas informações são essenciais para análise de crédito do financiamento</h3>",
                        max_length=100,
                        verbose_name="Tipo de Renda",
                    ),
                ),
                (
                    "renda_mensal_pessoal",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Renda Mensal Pessoal"
                    ),
                ),
                (
                    "profissao_assalariado",
                    models.CharField(
                        blank=True,
                        choices=[
                            (
                                "ADMINISTRADORES / ECONOMISTAS",
                                "ADMINISTRADORES / ECONOMISTAS",
                            ),
                            ("ANALISTAS", "ANALISTAS"),
                            ("CONSULTOR", "CONSULTOR"),
                            ("DIRETOR DE EMPRESA", "DIRETOR DE EMPRESA"),
                            (
                                "FUNCIONÁRIO DE EMPRESAS PUBLICAS",
                                "FUNCIONÁRIO DE EMPRESAS PUBLICAS",
                            ),
                            ("GERENTE", "GERENTE"),
                            ("OPERADOR EM GERAL", "OPERADOR EM GERAL"),
                            (
                                "OUTRAS PROFISSÕES DA INDUSTRIA",
                                "OUTRAS PROFISSÕES DA INDUSTRIA",
                            ),
                            (
                                "OUTRAS PROFISSÕES NO COMÉRCIO",
                                "OUTRAS PROFISSÕES NO COMÉRCIO",
                            ),
                            ("PROFESSORES", "PROFESSORES"),
                            ("PROMOTOR", "PROMOTOR"),
                            (
                                "VENDEDORES / REPRESENTANTES / INTERMEDIÁRIOS",
                                "VENDEDORES / REPRESENTANTES / INTERMEDIÁRIOS",
                            ),
                            ("OUTROS", "OUTROS"),
                        ],
                        max_length=100,
                        verbose_name="Profissão",
                    ),
                ),
                (
                    "profissao_liberal",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ADVOGADOS", "ADVOGADOS"),
                            ("ARQUITETOS", "ARQUITETOS"),
                            ("ENGENHEIROS", "ENGENHEIROS"),
                            (
                                "MÉDICOS E CIRURGIÕES DENTISTAS",
                                "MÉDICOS E CIRURGIÕES DENTISTAS",
                            ),
                            ("PROFESSORES", "PROFESSORES"),
                            ("OUTROS", "OUTROS"),
                        ],
                        max_length=100,
                        verbose_name="Profissão",
                    ),
                ),
                (
                    "cep_da_empresa",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="CEP da Empresa"
                    ),
                ),
                (
                    "endereco_comercial",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Endereço Comercial"
                    ),
                ),
                (
                    "numero_empresa",
                    models.CharField(blank=True, max_length=100, verbose_name="Número"),
                ),
                (
                    "complemento_empresa",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Complemento"
                    ),
                ),
                (
                    "bairro_empresa",
                    models.CharField(blank=True, max_length=100, verbose_name="Bairro"),
                ),
                (
                    "cidade_empresa",
                    models.CharField(blank=True, max_length=100, verbose_name="Cidade"),
                ),
                (
                    "uf_empresa",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AC", "AC"),
                            ("AL", "AL"),
                            ("AP", "AP"),
                            ("AM", "AM"),
                            ("BA", "BA"),
                            ("CE", "CE"),
                            ("DF", "DF"),
                            ("ES", "ES"),
                            ("GO", "GO"),
                            ("MA", "MA"),
                            ("MT", "MT"),
                            ("MS", "MS"),
                            ("MG", "MG"),
                            ("PA", "PA"),
                            ("PB", "PB"),
                            ("PR", "PR"),
                            ("PE", "PE"),
                            ("PI", "PI"),
                            ("RJ", "RJ"),
                            ("RN", "RN"),
                            ("RS", "RS"),
                            ("RO", "RO"),
                            ("RR", "RR"),
                            ("SC", "SC"),
                            ("SP", "SP"),
                            ("SE", "SE"),
                            ("TO", "TO"),
                        ],
                        max_length=2,
                        verbose_name="UF",
                    ),
                ),
                (
                    "inicio_da_atividade",
                    models.DateField(
                        blank=True, null=True, verbose_name="Início da Atividade"
                    ),
                ),
                (
                    "telefone_fixo_da_empresa",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Telefone Fixo da Empresa",
                    ),
                ),
                (
                    "tempo_de_empresa",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Tempo de Empresa (anos)",
                    ),
                ),
                (
                    "razao_social_da_empresa",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Razão Social da Empresa",
                    ),
                ),
                (
                    "cnpj_da_empresa",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="CNPJ da empresa"
                    ),
                ),
                (
                    "tempo_de_atividade",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Tempo de Atividade"
                    ),
                ),
                (
                    "tempo_de_aposentadoria",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="Tempo de Aposentadoria",
                    ),
                ),
                (
                    "outras_rendas",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Outras Rendas"
                    ),
                ),
                (
                    "ano_de_fabricacao",
                    models.CharField(
                        blank=True,
                        help_text="<h2>Informações sobre o Veículo</h2><p>Caso seu cliente não saiba extamente qual veículo irá comprar, indique algum compatível em termos de preço. Fique tranquilo, você poderá mudar essa informação a qualquer momento.</p>",
                        max_length=100,
                        verbose_name="Ano de Fabricação",
                    ),
                ),
                (
                    "ano_do_modelo",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Ano do Modelo"
                    ),
                ),
                (
                    "marca",
                    models.CharField(blank=True, max_length=100, verbose_name="Marca"),
                ),
                (
                    "modelo",
                    models.CharField(blank=True, max_length=100, verbose_name="Modelo"),
                ),
                (
                    "versao",
                    models.CharField(blank=True, max_length=100, verbose_name="Versão"),
                ),
                (
                    "cor",
                    models.CharField(blank=True, max_length=100, verbose_name="Cor"),
                ),
                (
                    "combustivel",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Gasolina/Alcool/Flex", "Gasolina/Alcool/Flex"),
                            ("Diesel", "Diesel"),
                        ],
                        max_length=100,
                        verbose_name="Combustível",
                    ),
                ),
                (
                    "cambio",
                    models.CharField(
                        blank=True,
                        choices=[("Manual", "Manual"), ("Automatico", "Automático")],
                        max_length=100,
                        verbose_name="Câmbio",
                    ),
                ),
                (
                    "motor",
                    models.CharField(blank=True, max_length=100, verbose_name="Motor"),
                ),
                (
                    "dados_placa",
                    models.CharField(
                        blank=True,
                        choices=[("Sim", "Sim"), ("Não", "Não")],
                        max_length=100,
                        verbose_name="VOCÊ POSSUI OS DADOS DE PLACA / CHASSI / RENAVAM DESTE VEÍCULO?",
                    ),
                ),
                (
                    "placa",
                    models.CharField(blank=True, max_length=100, verbose_name="Placa"),
                ),
                (
                    "renavam",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Renavam"
                    ),
                ),
                (
                    "chassi",
                    models.CharField(blank=True, max_length=100, verbose_name="Chassi"),
                ),
                (
                    "nome_operador",
                    models.CharField(
                        blank=True, max_length=100, verbose_name="Nome do Operador"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuário",
                    ),
                ),
            ],
            options={
                "verbose_name": "Proposta Porto Seguro",
                "verbose_name_plural": "Propostas Porto Seguro",
            },
        )
    ]
