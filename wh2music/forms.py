from django import forms

class songForm(forms.Form):
    song = forms.CharField(max_length=200)
    artist = forms.CharField(max_length=200)
    album = forms.CharField(max_length=200)
    music = forms.FileField()
