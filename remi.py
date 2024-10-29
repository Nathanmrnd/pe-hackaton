import matplotlib.pyplot as plt
import pandas as pd
import common_kataevskii as cm

df = cm.load_csv("bourse/AAOPL.csv")

liste_df = [df]

def recupererAction(companie, date, liste_df):
    return liste_df[companie].loc[date, "Open"]

def afficherStatsUtilisateur(somme, actions):
    print("Vous possedez", somme, "$ et vos actions sont:")
    for c in actions.keys():
        print(c, " : ", actions[c])
    print("\n")

companies = ["Apple", "Total", "Bnp_Paribas"]
def choixUtilisateur(somme_utilisateur, actions_utilisateur, date):

    print("\n\n")
    afficherStatsUtilisateur(somme_utilisateur, actions_utilisateur)
    
    print("Les compagnies disponibles sont")
    for c in companies:
        print(c)
    print("Voulez-vous vendre des actions ?")
    print("Rentrez N si non, O si oui")
    choix = input()
    if choix == "O":
        print("Ecrivez le nombre d'actions que vous voulez vendre et la companie concernée sous la forme [companie]-[nombre d'actions], vous pouvez faire une liste séparée par des virgules")
        choix = input().split(',')
        for i in range(len(choix)):
            choix[i] = choix[i].split('-')
        for i in range(len(choix)):
            actions_utilisateur[choix[i][0]] -= int(choix[i][1])
            somme_utilisateur += int(choix[i][1]) * recupererAction(choix[i][0], date, liste_df)
    print("Voulez-vous acheter des actions ?")
    print("Rentrez N si non, O si oui")
    choix = input()
    if choix == "O":
        print("Ecrivez le nombre d'actions que vous voulez acheter et la companie concernée sous la forme [companie]-[nombre d'actions], vous pouvez faire une liste séparée par des virgules")
        choix = input().split(',')
        for i in range(len(choix)):
            choix[i] = choix[i].split('-')
        for i in range(len(choix)):
            actions_utilisateur[choix[i][0]] += int(choix[i][1])
            somme_utilisateur -= int(choix[i][1]) * recupererAction(choix[i][0], date, liste_df)
            
    return somme_utilisateur, actions_utilisateur

def main():
    somme_utilisateur = 1000
    actions_utilisateur = {"Total": 0, "Apple": 0, "Bnp_Paribas": 0}
    window = cm.slice_date("2020-01-01", "2020-02-01")
    for i in range(10):
        #afficher fenetre
        window.Open.plot()
        #choix utilisateur
        date = window.indices[0]
        choixUtilisateur(somme_utilisateur, actions_utilisateur, date)
        #augmenter la date
        window = cm.advance_window(window, df, 5)

# actions_utilisateur = {"Apple": 10, "Total": 20, "Bnp_Paribas": 5}
# choixUtilisateur(1000, actions_utilisateur, "date")
