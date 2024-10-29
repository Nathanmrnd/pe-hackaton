import streamlit as st
from streamlit.web import cli
import pandas as pd
from common_kataevskii import load_csv
import remi

def choixUtilisateurStreamlit(somme_utilisateur, actions_utilisateur, date, df):

    
    choix = st.text_input("Voulez-vous vendre des actions ? (O/N)")
    if choix == "O":
        choix = st.text_input("Ecrivez le nombre d'actions que vous voulez vendre et la companie concernée sous la forme [companie]-[nombre d'actions], vous pouvez faire une liste séparée par des virgules")
        choix = choix.split(',')
        for i in range(len(choix)):
            choix[i] = choix[i].split('-')
        for i in range(len(choix)):
            actions_utilisateur[choix[i][0]] -= int(choix[i][1])
            somme_utilisateur += int(choix[i][1]) * df.loc[date, choix[i][0]]
            st.write(somme_utilisateur, actions_utilisateur)

    choix = st.text_input("Voulez-vous acheter des actions ? (O/N)")
    if choix == "O":
        choix = st.text_input("Ecrivez le nombre d'actions que vous voulez acheter et la companie concernée sous la forme [companie]-[nombre d'actions], vous pouvez faire une liste séparée par des virgules")
        choix = choix.split(',')
        for i in range(len(choix)):
            choix[i] = choix[i].split('-')
        for i in range(len(choix)):
            actions_utilisateur[choix[i][0]] += int(choix[i][1])
            somme_utilisateur -= int(choix[i][1]) * df.loc[date, choix[i][0]]
            st.write(somme_utilisateur, actions_utilisateur)
            
    return somme_utilisateur, actions_utilisateur


def main():
    df = pd.DataFrame()
    stocks = ["AAPL", "CSCO", "MSFT", "QCOM", "SBUX"] # les obtenir en itérant sur les fichiers de "bourse" serait mieux
    somme_utilisateur = 1000
    actions_utilisateur = {stock : 0 for stock in stocks}
    for stock in stocks:
        df_stock = load_csv(f"bourse/{stock}.csv")
        values = df_stock["Open"]
        values = values.resample("W").first()
        df[stock] = values

    stocks = st.multiselect("Choose stocks to display :", list(df.columns), stocks)
    # if not stocks:
    #     st.error("Please select at least one country.")
    # else:
    data = df.T.loc[stocks]
    st.write("### Stock Value ($)", data.sort_index())
    data = data.T
    

    start = 10

    chart = st.line_chart(data.loc[:df.index[start],])

    for i in range(10):
        date = df.index[start+i]
        choix = st.text_input("Voulez-vous vendre des actions ? (O/N)", key=f"1{i}")
        if choix == "O":
            choix = st.text_input("Ecrivez le nombre d'actions que vous voulez vendre et la companie concernée sous la forme [companie]-[nombre d'actions], vous pouvez faire une liste séparée par des virgules", key=f"2{i}")
            choix = choix.split(',')
            for i in range(len(choix)):
                choix[i] = choix[i].split('-')
            for i in range(len(choix)):
                actions_utilisateur[choix[i][0]] -= int(choix[i][1])
                somme_utilisateur += int(choix[i][1]) * df.loc[date, choix[i][0]]
                st.write(somme_utilisateur, actions_utilisateur)

        choix = st.text_input("Voulez-vous acheter des actions ? (O/N)", key=f"{i}")
        if choix == "O":
            choix = st.text_input("Ecrivez le nombre d'actions que vous voulez acheter et la companie concernée sous la forme [companie]-[nombre d'actions], vous pouvez faire une liste séparée par des virgules", key=f"4{i}")
            choix = choix.split(',')
            for i in range(len(choix)):
                choix[i] = choix[i].split('-')
            for i in range(len(choix)):
                actions_utilisateur[choix[i][0]] += int(choix[i][1])
                somme_utilisateur -= int(choix[i][1]) * df.loc[date, choix[i][0]]
                st.write(somme_utilisateur, actions_utilisateur)
        chart.add_rows(data.loc[df.index[start]:df.index[start+i],])
main()

# for i in range(10):
#     st.write(f"Semaine {i}")
#     inp = st.text_input("Voulez-vous vendre des actions ? (Y/N)")
#     if inp == "Y":
#         inp = st.text_input("Combien ?")
#         st.write(inp)

# remi.main()