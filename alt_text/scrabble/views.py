#from rest_framework import viewsets
from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import Scrabble
#from .serializers import ScrabbleSerializer

def ScrabbleViewSet(request):
    
    if request.method == "POST":

        data = json.loads(request.body)
        sentence = data["sentence"]

        print(sentence)

        return JsonResponse({"msg": response}, status=201)
    
    return render(request, 'scrabble_view.html')
