# -*- coding: utf-8 -*- 
from django.db import models
class Site(models.Model):
    STATUS_CHOICES = (
        (u'ativo', u'Ativo'),
        (u'inativo', u'Inativo'),
    )
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=45, verbose_name='Titulo')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    imagem = models.ImageField(max_length=255, blank=True, upload_to='conteudo/%Y', verbose_name='Imagem')
    link = models.URLField(max_length=255, blank=True, verbose_name='Link')
    email = models.EmailField(null = False),
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Status do conteudo')
    data_cadastro = models.DateTimeField(verbose_name='Data de Cadastro')
    def __unicode__(self):
        return self.titulo
    class Meta:
        db_table = u'site'
        verbose_name = 'site'
        verbose_name_plural = 'sites'
        ordering = ['titulo']        
        