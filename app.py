import streamlit as st
from transformers import pipeline

# Custom page configuration with a dark theme
st.set_page_config(page_title="Sentiment Analysis", layout="wide", page_icon="🧠")

# Initialize the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Title and description
st.title("Sentiment Analysis with Hugging Face")
st.write(
    "This tool uses a machine learning model to analyze the sentiment of your text. Enter some text below and see the magic!"
)

# Layout using columns for input and output sections
col1, col2 = st.columns([2, 1])

with col1:  # Column for user input
    user_input = st.text_area(
        "Enter Text Here", placeholder="Type something here...", height=250
    )
    analyze_button = st.button("Analyze")

with col2:  # Column for displaying analysis results
    st.write("## Analysis Result:")
    if analyze_button and user_input:
        result = sentiment_pipeline(user_input)[0]
        sentiment = result["label"]
        confidence = result["score"]

        # Dynamically change the color and font size of the sentiment result based on the sentiment
        if sentiment == "POSITIVE":
            st.markdown(
                f"<h2 style='color: green;'>{sentiment}</h2>", unsafe_allow_html=True
            )
        elif sentiment == "NEGATIVE":
            st.markdown(
                f"<h2 style='color: red;'>{sentiment}</h2>", unsafe_allow_html=True
            )
        else:  # Neutral or mixed sentiments can be handled here
            st.markdown(
                f"<h2 style='color: yellow;'>{sentiment}</h2>", unsafe_allow_html=True
            )

        st.metric(label="Confidence", value=f"{confidence:.2%}")

    elif analyze_button:
        st.warning("Please enter some text to analyze.")
