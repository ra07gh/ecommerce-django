from django import forms
from .models import BeautyProduct

class BeautyProductForm(forms.ModelForm):
    class Meta:
        model = BeautyProduct
        fields = '__all__'
