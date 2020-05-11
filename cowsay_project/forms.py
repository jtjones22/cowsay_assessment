from django import forms


# simple form
class AddCowsay(forms.Form):
    text = forms.CharField(max_length=100)