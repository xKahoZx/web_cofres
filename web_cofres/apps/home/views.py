from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from web_cofres.apps.productos.models import *
from django.contrib.auth import login, logout, authenticate
from web_cofres.apps.home.forms import *
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.core.mail import EmailMultiAlternatives

def index_view(request):

	slider = Slider.objects.filter(Estado = True)
	ctx = {'slider':slider}
	return render_to_response('home/index.html', ctx,context_instance = RequestContext(request))

def lista_slider_view(request,bandera):
	if bandera == "Activo":
		slider = Slider.objects.filter(Estado = True)
	else:
		slider = Slider.objects.filter(Estado = False)
	ctx = {'sliders':slider,'ban':bandera}
	return render_to_response('home/lista_slider.html', ctx,context_instance = RequestContext(request))

def sobre_nosotros_view(request):
	return render_to_response('home/nosotros.html', context_instance = RequestContext(request))

def slider_view(request, id_carousel):
	carousel = Carousel.objects.get(id = id_carousel)
	ctx = {'carousel':carousel}
	return render_to_response('home/slider.html',ctx, context_instance = RequestContext(request))


def sabias_que_view(request):
	carousel = Carousel.objects.filter(Estado = True)
	ctx = {'carousel': carousel}
	return render_to_response('home/sabias.html',  ctx, context_instance = RequestContext(request))


def productos_view(request, pagina):

	productos = Producto.objects.all().order_by('Nombre')
	paginator = Paginator(productos, 4)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except (EmptyPage, InvalidPage):
		productos = paginator.page(paginator.num_pages)
		
	ctx = {'productos':productos}
	return render_to_response('home/productos.html', ctx, context_instance = RequestContext(request))

def contacto_view(request):

	
	if request.method == "POST":
		formulario = contact_form(request.POST)
		
		if formulario.is_valid():

			name 	= formulario.cleaned_data['name']
			email 	= formulario.cleaned_data['email']
			phone	= formulario.cleaned_data['phone']
			asunto 	= formulario.cleaned_data['asunto']
			mensaje	= formulario.cleaned_data['mensaje']

			to_admin = "cofresdelquindio@gmail.com"
			html_content = "<h5> Informacion recivida de <p>%s</p> </h5><h5> correo <p>%s</p> </h5><h5> Telefono <p>%s</p> </h5><h5>Asunto <p>%s</p> </h5> <h5> Mensaje</h5> <p> %s</p>"%(name, email, phone, asunto, mensaje)
 			msg = EmailMultiAlternatives('Mensaje Pagina Web', html_content, 'from@server.com', [to_admin])
 			msg.attach_alternative(html_content, 'text/html')
			msg.send()
			formulario = contact_form()	
			ctx = {'form':formulario, 'men':"Mensaje envia exitosamente te responderemos lo mas pronto posible"}
			return render_to_response('home/contacto.html',ctx,context_instance = RequestContext(request))
		else:
			formulario = contact_form()	
			ctx = {'form':formulario, 'men':"Por favor completa todos los campos correctamente"}
			return render_to_response('home/contacto.html',ctx,context_instance = RequestContext(request))	
	else:
		formulario = contact_form()	
	ctx = {'form':formulario}
	return render_to_response('home/contacto.html',ctx,context_instance = RequestContext(request))

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			formulario = Login_form(request.POST)
			if formulario.is_valid():
				usu = formulario.cleaned_data['usuario']
				pas = formulario.cleaned_data['clave']
				usuario = authenticate(username = usu, password = pas)
				if usuario is not None and usuario.is_active:
					login(request, usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "usuario y/o clave incorrecta"
		formulario = Login_form()
		ctx = {'form': formulario, 'men': mensaje}
		return render_to_response('home/login.html', ctx, context_instance = RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
