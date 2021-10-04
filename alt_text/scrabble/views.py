# Import required libraries
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Scrabble
import pandas as pd
import random

# API EndPoint
@csrf_exempt
def main(request):
    words = LoadData()
    sentence = json.loads(request.body.decode('utf-8'))
    sentence = sentence['sentence'].lower()
    word_list = sentence.split(sep=" ")
    new_list = FindReplacements(word_list, words)
    response = ' '.join(new_list)
    return JsonResponse({'msg': response}, status=201)

# Load word list to chose from
def LoadData():
    words = pd.read_csv("Words.csv")
    return words

# Find replacement words for sentence
def FindReplacements(word_list, words):
    new_list = []
    for word in word_list:
        letters = len(word)
        first = word[0]
        temp = words[(words["First"] == first) & (words["Length"] == letters)]

        if temp.shape[0] <= 1:
            new_list.append(word)
        else:  
            temp = temp[temp["Word"] != word]
            w_list = temp["Word"].tolist()
            new_list.append(random.choice(w_list))

    return new_list



    