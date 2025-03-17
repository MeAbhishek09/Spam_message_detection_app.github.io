# Spam Message Detection App

## 📌 Overview

The **Spam Message Detection App** is a machine learning-based web application that classifies messages as either **ham (not spam)** or **spam**. This project integrates **machine learning** with **web development**, allowing users to input messages and get real-time spam detection results.

## 🛠 Features

- **Machine Learning Model**: Uses an ML algorithm to detect spam messages.
- **Web Integration**: User-friendly web interface for message classification.
- **Real-time Prediction**: Instant classification of messages as spam or ham.
- **Data Processing**: Preprocessing and feature extraction for accurate classification.
- **Feature Extraction**: Tokenization, TF-IDF vectorization, and stopword removal to improve model accuracy.
- **Dataset Statistics**: Provides insights into spam vs. ham message distribution.

## 📂 Project Structure

```
├── dataset/              # Dataset used for training
├── models/               # Trained ML models
├── web_app/              # Web application files
│   ├── static/           # CSS, JS files
│   ├── templates/        # HTML templates
│   ├── app.py           # Flask web application
├── spam_detection.ipynb  # Jupyter Notebook with ML model training
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

## 📊 Dataset & Preprocessing

The dataset consists of **5,572 messages**, where:

- **4,827** messages are **ham** (not spam)
- **745** messages are **spam**

### 🔹 Data Cleaning & Preprocessing Steps:

1. **Lowercasing**: Convert text to lowercase for uniformity.
2. **Removing Special Characters & Punctuation**: Filters unnecessary symbols.
3. **Tokenization**: Splits messages into individual words.
4. **Removing Stopwords**: Eliminates common words that do not contribute to meaning.
5. **TF-IDF Vectorization**: Converts text into numerical representation for the ML model.

## 📊 Data Visualization

### 1️⃣ Frequent Words in Ham Messages
A bar chart showcasing the most commonly used words in **ham (non-spam)** messages:

![image](https://github.com/user-attachments/assets/be484d42-84fe-4445-9069-b096755c6178)


### 2️⃣ Word Clouds for Spam and Ham Messages
Word clouds give an intuitive visualization of the most common words appearing in spam and ham messages.

- **Spam Messages Word Cloud** (Top frequent words in spam messages):

 ![image](https://github.com/user-attachments/assets/8ec1f724-9922-4052-800d-b7eb3e952817)



- **Ham Messages Word Cloud** (Top frequent words in non-spam messages):

  ![Ham Word Cloud]![image](https://github.com/user-attachments/assets/566e64d2-762f-4cdb-b5b3-4f36ea4d49a2)


### 3️⃣ Pairplot Analysis
A pairplot showing relationships between numerical features such as **number of characters, words, and sentences** in spam vs. ham messages:

![image](https://github.com/user-attachments/assets/55df158e-aba4-4f50-bbb0-d93d5148b1b3)


This visualization helps in understanding the distribution and correlations between different features used in spam detection.

## 🏗 Technologies Used

- **Python** (Flask for web development)
- **Machine Learning** (Scikit-learn, NLP techniques)
- **HTML, CSS, JavaScript** (Frontend development)

## 📸 Output Screenshot

Below is an example of the app classifying a message as spam:

![Screenshot (2)](https://github.com/user-attachments/assets/d2a94fba-e373-4a2d-a129-452696038206)


## 🤝 Contributing

Feel free to fork the repository, create a new branch, and submit a pull request with improvements!

## 📧 Contact

For queries, reach out via [**LinkedIn**](https://www.linkedin.com/in/abhishek-835b5632b/) or open an issue in the repository.

---

Made by Abhishek
