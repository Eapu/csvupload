
# -*- coding: utf-8 -*-

from django import forms


class DocumentoForm(forms.Form):
	docfile = forms.FileField(
		label='Select a file'
	)