import csv
import random

#fonction pour Le menu
def menu():
    print("-----------------------------------MENU----------------------------------\n"
          "|   01   |   02   |   03   |   04   |   05   |   06   |   07   |   08   |\n"
          "-------------------------------------------------------------------------\n"
          "|   09   |   10   |   11   |   12   |   13   |   14   |   15   |   16   |\n"
          "-------------------------------------------------------------------------\n"
          "|   17   |   18   |   19   |   20   |   21   |   22   |   23   |   24   |\n"
          "-------------------------------------------------------------------------\n"
    )

# ouverture du fichier des questions en ecriture pour le remplissage
with open("QST.csv", "w", newline="", encoding="utf-8") as fQ:
    QST=csv.writer(fQ, delimiter=";")
    QST.writerow(["Quel est le plus grand ocean du monde?" , "A)  Atlantique", "B)  Indien","C)  Arctique ","D)  Pacifique" ])
    QST.writerow([ "Quel pays est connu pour la Tour Eiffel? ", "A)  Italie" ,"B)  Espagne" ,"C)  France" ,"D)  Allemagne"])
    QST.writerow([ "Quelle est la formule chimique de l'eau?", "A)  H2O","B)  CO2","C)  O2","D)  H2SO4"])
    QST.writerow(["Combien y a-t-il de planetes dans notre systeme solaire?","A)  7", "B)  8","C)  9", "D)  10"])
    QST.writerow(["Qui a ecrit L'Origine des especes?",  "A)  Isaac Newton", "B)  Albert Einstein","C)  Charles Darwin","D)  Galilee"])

#ouverture du fichier des reponses en ecriture pour le remplissage
with open("reponse.csv","w",newline="",encoding="utf-8") as fR:
    reponse=csv.writer(fR, delimiter=";")
    reponse.writerow(["Pacifique",])
    reponse.writerow(["France"])
    reponse.writerow(["H2O"])
    reponse.writerow(["8"])
    reponse.writerow(["Charles Darwin"])


#ouverture du fichier des question en lecture
with open("QST.csv", "r", encoding="utf-8") as fLQ:
    L_QST=list( csv.reader(fLQ, delimiter=";"))


#ouverture du fichier des reponse en lecture
with open("reponse.csv", "r", encoding="utf-8") as fLR:
    l_reponse=list( csv.reader(fLR, delimiter=";"))

#debut d'affichage du programme
while True:
    x=input("Taper star pour debuter le jeux ou stop pour arreter : ")
    if x.lower() == "star" :
        menu()
        break
    if x.lower() == "stop":
        print("programme quitter")
        quit()
    else:
        print(" Erreur !! veuillez repeter votre choix")

for i in range (4):
    print(f"le groupe {i+1}: ")
    #choi d'un nombre
    NB=int(input("veuillez choisir un nombre : "))
    #choix par hasard du question
    hasard=(random.choice(L_QST))
    ligne_de_qst=L_QST.index(hasard)
    for y in hasard:
        print("     ",y ,"\n")

    #reponse d'utilisateur
    reponse_utilisateur=input("votre reponse :")

    #verification des reponse
    reponse_correct=l_reponse[ligne_de_qst]
    if reponse_utilisateur.lower().strip() == reponse_correct[0].lower():
        print(f"\n reponse est correct Vous avez gagné 100 pts")
    else:
        print(f"\n Réponse incorrecte. La bonne réponse était : {reponse_correct[0]}")
    L_QST.remove(hasard)
    l_reponse.remove(reponse_correct)


