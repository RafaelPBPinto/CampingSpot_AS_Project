from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='polls-index'),
    path('about.html/', views.about, name='polls-about'),
    path('gallery.html/', views.gallery, name='polls-gallery'),
]

urlpatterns += staticfiles_urlpatterns()
