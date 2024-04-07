# Sentiment Analysis with Hugging Face

This web application performs sentiment analysis on the text you provide. It's built using Streamlit and leverages the Hugging Face `transformers` library for the underlying sentiment analysis model.

https://miro.medium.com/v2/resize:fit:1200/1*HI4Kj_HQ-JYQHlLD-KSkDw.jpeg

![HuggingFace_Streamlit](https://miro.medium.com/v2/resize:fit:1200/1*HI4Kj_HQ-JYQHlLD-KSkDw.jpeg)

## Features

- **Easy-to-use interface**: A simple and intuitive UI to input text and get sentiment analysis results.
- **Live Analysis**: Get instant sentiment analysis of your text.
- **Responsive Design**: The app is designed to work on a wide range of devices, ensuring a good user experience.

## How to Use the App

1. Visit the app at [this link](https://sentiment-analysis-with-app-and-hugging-face-znsubeqzcfyqkqsbt.streamlit.app/).
2. You will see two main sections on the page: a larger left column for input and a smaller right column for results.
3. In the left column, **Enter Text Here**: Type or paste the text you want to analyze in the text area.
4. Click the **Analyze** button to process your text.
5. View the analysis results in the right column under **Analysis Result**. The sentiment (Positive, Negative, Neutral) will be displayed along with the confidence level of the analysis.

### Interpreting Results

- **Sentiment**: Indicates whether the sentiment of the text is Positive, Negative, or Neutral.
- **Confidence**: Shows how confident the model is about the sentiment analysis result, displayed as a percentage.

## Deployment

This app is currently deployed and accessible through Streamlit sharing. You can directly access it using the provided link.

## Local Setup

If you wish to run this app locally, follow these steps:

1. Clone the repository or download the files to your local machine.
2. Ensure you have Python installed and set up on your machine.
3. Install the required dependencies by running `pip install -r requirements.txt` in your terminal.
4. Start the app with `streamlit run app.py`.
5. Open your web browser and go to the local URL provided by Streamlit, usually `http://localhost:8501`.

Feel free to contribute to the app or suggest improvements by submitting a pull request or opening an issue on the GitHub repository.
