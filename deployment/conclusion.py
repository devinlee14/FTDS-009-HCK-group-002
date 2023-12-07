import streamlit as st

# Fill with project conclusion
def run():
    st.header('Conclusion')
    st.markdown('---')
    # -------------------------------------------------------------------------
    st.markdown('''
            **Model Deployment**: Integrating the sentiment analysis model into Google's app review system can be leveraged to achieve several outcomes:
            * Quality Control: Real-time sentiment scoring can be used to flag apps with consistently poor sentiment for quality review, ensuring that the apps offered on the Play Store maintain a high standard
            * Trend Detection: Google can monitor sentiment trends for early detection of issues like bugs in recent app updates, or to identify apps that are suddenly gaining positive attention, which could then be featured or recommended
            ''')
    st.markdown('---')    
    st.markdown('''
            **Strategic Actions**: Providing sentiment analysis feedback to app developers can be expanded upon for further strategic initiatives:
            * Automated Category Insights: An automated system could provide developers with real-time analytics on how their app's sentiment compares to the average within its category, including highlighting specific aspects like customer service, usability, or functionality that may need attention
            * Benchmarking and Best Practices: Developers can receive benchmark reports comparing their apps with top-performing ones in the same category, offering insights into best practices and areas for improvement
            * Predictive Analytics for Developers: By analyzing sentiment trends, Google can offer predictive insights to developers, helping them anticipate user needs and expectations, and guiding them on when to release updates or introduce new features
            * Content Moderation Strategies: Using sentiment analysis to prioritize the review of content can help:
                * Improve Moderation Efficiency: Focus human moderators' efforts on the most critical content first, improving the efficiency of the moderation process
                * Enhance App Safety: Quickly address apps with negative sentiments that might be related to safety or compliance issues, maintaining a safe environment for all users
                * Refine Automated Systems: Feed sentiment analysis data into automated content moderation systems to improve their accuracy and responsiveness  
            ''')