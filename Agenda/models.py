from django.db import models


class Agenda(models.Model):
    Tecnico = models.ForeignKey(
        "Tecnico.Tecnico",
        verbose_name="tecnico",
        related_name="tecnicoagenda",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    Empresa = models.ForeignKey(
        "Empresa.Empresa",
        verbose_name="empresa",
        related_name="empresaagenda",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    loc = models.CharField('localização', max_length=255)
    data = models.DateTimeField('Dia do agedamento')
    concluido = models.BooleanField('concluído', default=False)

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

    def __str__(self):
        return f'{self.Tecnico}, {self.Empresa}'
