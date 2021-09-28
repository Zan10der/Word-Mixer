from rest_framework import viewsets
from .models import Scrabble
from .serializers import ScrabbleSerializer

class ScrabbleViewSet(viewsets.ModelViewSet):
    queryset = Scrabble.objects.all()
    serializer_class = NoteSerializer
