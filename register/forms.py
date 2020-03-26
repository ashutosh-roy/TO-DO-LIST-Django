from django import forms
from django.forms import ModelForm
from register.models import detail

class detailForm(form.ModelForm):
    class Meta:
        model  = detail
        fields = '__all__'