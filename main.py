# Step 1: Import Libraries
import numpy as np
import tensorflow as tf
import streamlit as st

from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model


# Step 2: Load IMDB Word Index
word_index = imdb.get_word_index()


# Step 3: Load Trained Model
model = load_model("simple_rnn_imdb.h5")


# Step 4: Preprocess User Review
def preprocess_text(text):

    words = text.lower().split()

    encoded_review = []

    for word in words:

        # Get word index
        index = word_index.get(word, 2)

        # IMDB dataset encoding
        index = index + 3

        # IMPORTANT:
        # Model was trained with max_features = 10000
        # Therefore valid indices are 0 to 9999
        if index >= 10000:
            index = 2

        encoded_review.append(index)

    # Pad sequence to 500 words
    padded_review = sequence.pad_sequences(
        [encoded_review],
        maxlen=500
    )

    return padded_review


# Step 5: Streamlit UI
st.title("🎬 IMDB Movie Review Sentiment Analysis")

st.write(
    "Enter a movie review below and the model will classify it "
    "as Positive or Negative."
)


# Text input
user_input = st.text_area(
    "Movie Review",
    placeholder="Example: This movie was absolutely amazing..."
)


# Step 6: Classification
if st.button("Classify"):

    if user_input.strip() == "":
        st.warning("Please enter a movie review.")

    else:

        # Preprocess input
        preprocessed_input = preprocess_text(user_input)

        # Make prediction
        prediction = model.predict(preprocessed_input, verbose=0)

        score = float(prediction[0][0])

        # Classify sentiment
        if score > 0.5:
            sentiment = "Positive 😊"
        else:
            sentiment = "Negative 😞"

        # Display result
        st.subheader(f"Sentiment: {sentiment}")

        st.write(f"Prediction Score: {score:.4f}")

        # Show percentage
        if score > 0.5:
            st.success(f"Positive Probability: {score * 100:.2f}%")
        else:
            st.error(f"Positive Probability: {score * 100:.2f}%")