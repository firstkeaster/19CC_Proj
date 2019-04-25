from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'upload', views.uploadImg),
    url(r'^show', views.showImg),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)