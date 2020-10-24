from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.text import slugify

from .models import MenuSection

class MenuSectionCreateForm(ModelForm):

    class Meta:
        model = MenuSection
        fields = ['menu', 'name']
        widgets = {'menu': forms.HiddenInput()}
