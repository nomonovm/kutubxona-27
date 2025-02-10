from django import forms
from .models import *

class TalabaForm(forms.Form):
    ism = forms.CharField(max_length=111)
    guruh = forms.CharField(max_length=55)
    kurs = forms.IntegerField()
    yosh = forms.IntegerField()
    kitob_soni = forms.IntegerField()

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = "__all__"

class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = "__all__"

class KutubxonachiForm(forms.ModelForm):
    class Meta:
        model = Kutubxonachi
        fields = "__all__"

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"