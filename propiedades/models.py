from django.db import models

# Create your modelss here.
class Propiedad(models.Model):
    codigo=models.AutoField(primary_key=True)
    ancho=models.DecimalField(blank=False, decimal_places=2, max_digits=9)
    largo=models.DecimalField(blank=False, decimal_places=2, max_digits=9)
    precio=models.DecimalField(blank=False, decimal_places=2, max_digits=9)
    habitaciones=models.IntegerField(blank=False)
    opciones_disponible=(
        ('SI', 'DISPOPNIBLE'),
        ('NO', 'NO DISPONIBLE'),    
    )
    disponibilidad=models.CharField(choices=opciones_disponible, default='SI',  max_length=20)
    
    def _str_(self):
        return self.codigo
    class Meta:
        abstract  = True
  
class casa(Propiedad):
    pass
    opciones_jardin=(
        ('SI', 'CON JARDIN'),
        ('NO', 'SIN JARDIN'),    
    )
    jardin=models.CharField(choices=opciones_jardin, default='NO',max_length=20)
class departameto(Propiedad):
    pass
    piso=models.IntegerField()
