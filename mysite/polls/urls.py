from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='polls-index'),
    path('about/', views.about, name='polls-about'),
]

urlpatterns += staticfiles_urlpatterns()