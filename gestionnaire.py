import csv
import os

isClose = False
isPseudoOk = False

while isClose == False:

    #initialiser la data
    print("=================================")
    print("DATA :")
    data = []
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
        for row in data:
            print(row['pseudo'], row['mot_de_passe'])


    #ouverture du menu
    print("=================================")
    print("1. Inscription")
    print("2. Connexion")
    print("3. Options")
    print("4. Quitter")

    userChoiseMenu = int(input("Que voulez vous faire ?\n"))

    #inscription
    if userChoiseMenu == 1:
        print("choix 1")

        #entrée pseudo + verif si le pseudo est déja utilisé
        while isPseudoOk == False:

            userPseudo = input("rentrez votre pseudo : ")

            if userPseudo == "":
                print("le pseudo est vide")
            else:
                for i in data:
                    if userPseudo == i['pseudo']:
                        print("Ce pseudo existe déjà !")
                        isPseudoOk = False
                        break
                    else:
                        isPseudoOk = True



        userMdp = input("rentrez votre mot de passe : ")

        with open('data.csv', 'a') as file:
            writer = csv.DictWriter(file, delimiter=',', fieldnames = ['pseudo', 'mot_de_passe'], )
            writer.writerow({'pseudo': userPseudo, 'mot_de_passe': userMdp})
        userPseudo = ""
        userMdp = ""

    #connexion
    elif userChoiseMenu == 2:
        print("choix 2")


    elif userChoiseMenu == 3:
        print("choix 3")

        with open('data.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print("Voici la base de donnée : \n")
            for row in reader:
                print(row['pseudo'], row['mot_de_passe'])

    #option
    elif userChoiseMenu == 4:
        print("choix 4")
        isClose = True
        print("Fermeture de l'interface")

    #quitter
    else:
        print("Error veuillez rentrer un chiffre valide!")

    os.system('cls' if os.name == 'nt' else 'clear')