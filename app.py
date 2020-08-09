import streamlit as st
import pickle
import pandas as pd
import plotly_express as px
import numpy as np 


@st.cache(allow_output_mutation=True)
def load_data():
    return pd.read_csv("test.csv")

input_data = load_data()
colnames = input_data.columns
st.title("Embedding viewer")


x = st.sidebar.selectbox("select x", colnames)
y = st.sidebar.selectbox("select y", colnames)
color = st.sidebar.selectbox("select color", colnames)
labels = st.sidebar.selectbox("select labels", colnames)
inp_str = st.sidebar.text_input("look for string")

input_data[["labels"]] = input_data[[f"{labels}"]] 

plot_data = (
    input_data
    .assign(
        text = np.where(
            input_data.labels.str.contains(inp_str),
            input_data.labels,
            ""
        )
    )
)

fig = px.scatter(plot_data, x= f"{x}", y=f"{y}", color= f"{color}", text = "text", width = 1000, height = 1000)

st.plotly_chart(fig)
