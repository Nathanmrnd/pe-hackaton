import streamlit as st
from streamlit.web import cli
import pandas as pd
import common_kataevskii as cm
import time 

stocks = ["AAPL", "CSCO", "MSFT", "QCOM", "SBUX"]

df = pd.DataFrame()

for stock in stocks:
    df_stock = cm.load_csv(f"bourse/{stock}.csv")
    values = df_stock["Open"]
    df[stock] = values

placeholder = st.empty()

window = cm.slice_date("2020-01-01", "2021-01-01", df)

for i in range(1000):
    with placeholder.container():
        chart = st.line_chart(window)
        window = cm.advance_window(window, df, 1)
        time.sleep(0.1)
