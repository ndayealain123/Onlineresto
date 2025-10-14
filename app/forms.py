
from django import forms
from .models import *

class ProfileForm(forms.Form):
	#____________pour user___________________#
		username=forms.CharField(max_length=20)
		password=forms.CharField(max_length=20, widget=forms.PasswordInput)
		password1=forms.CharField(max_length=20, widget=forms.PasswordInput)
		nom=forms.CharField(max_length=20)
		prenom=forms.CharField(max_length=20)
	#______________champ pou profil___________#
		birthday = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
		gender = forms.CharField(max_length=20)
		phone = forms.CharField(max_length=20)
		address = forms.CharField(max_length=20)

class ConnexionForm(forms.Form):
	username= forms.CharField(widget= forms.TextInput(attrs={
    		'placeholder':'username....',
    		}),label="Username :")
	password = forms.CharField(widget= forms.PasswordInput(attrs={
    		'placeholder':'password....',
    		}),label="PassWord :")
	
