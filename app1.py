import cv2
import numpy as np
import pickle
import streamlit as st

st.set_page_config(
    page_title="Smart_Parking"
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """



st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>SMART PARKING SYSTEM</h1>", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)
#st.write'''Smart Parking is a parking strategy that combines technology and human innovation in an effort to use as few resources as possible—such as fuel, time and space—to achieve faster, easier and denser parking of vehicles for the majority of time they remain idle. 
#'''
st.markdown("<h3 style='text-align: center; color: white;'>Smart Parking is a parking strategy that combines technology and human innovation in an effort to use as few resources as possible—such as fuel, time and space—to achieve faster, easier and denser parking of vehicles for the majority of time they remain idle. </h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>Our Clients</h3>", unsafe_allow_html=True)
st.write('<div style="text-align:center">Mr P Ranganathan</div>', unsafe_allow_html=True)
st.write('''I wish parking of vehicles should be smooth and hastle free"
''')
st.write('<div style="text-align:center">Mr Ramesh Yadagiri</div>', unsafe_allow_html=True)
st.write('''For ground workers like us, we find it difficult to instruct the drivers to navigate to a parking 
''')

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://media.giphy.com/media/Jjfa6PH31VRgA/giphy.gif");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

