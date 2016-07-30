from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('web_cofres.apps.home.views',
	url(r'^$', 'index_view' , name = 'vista_index'),
	url(r'^contacto/$', 'contacto_view' , name = 'vista_contacto'),
	url(r'^lista_slider/(?P<bandera>.*)/$', 'lista_slider_view' , name = 'vista_slider'),
	url(r'^slider/(?P<id_carousel>.*)/$', 'slider_view' , name = 'vista_slider'),
	url(r'^sabias/$', 'sabias_que_view' , name = 'vista_sabias'),
	url(r'^nosotros/$', 'sobre_nosotros_view' , name = 'vista_nosotros'),
	url(r'^productos/page/(?P<pagina>.*)/$', 'productos_view' , name = 'vista_productos'),
	url(r'^login/$', 'login_view', name = 'vista_login'),
	url(r'^logout/$', 'logout_view', name = 'vista_logout'),
)