from .models import Imagemodel
from django.forms import ModelForm
class ImageForm(ModelForm):
    class Meta:
        model=Imagemodel
        fields="__all__"
        
        