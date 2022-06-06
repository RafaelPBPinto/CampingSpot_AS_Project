from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='polls-index'),
    path('about.html/', views.about, name='polls-about'),
    path('anpc.html/', views.anpc, name='polls-anpc'),
    path('gallery.html/', views.gallery, name='polls-gallery'),
    path('login.html/', views.login, name='polls-login'),
]

urlpatterns += staticfiles_urlpatterns()