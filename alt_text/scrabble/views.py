from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Scrabble
import pandas as pd

@csrf_exempt
def main(request):
    words = LoadData()
    print(request.data)
    response = request.data
    return JsonResponse({'msg': response}, status=201)

def LoadData():
    words = pd.read_csv("Words.csv")
    return words

def FindReplacements(word_list, words):
    new_list = []
    for word in word_list:
        letters = len(word)
        first = word[0]
        temp = words[(words["First"] == first) & (words["Length"] == letters)]

        if temp.shape[0] == 0:
            new_list.append(word)
        else:  
            temp = temp[temp["Word"] != word]
            w_list = temp["Word"].tolist()
            new_list.append(random.choice(w_list))

    return new_list