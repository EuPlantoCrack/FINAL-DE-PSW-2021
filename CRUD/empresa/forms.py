from django import forms
from empresa.models import empresa


class empresaForm(forms.ModelForm):
    class Meta:
        model = empresa
        fields = "__all__"