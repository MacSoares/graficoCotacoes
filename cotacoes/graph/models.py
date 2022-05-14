from django.db import models

# Create your models here.


class Currency(models.Model):
    base_date = models.DateTimeField()
    eur = models.DecimalField(max_digits=6, decimal_places=4)
    usd = models.DecimalField(max_digits=6, decimal_places=4)
    jpy = models.DecimalField(max_digits=6, decimal_places=4)
