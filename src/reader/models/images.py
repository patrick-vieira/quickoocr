from django.db import models


class ParsedImages(models.Model):

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'

    image = models.ImageField(verbose_name='Imagem')

    text = models.TextField(verbose_name='Texto')
    text_c = models.CharField(max_length=255, verbose_name='Texto C')

    details = models.TextField(verbose_name='Detalhes')

    folder = models.CharField(max_length=255)
