from django import forms

class uTxt(forms.Form):
    uTxt = forms.CharField(label='Press Enter to Submit:', max_length=100)