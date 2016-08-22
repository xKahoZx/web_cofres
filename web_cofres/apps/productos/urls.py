from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('web_cofres.apps.productos.views',
	url(r'^add/product/$','add_producto_view', name = 'vista_agregar_producto'),
	url(r'^add/sabias/$','add_sabias_view', name = 'vista_agregar_sabias'),
	url(r'^edit/product/(?P<id_producto>.*)/$', 'edit_producto_view' , name = 'vista_editar_productos'),
	url(r'^add/slider/$','add_slider_view', name = 'vista_agregar_slider'),
	url(r'^edit/slider/(?P<id_slider>.*)/$', 'edit_slider_view' , name = 'vista_editar_slider'),
	url(r'^activar/slider/(?P<id_item>.*)/$', 'activar_item_view' , name = 'vista_activar_slider'),
	url(r'^desactivar/slider/(?P<id_item>.*)/$', 'desactivar_item_view' , name = 'desactivar_activar_slider'),
	url(r'^edit/carousel/(?P<id_carousel>.*)/$','edit_carousel_view', name = 'vista_editar_carousel'),
)