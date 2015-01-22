from django import forms


class loginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput())
	
class registrationForm(forms.Form):
	college = forms.CharField(max_length=100)
	email = forms.EmailField()
