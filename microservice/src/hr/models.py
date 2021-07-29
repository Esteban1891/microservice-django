from django.db import models

# Create your models here.
class Direcciones(models.Model):
    ID_DIRECCION = models.CharField(max_length=150)
    ID_PREDIO = models.CharField(max_length=150)
    DIRECCION_IGAC = models.CharField(max_length=150)
    DIRECCION_STD = models.CharField(max_length=150)
    REVISAR = models.CharField(max_length=150)
    DIRECCION = models.CharField(max_length=150)
    REF_CATASTRAL = models.CharField(max_length=150)
    DESCRIPCION = models.CharField(max_length=150)
    MAT_INMOBILIARIA = models.CharField(max_length=150)
    REF_CAT_NUEVA = models.CharField(max_length=150)



    def __str__(self) -> str:
        return self.ID_DIRECCION