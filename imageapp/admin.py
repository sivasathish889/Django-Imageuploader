from django.contrib import admin
from imageapp.models import Imagemodel
# Register your models here.

class Imageadmin(admin.ModelAdmin):
    list_display=["id","title","image","date"]


admin.site.register(Imagemodel,Imageadmin)