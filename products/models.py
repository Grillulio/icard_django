from django.db import models
from django.db.models.fields.files import ImageField


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=10, decimal_places=0)  # Permite hasta 10 dígitos en total y 2 decimales
    active = models.BooleanField(default=False)
    category = models.ForeignKey(
        'categories.Category', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
