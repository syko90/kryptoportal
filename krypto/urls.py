from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('prices/', views.prices, name='prices'),
    path('wallet/', views.wallet, name='wallet'),
    path('events/', views.events, name='events'),
]
