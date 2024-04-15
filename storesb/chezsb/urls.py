from django.urls import path
from .views import *

urlpatterns = [
    path('', accueil, name='index'),
    path('barre-de-navigation/', barre_de_navigation, name='barre_de_navigation'),
    path('en-tete/', en_tete, name='en_tete'),
    path('catalogue/', catalogue, name='catalogue'),
    path('shoe/<int:id>/', shoe, name='shoe'),
    path('contact/', contact, name='contact'),
    path('creer-actualite/', creer_actualite, name='create_article'),
    path('create_annonce/', annonce, name='create_annonce'),
    path('approuver-actualite/<int:pk>/', approuver_actualite, name='approuver_actualite'),
    path('supprimer-actualite/<int:pk>/', supprimer_actualite, name='supprimer_actualite'),
    path('register', register, name='register'),
    path('logout', custom_logout, name='logout'),
    
] 