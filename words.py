import os
import random
from symbol import eval_input
from words import array_animals

def word_data():
    indice = random.randint(0, 86)
    english = array_animals[indice][0]
    portuguese = array_animals[indice][1]
    categorie = array_animals[indice][2]
    indice_categorie = array_animals[indice][3]

    #print("ejfnsdfdsfs", array_animals[0][1])

    return indice, english, portuguese, categorie, indice_categorie