from django.db import models


class Pag(models.Model):
    credito = 'cre'
    especie = 'esp'
    debito = 'deb'
    transferencia = 'tra'
    pix = 'pix'
    PAG_CHOICES = [
        (credito, 'Crédito'),
        (especie, 'Especie'),
        (debito, 'Debito'),
        (transferencia, 'Transferencia'),
        (pix, 'Pix')
    ]


class Pagamento(models.Model):
    funcionario = models.CharField('Funcionario', max_length=100, null=False, blank=False)
    Tecnico = models.ForeignKey(
        "Tecnico.Tecnico",
        verbose_name="tecnico",
        related_name="tecnicopagamento",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    Empresa = models.ForeignKey(
        "Empresa.Empresa",
        verbose_name="empresa",
        related_name="empresapagamento",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    Cliente = models.ForeignKey(
        "Cliente.Cliente",
        verbose_name="cliente",
        related_name="clientepagamento",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    Veiculo = models.ForeignKey(
        "Cliente.Veiculo",
        verbose_name="veiculo",
        related_name="veiculopagamento",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    forma_de_pag = models.CharField('Forma de pagamento', max_length=100, choices=Pag.PAG_CHOICES, default=Pag.pix, null=False, blank=False)
    valor = models.CharField('Valor pago', max_length=100, null=False, blank=False)

    def __str__(self):
        return f' {self.Empresa}, recebeu de: {self.Cliente}, {self.valor}'
