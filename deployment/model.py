import streamlit as st
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from functions.text_preprocessed import text_preprocessing
from tensorflow.keras.models import load_model

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def run():
    st.title('Predict')
    st.write('You can use our model here by inputting your text (review) here:')

    # -------------------------------------------------------------------------
    # Dataframe
    data = pd.DataFrame()

    # -------------------------------------------------------------------------
    # App name
    data['app'] = [st.text_input('Application name')]

    # -------------------------------------------------------------------------
    # Category
    data['category'] = [st.text_input('Application category')]

    # -------------------------------------------------------------------------
    # Rating
    data['rating'] = [round(st.slider('Rating', min_value=0.0, max_value=5.0), 1)]

    # -------------------------------------------------------------------------
    # Reviews
    data['reviews'] = [st.number_input('Total review count', min_value=0)]
    
    # -------------------------------------------------------------------------
    # Size
    data['size'] = [st.text_input('File size')]

    # -------------------------------------------------------------------------
    # Installs
    data['installs'] = [st.number_input('Total installs', min_value=0)]

    # -------------------------------------------------------------------------
    # Type
    data['type'] = [st.text_input('Paid / Free')]

    # -------------------------------------------------------------------------
    # Price
    data['price'] = [st.number_input('Application price', min_value = 0.00)]

    # -------------------------------------------------------------------------
    # Content rating
    data['content_rating'] = [st.text_input('Age rating')]

    # -------------------------------------------------------------------------
    # Genres
    data['genres'] = [st.text_input("Genres").split(',')]
    st.caption("Separate by ',' if multiple genres")
    # -------------------------------------------------------------------------
    # Last updated
    data['last_updated'] = [st.date_input('Last updated')]

    # -------------------------------------------------------------------------
    # Current version
    data['current_ver'] = [st.text_input('Current version')]

    # -------------------------------------------------------------------------
    # Android version
    data['android_ver'] = [st.text_input('Android version')]
    
    # -------------------------------------------------------------------------
    # Review
    review = st.text_input('Application review (in English)')
    ## Stop words 
    stop_words = set(stopwords.words('english'))
    ## Lemmatizer
    lemmatizer = WordNetLemmatizer()
    ## Processed text
    text_processed = text_preprocessing(review, lemmatizer, stop_words)

    data['translated_review'] = [review]
    data['text_processed'] = [text_processed]

    # -------------------------------------------------------------------------
    # User data
    st.dataframe(data.T, width=800, height=565)

    # -------------------------------------------------------------------------
    # Prediction
    if st.button('Predict'):
        model = load_model('lstm')
        sentiment_pred = model.predict(data['text_processed'])
        st.write(sentiment_pred)
        if sentiment_pred > 1.5:
            st.write('Positive Review')
        elif (sentiment_pred < 1.5) & (sentiment_pred >= 1.0):
            st.write('Negative Review')
        else:
            st.write('Neutral Review')