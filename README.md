# AI-Powered Fake News Detector

This project is an AI-powered web app that detects whether a given news headline or article is **real** or **fake**, using Natural Language Processing (NLP) and machine learning techniques.

## Features

- Input any news statement
- Predict whether it's Real or Fake
- Built using Python, Streamlit, and Scikit-learn
  


## Dataset

- Used a public dataset containing real and fake news articles
- Dataset source: Kaggle Fake News Dataset (up to 2017)

## Technologies Used

- Python
- Scikit-learn
- Pandas
- Numpy
- Streamlit
- Pickle (for model saving/loading)

## How it Works

1. The dataset is cleaned and preprocessed (removing stopwords, stemming, etc.)
2. A TF-IDF vectorizer converts text into numerical format
3. A Random Forest Classifier predicts the label (real/fake)
4. The model and vectorizer are saved using pickle.
