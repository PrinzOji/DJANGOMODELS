from django.urls import path

from . import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('contact2/', views.contact2, name='contact2'),
]