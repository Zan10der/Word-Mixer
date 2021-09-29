import pandas as pd
import random

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

words = LoadData()

while True:
    sentence = input("Please type in a 5 word sentence:\n")
    sentence = sentence.lower()

    word_list = sentence.split(sep=" ")

    new_list = FindReplacements(word_list=word_list, words=words)

    print(new_list)