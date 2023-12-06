import streamlit as st
import eda
import model
import conclusion

# Sidebar
st.sidebar.header("Choose Here!")
options = ['Home Page', 'Exploratory Data Analysis', 'Test our Model!', 'Conclusion']
page = st.sidebar.selectbox(label='Select Page:', options=options)

# Home Page
if page == 'Home Page':
    st.header('Feedback to Foresight: Simplifying App Review Sentiment Analysis')
    st.caption("This project was carried out as part of Hacktiv8's Data Science programme final collaborative project.")
    st.caption('Please check our github repository [here!](https://github.com/devinlee14/FTDS-009-HCK-group-002)')
    st.markdown('---')

    st.markdown('''
            #### Group members:
            * Devin Yaung Lee — Data Analyst
            * Fernaldy Aristo Wirjowerdojo — Data Engineer
            * Muhammad Furqon Pakpahan — Data Engineer
            * Sifra Hilda Juliana Siregar — Data Scientist
            ''')
    st.write('')

    st.caption('Please select another page in the `Select Page` on the left side of your screen to get started!')
    st.write('')

    with st.expander("Project Overview"):
            st.caption('''
                    This project focuses on performing sentiment analysis on Google Play Store app reviews. 
                    Utilizing Natural Language Processing (NLP), the goal is to analyse user feedback 
                    to gain insights into satisfaction and app perception.
                    ''')

    with st.expander("Problem Statement"):
            st.caption('''
                    In the competitive landscape of mobile applications, user feedback for app reviews is a 
                    goldmine of insights that can inform product development and marketing strategies. 
                    However, these reviews are often unstructured, making it challenging to efficiently extract, 
                    categorize, and analyze sentiments and opinions. There is a need for an automated system 
                    that can process this feedback to provide actionable insights, identify trends in user sentiment, 
                    and highlight areas for improvement. This project aims to address the lack of structured 
                    analysis of user-generated content in app reviews on the Google Play Store, which, 
                    if leveraged correctly, can significantly enhance user satisfaction and app performance in the market.
                    ''')

    with st.expander("Objectives"):
            st.caption('''
                    * **Develop an Automated Sentiment Analysis Model**  
                    Build and train a TensorFlow model to classify app reviews into positive, negative, and neutral sentiments with high accuracy.

                    * **Understand the User Feedbacks in Depth**  
                    Utilize the sentiment analysis model to delve into the nuances of user feedback on the Google Play Store.
                    ''')

# EDA      
elif page == 'Exploratory Data Analysis':
    eda.run()

# Model
elif page == 'Test our Model!':
    model.run()

# Conclusion
else:
    conclusion.run()
    