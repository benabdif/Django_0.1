from django import forms

from .models import Addproduct2, test_t


class my(forms.ModelForm):
    class Meta:
        model = Addproduct2
        fields = ['price', 'name']
        

class test_t1(forms.ModelForm):
    class Meta:
        model = test_t
        fields = ['product']
        