from django.db import models


class Servico(models.Model):
    Empresa = models.ForeignKey(
        "Empresa.Empresa",
        verbose_name="empresa",
        related_name="empresaservico",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    Tecnico = models.ForeignKey(
        "Tecnico.Tecnico",
        verbose_name="tecnico",
        related_name="tecnicoservico",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    Cliente = models.ForeignKey(
        "Cliente.Cliente",
        verbose_name="cliente",
        related_name="clienteservico",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    Pagamento = models.ForeignKey(
        "Pagamento.Pagamento",
        verbose_name="pagamento",
        related_name="pagamentoservico",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "tutorial_servico"
        verbose_name = "Serviço"
        verbose_name_plural = "Servico"
