from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ["titulo", "subtitulo", "cuerpo", "fecha", "imagen_url"]
    
    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        self.fields['fecha'].widget.attrs.update({'class': 'datepicker'})
        self.fields['titulo'].widget.attrs.update({'class': 'form-control', 'id': 'form3Example5'})
        self.fields['subtitulo'].widget.attrs.update({'class': 'form-control', 'id': 'form3Example5'})
        self.fields['imagen_url'].widget.attrs.update({'class': 'form-control', 'id': 'form3Example5'})
        self.fields['cuerpo'].widget = forms.Textarea(attrs={'class': 'form-control', 'id': 'form3Example5', 'rows': 8})
        