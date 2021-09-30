"""from django.db import models

class Scrabble(models.Model):
    content = models.TextField()
"""
import pandas as pd
import random

class Scrabble():
    def LoadData(self,):
        words = pd.read_csv("Words.csv")
        return words

    def FindReplacements(self, word_list, words):
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