from django.urls import include, path

from Vocabulary import views

urlpatterns = [
    path('', views.build_vocab, name='build_vocab'), 
]
