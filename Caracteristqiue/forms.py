from django import forms
from .models import Pam,Utilite

class PamForm(forms.ModelForm):
	class Meta:
		model =Pam
		fields ="__all__"


class UtiliteForm(forms.ModelForm):
	class Meta:
		model =Utilite
		fields ="__all__"