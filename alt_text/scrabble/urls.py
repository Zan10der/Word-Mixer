from django.urls import path
#from rest_framework import routers
from .views import main

#router = routers.DefaultRouter()
#router.register(r'scrabble', ScrabbleViewSet)

urlpatterns = [
    path('', main),
]
