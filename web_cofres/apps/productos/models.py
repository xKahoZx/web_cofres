from django.db import models

# Create your models here.

class Slider(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Slider/%s_%s"%(self.Nombre, str(filename))
		return ruta
	Nombre 		= models.CharField(max_length = 50)
	Imagen		= models.ImageField(upload_to = url)
	Estado		= models.BooleanField(default = True)

	def __unicode__(self):
		return self.Nombre

class Carousel(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Carousel/%s_%s"%(self.Nombre, str(filename))
		return ruta
	Nombre 		= models.CharField(max_length = 50)
	Imagen_1	= models.ImageField(upload_to = url)
	Imagen_2	= models.ImageField(upload_to = url)
	Imagen_3	= models.ImageField(upload_to = url)
	Imagen_4	= models.ImageField(upload_to = url)	
	Imagen_5	= models.ImageField(upload_to = url)
	Descripcion	= models.TextField(max_length = 200)
	Estado		= models.BooleanField(default = True)


	def __unicode__(self):
		return self.Nombre

class Producto(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Producto/%s_%s"%(self.Nombre, str(filename))
		return ruta

	Nombre 		= models.CharField(max_length = 50)
	Imagen		= models.ImageField(upload_to = url)
	Descripcion	= models.TextField(max_length = 500)

	def __unicode__(self):
		return self.Nombre

