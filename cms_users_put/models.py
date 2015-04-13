from django.db import models

# Create your models here.

class Page(models.Model):
	name = models.CharField(max_length=32)
	contenido = models.TextField()
    
	def __str__(self):
		return self.name
