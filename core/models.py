from django.db import models
from stdimage import StdImageField


class Base(models.Model):
    created = models.DateField('Criado', auto_now_add=True)
    edited = models.DateField('Editado', auto_now=True)
    active = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


class MedicalRecord(Base):
    CHOICES = (
        ('simple', 'Simples'),
        ('medication', 'Medicação'),
        ('observation', 'Observação'),
        ('band_aid', 'Curativo'),
        ('suture', 'Sutura'),
        ('withdrawal', 'Retirada de Pontos'),
        ('rh', 'RH'),
    )
    SEX_CHOICES = (
        ('male', 'Masculino'),
        ('female', 'Feminino'),
        ('another', 'Outro'),
    )

    type = models.CharField('Tipo da consulta', max_length=18, choices=CHOICES)
    name = models.CharField('Nome completo', max_length=100)
    sus = models.CharField('Número do SUS', max_length=15, blank=True, null=True)
    sex = models.CharField('Sexo', max_length=9, choices=SEX_CHOICES)
    birth_date = models.DateField('Data de nascimento', blank=True, null=True)
    consultation_date = models.DateField('Data da consulta', blank=True, null=True)
    medical_record = StdImageField('Ficha médica', upload_to='medical_records')

    class Meta:
        verbose_name = 'Ficha médica'
        verbose_name_plural = 'Fichas médicas'

    def __str__(self):
        return f'{self.name} ({self.type})'
