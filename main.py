import streamlit as st
import pandas as pd
import base64

from pip._internal import main

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("1_small.png")

with col3:
    st.write(' ')

# A streamlit app with two centered texts with different seizes
import streamlit as st

st.markdown("<h1 style='text-align: center; color: black;'>3DP-as-a-Service (3DPaaS)</h1>" , unsafe_allow_html = True)

st.markdown("<h2 style='text-align: center; color: black;'>The Resource Management Solution for Additive Manufacturing! </h2>" , unsafe_allow_html = True)

st.markdown("<h2 style='text-align: center; color: black;'>3D Print any model in minutes by: </h2>" , unsafe_allow_html = True)

st.subheader("""- Connecting to 3D Printers via the Blockchain""")

st.subheader("""- Mine Crypto as a member of our Blockchain""")

st.subheader("""- View 3D Models""")

st.subheader("""- Slice models""")

st.subheader("""- View Printing Data""")

st.markdown("<h1 style='text-align: center; color: white;'>To learn more watch the video!</h1>" , unsafe_allow_html = True)

st.video("3DPaaSgood.mp4")

st.markdown("<h1 style='text-align: center; color: white;'>Find a Service Bureau in your area (or anywhere)!</h1>" , unsafe_allow_html = True)

df = pd.DataFrame(np.random.randn(100, 2) / [50, 50] + [42.8864, -78.8784],
columns=['lat', 'lon'])
st.map(df)

st.sidebar.header('Start your 3D Printing experience by choosing an app below:')

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

app_mode = st.sidebar.selectbox('Select Feature',['Home','Model Viewer','Analytics Data','Service Bureau Connect','Blockchain Service','SLS and BinderJet Quote']) #two pages

