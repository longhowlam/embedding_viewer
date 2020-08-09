import streamlit as st
import pickle
import pandas as pd
import plotly_express as px
import numpy as np 

st.set_option('deprecation.showfileUploaderEncoding', False)

#@st.cache(allow_output_mutation=True)
#def load_data():
#    return pickle.load(_csv("test.csv")

#input_data = load_data()

uploaded_file = st.file_uploader("Choose a pickle file", type="pck")

if uploaded_file is not None:
    input_data = pickle.load(uploaded_file)

print( input_data.shape )   

colnames = input_data.columns
st.title("Embedding viewer")


x = st.sidebar.selectbox("select x", colnames)
y = st.sidebar.selectbox("select y", colnames)

threeD = st.sidebar.checkbox("3D")
if threeD :
    z = st.sidebar.selectbox("select z", colnames)

color = st.sidebar.selectbox("select color", colnames)
labels = st.sidebar.selectbox("select labels", colnames)
inp_str = st.sidebar.text_input("look for string")
hovername =  st.sidebar.selectbox("select hover", colnames)
sizevar =  st.sidebar.selectbox("select size", colnames)

mxsize = st.sidebar.slider("pointsiz", 1,15)
input_data[["labels"]] = input_data[[f"{labels}"]] 

plot_data = (
    input_data
    .assign(
        text_label = np.where(
            input_data.labels.str.contains(inp_str),
            input_data.labels,
            ""
        )
    )
    .assign( size = 1)
)

if threeD:
    fig = px.scatter_3d(
        plot_data,
        x= f"{x}", y=f"{y}", z = f"{z}", 
        color= f"{color}", 
        text = "text_label", hover_name = f"{hovername}"  ,
        width = 1300, height = 1000, 
        size = f"{sizevar}", size_max = mxsize
    )
else:
    fig = px.scatter(
        plot_data, 
        x= f"{x}", y=f"{y}", 
        color= f"{color}", 
        text = "text_label",  hover_name = f"{hovername}" ,
        width = 1300, height = 1000, 
        size = f"{sizevar}", size_max = mxsize
    )

st.plotly_chart(fig)
