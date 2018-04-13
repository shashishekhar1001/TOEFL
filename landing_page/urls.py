from django.urls import include, path 
from landing_page import views

urlpatterns = [
    path('', views.home, name='home'), 
]
