import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
from datetime import datetime
import glob


def entry_analyser():
    filepaths = glob.glob("entries/*.txt")
    scores = []
    dates = []
    analyzer = SentimentIntensityAnalyzer()

    for filepath in filepaths:
        with open(filepath, "r") as file:
            content = file.read()
            score = analyzer.polarity_scores(content)
            scores.append(score)

            date = str(filepath)[8:26]
            date_frmt = "%Y-%m-%d - %H-%M"
            date_formatted = datetime.strptime(date, date_frmt)

            dates.append(date_formatted)

    return scores, dates


scores, dates = entry_analyser()

# Extract positive and negative scores
pos_scores = []
neg_scores = []
for entry in scores:
    pos_score = entry["pos"]
    pos_scores.append(pos_score)

    neg_score = entry["neg"]
    neg_scores.append(neg_score)

# Streamlit widgets
st.title("Diary mood graphs")
st.subheader("Positive scores")
# positive graph
figure = px.line(x=dates, y=pos_scores, labels={"x": "Date and time", "y": "positive score"})
st.plotly_chart(figure)

st.subheader("Negative scores")
# negative graph
figure = px.line(x=dates, y=neg_scores, labels={"x": "Date and time", "y": "positive score"})
st.plotly_chart(figure)
