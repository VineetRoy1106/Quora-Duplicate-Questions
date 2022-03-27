import joblib
import streamlit as st
import helper
import pickle
import warnings

with warnings.catch_warnings():
      warnings.simplefilter("ignore", category=UserWarning)
      estimator = joblib.load('model.pkl')

model = pickle.load(open('model.pkl', 'rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')