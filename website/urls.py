from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('preise/', views.preise, name='preise'),
    path('oeffnungszeiten/', views.oeffnungszeiten, name='oeffnungszeiten'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('booking/', views.booking, name='booking'),
]
