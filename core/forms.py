# -*- coding: utf-8 -*-

from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):

	def __init__(self, *args, **kwargs):
		super(CustomAuthenticationForm,self).__init__(*args,**kwargs)
		
		self.fields['username'].label =  u''#Usuário'
		self.fields['password'].label =  u''#Senha'

		self.fields['username'].widget.attrs['class']="form-control"
		self.fields['password'].widget.attrs['class']="form-control"

		self.fields['username'].widget.attrs['placeholder']=u'Usuário'
		self.fields['password'].widget.attrs['placeholder']=u'Senha'