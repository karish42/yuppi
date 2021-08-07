from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path

from arts import views
from yuppi import settings

#from django.views.static import serve
#from django.conf.urls import url

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
   # path('<int:id>/', views.detail_view, name='detail'),
    #url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
   # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
