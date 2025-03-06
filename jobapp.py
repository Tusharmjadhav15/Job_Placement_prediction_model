from PIL import Image
import numpy as np
import pandas as pd
import pickle
import streamlit as st

lr = pickle.load(open('placement.pkl','rb'))

#web app
img = Image.open(r'photos\jobplacement.jpg')
st.image(img,width=650)
st.title('Job Placement Prediction Model')

input_txt= st.text_input("Enter all Features")
input_list = input_txt.split(',')

if input_list:
    np_df = np.asarray(input_list,dtype=float)
    pred = lr.predict(np_df.reshape(1,-1))

    if pred[0]==1:
        st.write('This person is placed')
    else:
        st.write('This person is not placed ')