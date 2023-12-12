from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class Prices(models.Model):
    original_price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Цена продавца')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, **NULLABLE,verbose_name='Цена на площадке')

    class Meta:
        verbose_name = 'цена'
        verbose_name_plural = 'цены'