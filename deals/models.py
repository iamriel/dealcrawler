from decimal import Decimal

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=20)
    spider_name = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return self.name


class Deal(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    company = models.ForeignKey(Company)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0'))
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0'))

    def __str__(self):
        return self.title
