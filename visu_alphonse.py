import streamlit as st
from streamlit.web import cli
import pandas as pd
from common_kataevskii import load_csv
import altair
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}
df = pd.DataFrame()
stocks = ["AAPL", "CSCO", "MSFT", "QCOM", "SBUX"] # les obtenir en itérant sur les fichiers de "bourse" serait mieux

for stock in stocks:
    df_stock = load_csv(f"bourse/{stock}.csv")
    values = df_stock["Open"]
    values = values.resample("W").first()
    df[stock] = values

stocks = st.multiselect("Choose stocks", list(df.columns), ["AAPL", "QCOM"])
# if not stocks:
#     st.error("Please select at least one country.")
# else:
data = df.T.loc[stocks]
st.write("### Stock Value ($)", data.sort_index())
data = data.T
st.line_chart(data)
