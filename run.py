import os
import random
from words import array_animals

def word_data():
    indice = random.randint(0, 86)
    english = array_animals[indice][0]
    portuguese = array_animals[indice][1]
    categorie = array_animals[indice][2]
    indice_categorie = array_animals[indice][3]

    #print("ejfnsdfdsfs", array_animals[0][1])

    return indice, english, portuguese, categorie, indice_categorie


def menu():
    print("[LAN] Learning Animal Names - [PTBR to EN]\n")
    print("[1] Start\n[2] Statistics\n[3] Config\n[9] Exit")
    array_op = ['1', '2', '3', '9']
    op = input()
    os.system("cls")
    if op in array_op:
        op = int(op)
        if op == 1:
            run()
        elif op == 2:
            statistic()
            menu()
        elif op == 3:
            config()
            menu()
        elif op == 9:
            exit()
    else:
        os.system('cls')
        print("Keryword ["+ op +"] not found!")
        menu()
        

def main():

    os.system('cls')
    menu()


main()