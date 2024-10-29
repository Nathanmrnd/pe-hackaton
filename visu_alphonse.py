import streamlit as st
from streamlit.web import cli
import pandas as pd
from common_kataevskii import load_csv


def main():
    df = pd.DataFrame()
    stocks = ["AAPL", "CSCO"] # les obtenir en itérant sur les fichiers de "bourse" serait mieux
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
    st.line_chart(data)
    
    # start = 10
    # interval = 4
    # reps = 10

    # chart = st.line_chart(data.loc[:df.index[start],])
    # st.write("Argent : ",somme_utilisateur, "Actions : ", actions_utilisateur)

    # for i in range(reps):
    #     date = df.index[start+interval*i]

    #     with st.form(f"form{i}1"):
    #         choix = st.text_input("Voulez-vous vendre des actions ? (O/N)", key=f"1{i}")
    #         submitted = st.form_submit_button("Valider")
    #         if choix == "O":
    #             choix = st.text_input("Ecrivez le nombre d'actions que vous voulez vendre et la companie concernée sous la forme [companie]-[nombre d'actions], vous pouvez faire une liste séparée par des virgules", key=f"2{i}")
    #             choix = choix.split(',')
    #             for i in range(len(choix)):
    #                 choix[i] = choix[i].split('-')
    #             for i in range(len(choix)):
    #                 actions_utilisateur[choix[i][0]] -= int(choix[i][1])
    #                 somme_utilisateur += int(choix[i][1]) * df.loc[date, choix[i][0]]
    #                 st.write(somme_utilisateur, actions_utilisateur)
    #             submitted = st.form_submit_button("Valider le(s) choix")
    #     with st.form(f"form{i}2"):
    #         choix = st.text_input("Voulez-vous acheter des actions ? (O/N)", key=f"3{i}")
    #         submitted = st.form_submit_button("Valider")
    #         if choix == "O":
    #             choix = st.text_input("Ecrivez le nombre d'actions que vous voulez acheter et la companie concernée sous la forme [companie]-[nombre d'actions], vous pouvez faire une liste séparée par des virgules", key=f"4{i}")
    #             choix = choix.split(',')
    #             for i in range(len(choix)):
    #                 choix[i] = choix[i].split('-')
    #             for i in range(len(choix)):
    #                 actions_utilisateur[choix[i][0]] += int(choix[i][1])
    #                 somme_utilisateur -= int(choix[i][1]) * df.loc[date, choix[i][0]]
    #                 st.write(somme_utilisateur, actions_utilisateur)
    #             submitted = st.form_submit_button("Valider le(s) choix")
    #     chart.add_rows(data.loc[df.index[start+interval*i]:df.index[start+interval*(i+1)],])
main()