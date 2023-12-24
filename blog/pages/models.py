from django.db import models
from accounts.models import CustomUser

class Page(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=80)
    cuerpo = models.TextField(max_length=20000)
    fecha = models.DateField()
    _autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    imagen_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.fecha}"
    
    @property
    def autor(self):
        return f"{self._autor.first_name} {self._autor.last_name}" if self._autor else ""