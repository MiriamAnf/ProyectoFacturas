from django.db import models
from django.core.exceptions import ValidationError
from decimal import *

import arrow
import datetime
import decimal

class Receipt(models.Model):
    num_receipt = models.AutoField(primary_key=True, verbose_name='Número de factura')
    year = models.DateTimeField(auto_now_add=True, verbose_name='Año')
    date_of_issue = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de emisión')
    updated_issue = models.DateTimeField(auto_now=True)
    costumer_name = models.TextField(verbose_name='Nombre del cliente')
    costumer_address = models.TextField(verbose_name='Dirección del cliente')
    closed = models.DateTimeField(
        null=True, 
        blank=True,
        default=None,
    )

    def precio_total(self):
        getcontext().prec = 6
        total = Decimal(0)
        for linereceipt in self.linereceipt_set.all():
            unit_price = linereceipt.base_imponible()
            total += unit_price
        return total   
    
    def __str__(self):
        return f"{self.num_receipt}: {self.costumer_name}"


class LineReceipt(models.Model):
    id_product = models.AutoField(primary_key=True, verbose_name='Línea')
    product_name = models.CharField(max_length=200, verbose_name='Nombre del producto')
    receipt = models.ForeignKey(
        Receipt,
        on_delete=models.PROTECT,
        )
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Precio unitario')
    units = models.IntegerField(default=1, verbose_name='Unidades')

    def base_imponible(self):
        return self.unit_price * Decimal(self.units)
    
    def __str__(self):
        return f"{self.id_product}|: {self.product_name}"
