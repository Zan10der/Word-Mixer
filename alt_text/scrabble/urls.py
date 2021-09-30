from django.urls import include, path
#from rest_framework import routers
from .views import ScrabbleViewSet

#router = routers.DefaultRouter()
#router.register(r'scrabble', ScrabbleViewSet)

urlpatterns = [
    path('', ScrabbleViewSet, name="scrabble_view"),
]
