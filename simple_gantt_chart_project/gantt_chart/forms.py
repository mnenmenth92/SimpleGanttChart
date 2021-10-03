from django import forms


class jsonStringForm(forms.Form):
    data = forms.CharField(max_length=10000)



