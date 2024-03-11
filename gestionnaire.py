import csv
import os

isClose = False
isOptionClose = True

def dataShow():
    print("=================================")
    print("DATA :")
    data = []
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
        for row in data:
            print(row['pseudo'], row['mot_de_passe'])
    return data

def Inscription():
    print("choix 1")
    #entrée pseudo + verif si le pseudo est déja utilisé
    isPseudoOk = False
    while isPseudoOk == False:
        isPseudoOk = True
        userPseudo = input("rentrez votre pseudo : ")
        if userPseudo == "":
            print("le pseudo est vide")
            isPseudoOk = False
        else:
            for i in data:
                if userPseudo == i['pseudo']:
                    print("Ce pseudo est déjà pris !")
                    isPseudoOk = False
                    break
                else:
                    isPseudoOk = True
            
    userMdp = input("rentrez votre mot de passe : ")
    with open('data.csv', 'a') as file:
        writer = csv.DictWriter(file, delimiter=',', fieldnames = ['pseudo', 'mot_de_passe'], )
        writer.writerow({'pseudo': userPseudo, 'mot_de_passe': userMdp})

def Connexion():
    print("choix 2")
    isIdentifyOK = False
    while isIdentifyOK == False:
        userPseudo = input("rentrez votre pseudo : ")
        userMdp = input("rentrez votre mot de passe : ")
        if userPseudo == "" or userMdp == "":
            print("Veuillez rentrer les informations nécessaires !")
            isIdentifyOK == False
        else:
            for i in data:
                if userPseudo == i['pseudo'] and userMdp == i['mot_de_passe']:
                    isIdentifyOK = True
            if isIdentifyOK == False:
                print("Mauvais Identifiants !")
            elif isIdentifyOK == True:
                input("Bienvenue " + userPseudo + ", appuie sur entrer pour revenir au menu ! :)")

def Option(data):
    print("choix 3 saisie")
    isOptionClose = False
    while isOptionClose == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=================================")
        print("DATA :")
        for row in data:
            print(row['pseudo'], row['mot_de_passe'])
        #ouverture du menu
        print("=================================")
        print("1. Supprimer un compte")
        print("2. Retour")
        
        userChoiseOption = int(input(""))
        if userChoiseOption == 1:
            ("choix 1")
            isIdentifyOK = False
            nameToDelete = input("quel nom voulez vous supprimer? ")
            if nameToDelete == "":
                ("rentrez un nom!")
            else:
                for i in data:
                    if nameToDelete == i['pseudo']:
                        mdpTry = input("rentrez le mot de passe de ce compte")
                        if mdpTry == i['mot_de_passe']:
                            with open('data.csv', newline='') as csvfile:
                                


                    



            isOptionClose = True
        elif userChoiseOption == 2:
            isOptionClose = True



while isClose == False:
    os.system('cls' if os.name == 'nt' else 'clear')

    data = dataShow() #initialiser la data

    #ouverture du menu
    print("=================================")
    print("1. Inscription")
    print("2. Connexion")
    print("3. Options")
    print("4. Quitter")

    userChoiseMenu = int(input("Que voulez vous faire ?\n"))

    #inscription
    if userChoiseMenu == 1:
        Inscription()

    #connexion
    elif userChoiseMenu == 2:
        Connexion()

    elif userChoiseMenu == 3:
        Option(data)

    #option
    elif userChoiseMenu == 4:
        print("choix 4")
        isClose = True
        print("Fermeture de l'interface")

    #quitter
    else:
        print("Error veuillez rentrer un chiffre valide!")