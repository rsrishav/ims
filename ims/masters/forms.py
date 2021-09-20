from django import forms


class Category(forms.Form):
    title = forms.CharField(label='Enter tile', max_length=50)
    description = forms.CharField(label='Enter description', max_length=250)
