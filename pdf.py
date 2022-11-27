from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse

nomes = ['caio', 'marcos', 'joao']


def mm2p(milimetros):
    return milimetros / 0.352777


cnv = canvas.Canvas("meu_PDF.pdf", pagesize=A4)


eixo = 100


for nome in nomes:
    cnv.drawString(mm2p(eixo), mm2p(150), nome)
    eixo += 30

cnv.circle(mm2p(100), mm2p(150), mm2p(10))

cnv. line(mm2p(100), mm2p(150), mm2p(120), mm2p(160))
cnv. rect(mm2p(100), mm2p(150), mm2p(120), mm2p(160))
#

cnv.save()
