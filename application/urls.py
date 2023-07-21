from django.urls import path
from . import views



urlpatterns = [
    path('',views.index , name='index'),
    path('signup/', views.signup, name='signup'),
    path('prenota/', views.prenota, name='prenota'),
    path('prenotazione/', views.prenotazione, name='prenotazione'),
    path('ordine/', views.ordine, name='ordine'),
    ]