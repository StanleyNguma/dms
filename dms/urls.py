from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^auth/$', views.auth),
    url(r'^upload-files/$', views.upload_files),
]
