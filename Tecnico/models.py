from django.db import models


class Base(models.Model):
    contratacao = models.DateTimeField(auto_now_add=True)
    disponivel = models.BooleanField(default=True)


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


class Tecnico(Base):
    nome = models.CharField('Nome', max_length=255, null=False, blank=False)
    estado = models.CharField('Estado', max_length=100, choices=Estados.STATUS_CHOICES, default=Estados.Paraiba, null=False, blank=False)
    cidade = models.CharField('Cidade', max_length=255)
    registro = models.IntegerField('Registro', unique=True, null=False, blank=False)

    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'
        unique_together = ['registro']

    def __str__(self):
        return f'Técnico {self.nome}, {self.estado}/{self.cidade}'
