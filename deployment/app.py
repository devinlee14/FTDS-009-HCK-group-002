import streamlit as st
import eda
import models

st.sidebar.header("Group 2")
st.sidebar.write("Simplifying App Review Sentiment Analysis")

page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploratory Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Final Project') 
    st.write('')
    # st.write('Final Project')
    st.write('Devin Yaung Lee — Data Analyst')
    st.write('Fernaldy Aristo Wirjowerdojo — Data Engineer')
    st.write('Muhammad Furqon Pakpahan — Data Engineer')
    st.write('Sifra Hilda Juliana Siregar — Data Scientist')
    # st.write('Objectives : Develop an Automated Sentiment Analysis Model')
    st.write('')
    st.caption('Please select another menu in the Select Box on the left side of your screen to get started!')
    st.write('')
    st.write('')
    with st.expander("Project Overview"):
            st.caption('This project focuses on performing sentiment analysis on Google Play Store app reviews. Utilizing Natural Language Processing (NLP), the goal is to analyse user feedback to gain insights into satisfaction and app perception.')

    with st.expander("Problem Statement"):
            st.caption('In the competitive landscape of mobile applications, user feedback for app reviews is a goldmine of insights that can inform product development and marketing strategies. However, these reviews are often unstructured, making it challenging to efficiently extract, categorize, and analyze sentiments and opinions. There is a need for an automated system that can process this feedback to provide actionable insights, identify trends in user sentiment, and highlight areas for improvement. This project aims to address the lack of structured analysis of user-generated content in app reviews on the Google Play Store, which, if leveraged correctly, can significantly enhance user satisfaction and app performance in the market.')

    with st.expander("Objectives"):
            st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        <ul> 
            <li>Develop an Automated Sentiment Analysis Model</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True)
            st.caption('Build and train a TensorFlow model to classify app reviews into positive, negative, and neutral sentiments with high accuracy.')

            st.caption(
        f"""
        <div style="font-size: 15px; text-align: justify;">
        <ul> 
            <li>Understand the user feedbacks in depth</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True)
            st.caption('Utilize the sentiment analysis model to delve into the nuances of user feedback on the Google Play Store')
elif page == 'Exploratory Data Analysis':
    eda.run()
else:
    models .run()

    