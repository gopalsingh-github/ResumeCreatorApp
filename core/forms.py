from django import forms
from .models import Data

class Student_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=50)
    email = forms.EmailField(widget=forms.EmailField(), required=True)
    massage = forms.CharField(widget=forms.TextInput(), required=False, max_length=60)

    """class Meta:
        model = Data
        fields = ['id','name', 'email', 'massage']
        widgets= {
            'name':forms.TextInput(),
            'email': forms.TextInput(),
            'massage': forms.TextInput(),
        }"""