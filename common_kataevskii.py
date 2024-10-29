# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

#%%
import pandas as pd
# %%
def load_csv(name):
    df = pd.read_csv(name, index_col="Date")
    df.index = pd.to_datetime(df.index, format="%m/%d/%Y")
    df["High"] = df["High"].str.replace("$", "").astype(float)
    df["Open"] = df["Open"].str.replace("$", "").astype(float)
    df["Low"] = df["Low"].str.replace("$", "").astype(float)
    df["Close/Last"] = df["Close/Last"].str.replace("$", "").astype(float)
    return df
# %%
def slice_date(beginning, ending, df): #format should be "2024-10-28"
    beg = pd.to_datetime(beginning, format ="%Y-%m-%d")
    end = pd.to_datetime(ending, format ="%Y-%m-%d")
    result = df[(df.index > beg) & (df.index < end)]
    return result