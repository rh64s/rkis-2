from django import forms
from django.forms import models


class BookFilesForm(models.ModelForm):
    image = forms.fields.ImageField(required=False)
    text = forms.fields.FileField(required=False)
    class Meta:
        fields = ('image', 'text')