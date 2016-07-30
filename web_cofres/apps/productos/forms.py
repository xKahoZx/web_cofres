from django import forms
from web_cofres.apps.productos.models import *

class add_product_form(forms.ModelForm):
	class Meta:
		model   = Producto
		

class edit_carousel_form(forms.ModelForm):
	class Meta:
		model   = Carousel
		exclude = ('Estado')

class slider_form(forms.ModelForm):
	class Meta:
		model   = Slider
		exclude = ('Estado')

