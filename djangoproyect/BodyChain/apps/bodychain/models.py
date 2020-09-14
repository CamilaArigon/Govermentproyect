from django.db import models

class Client(models.Model):
    id = models.AutoField(primary_key= True)
    nombre=models.CharField(max_length=30, blank= True, null= True)
    direccion=models.CharField(max_length=50 blank= True, null= True)
    email=models.EmailField(blank= True, null= True)
    tfno=models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre

