from django.db import models


class Subscription(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.IntegerField(null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "subscription"


"""
Pasos para crear una tabla:
1: Crear la migracion: Crea un archivo con el codigo necesario para poder crear
    la tabla
    
    python manage.py makemigrations subscription
    
2: Ejecutar la migracion 

    python manage.py migrate subscription
"""

"""
CharField: Para textos cortos/medianos
FloatField: Para decimales
TextField: Para textos largos
DateTimeField: Para la fecha y hora
"""