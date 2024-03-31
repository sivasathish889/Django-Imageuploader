
from django.contrib import admin
from django.urls import path,include
from imageapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.imageview),
    path("delete/<id>/",views.Delete),
    path("delete/",views.deleted)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_DIR)
