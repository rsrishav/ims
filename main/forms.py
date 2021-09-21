from django import forms


class CreateNewItem(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    check = forms.BooleanField()
