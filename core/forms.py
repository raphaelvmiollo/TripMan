# -*- coding: utf-8 -*-

from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):

	def __init__(self, *args, **kwargs):
		super(CustomAuthenticationForm,self).__init__(*args,**kwargs)

		self.fields['username'].widget.attrs['style']='width:100%'
		self.fields['password'].widget.attrs['style']='width:100%'
		
		self.fields['username'].label =  u'Usuário'
		self.fields['password'].label =  u'Senha'

		self.fields['username'].widget.attrs['class']="form-control"
		self.fields['password'].widget.attrs['class']="form-control"
