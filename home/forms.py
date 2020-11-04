from django.forms import ModelForm
from home.models import *
from django import forms

class ListForm(ModelForm):
    class Meta:
        model=List
        fields=['name','phonenumber','age','gender','bp','pulserate','sugarf','sugarpp','temp','diagnosis','medicine','reference']



class ListImageForm(ModelForm):
	class Meta:
		model = Listimages
		fields =['image']