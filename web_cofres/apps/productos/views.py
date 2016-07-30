from django.shortcuts import render_to_response
from django.template import RequestContext
from web_cofres.apps.productos.forms import *
from web_cofres.apps.productos.models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def add_producto_view(request):
	if request.method=="POST":
		formulario = add_product_form(request.POST, request.FILES) 
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()
			return HttpResponseRedirect ('/productos/page/1')
	else:
		formulario = add_product_form()
	ctx = {'form':formulario}
	return render_to_response('productos/add_producto.html',ctx,context_instance = RequestContext(request))

def edit_producto_view(request, id_producto):
	producto = Producto.objects.get(id = id_producto)
	if request.method == "POST":
		formulario = add_product_form(request.POST, request.FILES,instance = producto)
		if formulario.is_valid():
			edit = formulario.save(commit = False)
			edit.save()
			return HttpResponseRedirect ('/productos/page/1')
	else:
		formulario = add_product_form(instance = producto)
	bandera = "editar"
	ctx = {'form':formulario,'ban':bandera}
	return render_to_response('productos/add_producto.html', ctx , context_instance = RequestContext(request))

def edit_carousel_view(request, id_carousel):
	carousel = Carousel.objects.get(id = id_carousel)
	if request.method == "POST":
		formulario = edit_carousel_form(request.POST, request.FILES, instance = carousel)
		if formulario.is_valid():
			edit = formulario.save(commit = False)
			edit.save()
			return HttpResponseRedirect ("/sabias")
	else:
		formulario = edit_carousel_form(instance = carousel)
	ctx = {'form':formulario}
	return render_to_response('productos/edit_carousel.html', ctx , context_instance = RequestContext(request))


def add_slider_view(request):

	if request.method=="POST":
		formulario = slider_form(request.POST, request.FILES) 
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save()
			return HttpResponseRedirect ('/lista_slider')
	else:
		formulario = add_product_form()
	ctx = {'form':formulario}
	return render_to_response('productos/add_edit_slider.html',ctx,context_instance = RequestContext(request))

def edit_slider_view(request, id_slider):
	slider = Slider.objects.get(id = id_slider)
	if request.method == "POST":
		formulario = slider_form(request.POST, request.FILES,instance = slider)
		if formulario.is_valid():
			edit = formulario.save(commit = False)
			edit.save()
			return HttpResponseRedirect ('/lista_slider/Activo')
	else:
		formulario = add_product_form(instance = slider)
	bandera = "editar"
	ctx = {'form':formulario,'ban':bandera}
	return render_to_response('productos/add_edit_slider.html', ctx , context_instance = RequestContext(request))

def activar_item_view(request, id_item):
	if User.is_authenticated:
		item = Slider.objects.get(id = id_item)
		item.Estado = True
		item.save()
	return HttpResponseRedirect ('/lista_slider/Inactivo')

def desactivar_item_view(request, id_item):
	if User.is_authenticated:
		item = Slider.objects.get(id = id_item)
		item.Estado = False
		item.save()
	return HttpResponseRedirect ('/lista_slider/Activo')