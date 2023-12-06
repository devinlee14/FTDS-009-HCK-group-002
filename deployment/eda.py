import streamlit as st

def run():
    st.title("Exploratory Data Analysis")
    st.markdown('---')
    
# -----------------------------------------------------------------------------------------
    # Rating Distribution
    st.markdown('### Rating Distribution')
    st.image('images/rating_distribution.png', caption='Figure 1')
    with st.expander('Explanation'):
        st.caption('From this Histogram of Rating Distribution, we know:')
        st.caption('''
                * The distribution is skewed towards higher ratings, with most apps receiving ratings between 4.0 and 4.7
                * The highest frequency of ratings is at 4.4, followed closely by 4.3 and 4.5, indicating that a large number of apps are rated favorably
                * Very few apps have ratings lower than 3.0, suggesting either a selection of generally well-received apps or a tendency for users 
                to rate apps more favorably
                ''')
        st.caption('''
                The drop in frequency for ratings 4.8 and above could indicate a standard where few apps 
                are rated as near-perfect. Overall, this distribution indicates a trend where users rate apps positively, 
                with few instances of very low ratings.
                ''')
    st.write('')
    st.write('')

# -----------------------------------------------------------------------------------------
    # Review Distribution
    st.markdown('### Review Distribution')
    st.image('images/reviews_distribution.png', caption='Figure 2')
    with st.expander('Explanation'):
        st.caption('''
                The distribution is highly right-skewed, indicating that a large number of apps have a small number of reviews, 
                This could be due to several reasons like new apps, or even unpopular apps, while only a few apps have a 
                very high number of reviews. This pattern suggests that a small subset of apps is receiving the majority 
                of the attention from users in terms of reviews.
                ''')
    st.write('')
    st.write('')

# -----------------------------------------------------------------------------------------
    # Price distribution among paid apps
    st.markdown('### Price Distribution among Paid Apps')
    st.image('images/Price_Distribution_Among_Paid_Apps.png', caption='Figure 3')
    with st.expander('Explanation'):
        st.caption('''
                Most paid apps are priced below $10, with peaks at around the $2 and $4 price points. 
                There are fewer apps at higher price points, indicating that lower-priced apps are 
                more common and potentially more popular among users.
                ''')
    st.write('')
    st.write('')

# -----------------------------------------------------------------------------------------
    # Ratings vs Reviews
    st.markdown('### Ratings vs Reviews')
    st.image('images/Rating_vs_Reviews.png', caption='Figure 4')
    with st.expander('Explanation'):
        st.caption('''
                There is a concentration of apps with high ratings and a moderate number of reviews, 
                very few apps have low ratings, and apps with near perfect rating are relatively rare. 
                This may indicate that well-rated apps tend to receive a good number of reviews, but not all popular apps 
                (in terms of the number of reviews) are necessarily high-rated.
                ''')
    st.write('')
    st.write('')

# -----------------------------------------------------------------------------------------
    # Category popularity
    st.markdown('### Category Popularity')
    st.image('images/Category_Popularity.png', caption='Figure 5')
    with st.expander('Explanation'):
        st.caption('''
                The 'Game' category is the most popular, followed by 'Family' and 'Health & Fitness', 
                suggesting these are the most common types of apps. Less populated categories like 
                'Events' and 'Comics' may represent more niche markets.
                ''')
    st.write('')
    st.write('')

# -----------------------------------------------------------------------------------------
    # Ratings by Category
    st.markdown('### Ratings by Category')
    st.image('images/Boxplot_of_Ratings_by_Category.png', caption='Figure 6')
    with st.expander('Explanation'):
        st.caption('''
                * Most categories have median ratings above 4.0, indicating generally positive reception of apps across all categories
                * Some categories show a wide range of ratings (evidenced by longer boxes), indicating more variability in how users rate these apps
                * Categories with tight boxes, where Q1 and Q3 are close together, indicate more consistency in ratings
                * Outliers are present in many categories, both on the high and low ends, suggesting that there are a 
                few apps that are rated significantly differently than the majority in their category
                ''')
        st.caption('''
                Overall, this plot provides a comprehensive view of how apps are rated within each category, 
                showing general user satisfaction and highlighting categories with more diverse user opinions.
                ''')
    st.write('')
    st.write('')

