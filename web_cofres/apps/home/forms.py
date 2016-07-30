from django import forms


class contact_form(forms.Form):

	name  		= forms.CharField( widget = forms.TextInput())
	phone		= forms.CharField( widget = forms.TextInput())
	email		= forms.EmailField( widget = forms.TextInput())
	asunto 		=  forms.CharField( widget = forms.TextInput())
	mensaje 	= forms.CharField( widget = forms.Textarea())

class Login_form(forms.Form):
	usuario		= forms.CharField(widget = forms.TextInput())
	clave		= forms.CharField(widget = forms.PasswordInput(render_value = True))