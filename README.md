# 🎬 IMDB Movie Review Sentiment Analysis using Simple RNN

An end-to-end **Natural Language Processing (NLP)** project that uses a **Simple Recurrent Neural Network (RNN)** to classify IMDB movie reviews as **Positive** or **Negative**.

The project includes text preprocessing, sequence padding, RNN model training, evaluation, and a **Streamlit web application** for real-time sentiment prediction.

---

## 🚀 Live Demo

🌐 **Streamlit App:**
https://simple-rnn-imdb-sentiment-analysis.streamlit.app/

Enter a movie review and the application predicts its sentiment along with the model's prediction score.

---

## 📌 Project Overview

Sentiment Analysis is an NLP task used to determine whether a piece of text expresses a positive or negative opinion.

In this project, a **Simple RNN** is trained on the **IMDB movie review dataset** to understand the relationship between words in a sequence and predict the sentiment of movie reviews.

### Example

```text
Input:
"This movie was amazing. The story and acting were excellent."

Output:
Positive 😊
```

---

## 🧠 Concepts Covered

* Natural Language Processing (NLP)
* IMDB Movie Review Dataset
* Text Tokenization
* Vocabulary and Word Indexing
* Sequence Padding
* Word Embeddings
* Recurrent Neural Networks (RNN)
* Binary Classification
* Model Evaluation
* TensorFlow / Keras
* Streamlit Deployment

---

## 🔄 Project Workflow

```text
IMDB Dataset
      ↓
Text / Integer Encoding
      ↓
Vocabulary Limitation
      ↓
Sequence Padding
      ↓
Embedding Layer
      ↓
Simple RNN
      ↓
Dense Output Layer
      ↓
Sigmoid Prediction
      ↓
Positive / Negative Sentiment
```

---

## 📊 Dataset

The project uses the **IMDB Movie Reviews Dataset** available through TensorFlow/Keras.

The dataset contains movie reviews labeled as:

* `0` → Negative
* `1` → Positive

The vocabulary is limited to the **10,000 most frequently used words**, and each review is padded/truncated to a maximum length of **500 tokens**.

---

## 🏗️ Model Architecture

The model uses a simple neural network architecture:

```text
Input Sequence
      ↓
Embedding Layer
      ↓
Simple RNN Layer
      ↓
Dense Layer
      ↓
Sigmoid Output
```

### Main Components

**Embedding Layer**

Converts integer word representations into dense numerical vectors that can capture useful relationships between words.

**Simple RNN**

Processes the sequence of word representations and maintains information from previous words while reading the review.

**Dense + Sigmoid**

Produces a value between `0` and `1` representing the model's predicted probability for the positive class.

```text
Score > 0.5  → Positive 😊
Score ≤ 0.5  → Negative 😞
```

---

## 🔧 Text Preprocessing

For a user-entered review, the application:

1. Converts the text to lowercase.
2. Splits the review into words.
3. Converts words into their IMDB vocabulary indices.
4. Maps words outside the model vocabulary to the unknown-token index.
5. Pads the sequence to a length of 500.
6. Passes the processed sequence to the trained RNN model.

This ensures that the input format is consistent with the model used during training.

---

## 💻 Technologies Used

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| Python       | Programming language           |
| TensorFlow   | Deep learning framework        |
| Keras        | Model development              |
| NumPy        | Numerical operations           |
| Streamlit    | Web application and deployment |
| IMDB Dataset | Sentiment analysis dataset     |

---

## 📂 Project Structure

```text
Simple-RNN/
│
├── main.py
├── simple rnn.ipynb
├── simple_rnn_imdb.h5
├── requirements.txt
├── README.md
└── .gitignore
```

### File Description

**`main.py`**
Streamlit application that loads the trained model, preprocesses user reviews, and performs sentiment prediction.

**`simple rnn.ipynb`**
Jupyter Notebook containing the data preparation, model development, training, and experimentation.

**`simple_rnn_imdb.h5`**
Saved trained RNN model.

**`requirements.txt`**
Python dependencies required to run the project.

---

## ▶️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/AdityaJanagal/Simple-RNN.git
```

### 2. Navigate to the project directory

```bash
cd Simple-RNN
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run main.py
```

The application will open in your browser.

---

## 🧪 Example Predictions

### Positive Review

```text
This movie was absolutely fantastic.
The story was engaging and the acting was brilliant.
I loved every minute of it.
```

Expected:

```text
Sentiment: Positive 😊
```

### Negative Review

```text
This movie was extremely boring and disappointing.
The story was poorly written and the acting was terrible.
I completely regret watching it.
```

Expected:

```text
Sentiment: Negative 😞
```

---

## 📈 Model Output

The application displays the model's prediction score along with the predicted sentiment.

For example:

```text
Sentiment: Positive 😊
Prediction Score: 0.6837
Positive Probability: 68.37%
```

The score represents the model's output for the positive class for that particular input. It should not be interpreted as the overall accuracy of the model.

---

## 🎯 Learning Outcomes

Through this project, I learned how to:

* Work with text data for NLP tasks.
* Convert words into numerical sequences.
* Handle vocabulary limitations.
* Use sequence padding for neural networks.
* Understand the basic working of RNNs.
* Build an NLP classification model using TensorFlow/Keras.
* Save and load trained deep learning models.
* Build an interactive prediction application using Streamlit.
* Deploy a deep learning application for real-time inference.

---

## 🔮 Future Improvements

Possible improvements include:

* Experimenting with LSTM and GRU architectures.
* Using pretrained word embeddings.
* Improving text preprocessing.
* Hyperparameter tuning.
* Comparing RNN, LSTM, and GRU performance.
* Adding prediction confidence visualization.
* Exploring Transformer-based sentiment analysis.

---

## 👨‍💻 Author

**Aditya Janagal**

B.Tech — Artificial Intelligence & Data Science

GitHub:
https://github.com/AdityaJanagal

---

⭐ If you found this project useful, consider giving the repository a star!