# -----------------------------------------------------------------------------------------
    # Sentiment Distribution
    st.markdown('### Sentiment Distribution')
    st.image('images/Sentiment_Distribution.png', caption='Figure 7')
    with st.expander('Explanation'):
        st.caption('''
                * The 'positive' category has the highest count, exceeding 20,000 items
                * The 'negative' category has a lower count, roughly around 7,500 items
                * The 'neutral' category has the least, with just under 5,000 items 
                ''')
        st.caption('This suggests that the positive sentiment among the items being analyzed predominates significantly over negative and neutral sentiments.')
    st.write('')
    st.write('')

# -----------------------------------------------------------------------------------------
    # Sentiment Polarity Distribution
    st.markdown('### Sentiment Polarity Distribution')
    st.image('images/Distribution_of_Sentiment_Polarity.png', caption='Figure 8')
    with st.expander('Explanation'):
        st.caption('''
                The chart shows a large concentration of scores around 0, indicating a high frequency of neutral sentiments. 
                There is a notable spike at exactly 0, which is significantly higher than any other value, suggesting a 
                large number of entries with a perfectly neutral sentiment. The distribution is somewhat bimodal, with smaller peaks 
                in the positive range (around 0.5) and negative range (around -0.25 to -0.5), implying clusters of positive and 
                negative sentiments as well. However, the positive sentiments appear to have a slightly wider spread 
                with multiple smaller peaks, while negative sentiments are more concentrated around their peak. 
                Overall, this suggests that the data contains a high volume of neutral sentiments, with a presence of 
                both positive and negative sentiments, and a broader diversity of positive sentiment intensities.
                ''')
    st.write('')
    st.write('')

# -----------------------------------------------------------------------------------------
    # Sentiment Subjectivity Distribution
    st.markdown('### Sentiment Subjectivity Distribution')
    st.image('images/Distribution_of_Sentiment_Subjectivity.png', caption='Figure 9')
    with st.expander('Explanation'):
        st.caption('Sentiment subjectivity shows the level of objectiveness of the user review where 0 indicates no subjectivity and 1 indicates high subjectivity.')
        st.caption('''
                * A high peak at 0, suggesting a significant number of texts are classified with no subjectivity, meaning they are likely to be factual or objective
                * Several moderate peaks throughout, especially noticeable around 0.2, 0.5, 0.6, and towards the higher end at 1.0
                * The peaks at 0.5 and higher indicate a considerable number of texts contain subjective opinions
                ''')
        st.caption('''
                The distribution is somewhat uneven, suggesting varying levels of opinion across the dataset, 
                with a notable amount of completely objective (or detected as such) texts and others 
                expressing different degrees of subjectivity. The presence of multiple peaks indicates that 
                texts do not conform to a single level of subjectivity but vary widely, which might be typical in 
                datasets containing both factual information and personal opinions.
                ''')
    st.write('')
    st.write('')

# -----------------------------------------------------------------------------------------
    # Text Length by Sentiment
    st.markdown('### Text Length by Sentiment')
    st.image('images/Distribution_of_Text_Length_Character_by_Sentiment.png', caption='Figure 10')
    with st.expander('Explanation'):
        st.caption('''
                The distribution of text length for reviews shows that neutral sentiment texts are generally shorter, 
                with a mean length of around 7 words and a median of 5 words. Positive sentiment texts are longer, 
                with a mean of approximately 19 words and a median of 17 words, while negative sentiment texts have a mean 
                length close to 17 words and a median of 14 words. This could indicate that users tend to be more 
                verbose when expressing positive or negative sentiments, while neutral comments are more concise.
                ''')
    st.write('')
    st.write('')

# -----------------------------------------------------------------------------------------
    # Wordclouds by Sentiment
    st.markdown('## Wordcloud by Sentiment')

    st.markdown('### Positive')
    st.image('images/Positive_Sentiment_Words.png', caption='Figure 11')
    st.write('')

    st.markdown('### Negative')
    st.image('images/Negative_Sentiment_Words.png', caption='Figure 12')
    st.write('')

    st.markdown('### Neutral')
    st.image('images/Neutral_Sentiment_Words.png', caption='Figure 13')
    with st.expander('Explanation'):
        st.caption('''
                The word clouds for positive, negative, and neutral sentiments highlight the most frequently used 
                words in each category. 
                * Positive sentiments words like "love", "great", "good" and "best" dominate, reflecting strong satisfaction 
                * Negative sentiment texts frequently include words like "bad", "problem", "worst" and "annoying" pointing to dissatisfaction 
                * Neutral sentiment texts feature words like "update", "phone" and "app" which may relate to more factual 
                or inquiry-based content rather than opinion.
                ''')
