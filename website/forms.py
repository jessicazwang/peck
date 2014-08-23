from django import forms
from website.models import Brother
import ast

class BrotherForm(forms.ModelForm):
	name = forms.CharField(widget=forms.HiddenInput(),initial='')
	year = forms.CharField(widget=forms.HiddenInput(),initial='')
	photo = forms.CharField(widget=forms.HiddenInput(),initial='')
	nickname = forms.CharField(widget=forms.HiddenInput(),initial='')
	initials = forms.CharField(widget=forms.HiddenInput(),initial='')
	hometown = forms.CharField(widget=forms.HiddenInput(),initial='')
	major = forms.CharField(widget=forms.HiddenInput(),initial='')
	activities = forms.CharField(widget=forms.HiddenInput(),initial='')
	quote = forms.CharField(widget=forms.HiddenInput(),initial='')
	blurb = forms.CharField(widget=forms.HiddenInput(),initial='')

	class Meta:
		model = Brother

