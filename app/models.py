from django.db import models
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.core.validators import MinLengthValidator

class Log(models.Model):
    LEVEL_CHOICES = [
        ("A", "All"),
        ("D", "Debug"),
        ("I", "Info"),
        ("W", "Warning"),
        ("E", "Error"),
        ("F", "Fatal"),
        ("O", "Off"),
        ("T", "Trace"),
    ]
    TYPE_CHOICES = [
        ("P", "Produção"),
        ("H", "Homologação"),
        ("D", "Dev"),
    ]
    descricao = models.CharField(max_length=30, null=False, blank=False)
    origem = models.CharField(max_length=100, null=False, blank=False)
    data_registro = models.DateTimeField(null=False, blank=False)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, null=False, blank=False)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TYPE_CHOICES, null=False, blank=False)
    eventos = models.BigIntegerField(null=False, blank=False)
    detalhes = models.CharField(max_length=400, null=True, blank=True)

min_validator = MinLengthValidator(8, 'A senha deve conter pelo menos 8 caracteres.')

class LogManager(models.Manager):
    def tipo(self, pk: int, order: str) -> QuerySet:
        """
            Realiza a pesquisa nos logs cujo tipo de erro serja do id **pk**.

            :param text: Texto que será usado na pesquisa

            :return: QuerySet com o filtro aplicado
        """
        queryset = self.get_queryset().filter(tipo=pk).order_by(order)
        return queryset

    def level_with_text(self, text: str, order: str) -> QuerySet:
        """
            Realiza a pesquisa nos logs cujo tipo de level contenha **text**.

            :param text: Texto que será usado na pesquisa

            :return: QuerySet com o filtro aplicado
        """
        queryset = self.get_queryset().filter(level__name__contains=text).order_by(order)
        return queryset

    def tipo_with_text(self, text: str, order: str) -> QuerySet:
        """
            Realiza a pesquisa nos logs cujo tipo contenha **text**.

            :param text: Texto que será usado na pesquisa

            :return: QuerySet com o filtro aplicado
        """
        queryset = self.get_queryset().filter(tipo__name__contains=text).order_by(order)
        return queryset

    def descricao_with_text(self, text: str, order: str) -> QuerySet:
        """
            Realiza a pesquisa nos logs cuja descrição contenha **text**.

            :param text: Texto que será usado na pesquisa

            :return: QuerySet com o filtro aplicado
        """
        queryset = self.get_queryset().filter(descricao__contains=text).order_by(order)
        return queryset
