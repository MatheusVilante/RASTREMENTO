from django.db import models


class Estados(models.Model):
    Acre = 'AC'
    Alagoas = 'AL'
    Amapa = 'AP'
    Amazonas = 'AM'
    Bahia = 'BA'
    Ceara = 'CE'
    Distrito_Federal = 'DF'
    Espirito_Santo = 'ES'
    Goias = 'GO'
    Maranhao = 'MA'
    Mato_Grosso = 'MT'
    Mato_Grosso_do_Sul = 'MS'
    Minas_Gerais = 'MG'
    Para = 'PA'
    Paraiba = 'PB'
    Parana = 'PR'
    Pernambuco = 'PE'
    Piaui = 'PI'
    Rio_de_Janeiro = 'RJ'
    Rio_Grande_do_Sul = 'RS'
    Rondonia = 'RO'
    Roraima = 'RR'
    Santa_Catarina = 'SC'
    Sao_Paulo = 'SP'
    Sergipe = 'SE'
    Tocantins = 'TO'
    STATUS_CHOICES = [
        (Acre, 'AC'),
        (Alagoas, 'AL'),
        (Amapa, 'AP'),
        (Amazonas, 'AM'),
        (Bahia, 'BA'),
        (Ceara, 'CE'),
        (Distrito_Federal, 'DF'),
        (Espirito_Santo, 'ES'),
        (Goias, 'GO'),
        (Maranhao, 'MA'),
        (Mato_Grosso, 'MT'),
        (Mato_Grosso_do_Sul, 'MS'),
        (Minas_Gerais, 'MG'),
        (Para, 'PA'),
        (Paraiba, 'PB'),
        (Parana, 'PR'),
        (Pernambuco, 'PE'),
        (Piaui, 'PI'),
        (Rio_de_Janeiro, 'RJ'),
        (Rio_Grande_do_Sul, 'RS'),
        (Rondonia, 'RO'),
        (Roraima, 'RR'),
        (Santa_Catarina, 'SC'),
        (Sao_Paulo, 'SP'),
        (Sergipe, 'SE'),
        (Tocantins, 'TO'),
    ]


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=255, null=False, blank=False)
    sobrenome = models.CharField('Sobrenome', max_length=255, null=False, blank=False)
    cpf = models.IntegerField('CPF', unique=True, null=False, blank=False)
    estado = models.CharField('Estado', max_length=100, choices=Estados.STATUS_CHOICES, default=Estados.Paraiba, null=False, blank=False)
    cidade = models.CharField('Cidade', max_length=255)
    rua = models.CharField('Rua', max_length=255, null=False, blank=False)
    numero = models.CharField('Número', max_length=255, null=False, blank=False)
    complemento = models.CharField('Complemento', max_length=255, null=False, blank=False)
    bairro = models.CharField('Bairro', max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        unique_together = ['cpf']

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class Veiculo(models.Model):
    Cliente = models.ForeignKey(
        "Cliente.Cliente",
        verbose_name="cliente",
        related_name="clienteveiculo",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    veiculo = models.CharField('Veículo (Marca/Modelo)', max_length=255, null=False, blank=False)
    ano = models.IntegerField('Ano do veículo', null=False, blank=False)
    placa = models.CharField('Placa', max_length=255, null=False, blank=False)
    renavam = models.CharField('Renavam', max_length=255, null=False, blank=False)
    chassi = models.CharField('Chassi', max_length=255, null=False, blank=False)
    cor = models.CharField('Cor', max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Veículo'
        verbose_name_plural = 'Veículos'

    def __str__(self):
        return self.veiculo

