# Bharat Virtual Internship - SMS/Email Spam Classifier

## Project Overview

This project aims to develop a text classification model for classifying SMS/Email messages as spam or non-spam. The model is built using natural language processing techniques and machine learning algorithms.

### Dataset

The dataset used in this project is sourced from [Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset/download?datasetVersionNumber=1). It contains information about SMS/Email messages and their classification as spam or non-spam.

## Steps and Methodologies

### 1. Data Cleaning and Initial Exploration

- Install necessary libraries (`nltk` and `wordcloud`).
- Import required libraries.
- Load the dataset and perform initial exploration.
- Handle inconsistencies in the dataset.
- Check for data type consistency.
- Drop unnecessary columns and rename columns for clarity.
- Transform the target variable for clarity.
- Check for and drop duplicate entries.

### 2. Exploratory Data Analysis (EDA)

- Explore basic statistics of the data.
- Check for imbalance between spam and non-spam classes.
- Visualize class distribution.
- Perform feature engineering, including the creation of new features.
- Explore various visualizations to understand feature relationships.

### 3. Data Preprocessing

- Create a function to clean and transform messages.
- Apply the cleaning function to the 'message' field.
- Visualize word clouds for each target variable.
- Analyze and visualize the top 20 words in each target variable.

### 4. Model Building

- Label encoding for the target variable.
- Model selection with various classifiers.
- Train and evaluate the models using different text vectorization techniques:
  - Count Vectorizer
  - TFIDF Vectorizer
  - TFIDF Vectorizer with max features

### 5. Model Training and Evaluation

- Compare evaluation metrics among models.
- Serialize the selected model for future use.

### 6. Model Deployment

...

## Running the PyCharm Code

For users who prefer working with PyCharm, the project includes Python scripts developed using the PyCharm IDE. Follow the steps below to run the code:

1. Open the PyCharm IDE.
2. Load the project into PyCharm.
3. Navigate to the Python script (`your_pycharm_script.py`) that contains the main code.
4. Execute the script to run the SMS/Email Spam Classifier.

Note: Ensure that you have the necessary Python dependencies installed using the provided `requirements.txt` file.

## Directory Structure

- `/data`: Contains the dataset used for training the model.
- `/notebooks`: Jupyter notebooks for data exploration and model development.
- `/scripts`: Python scripts for the final implementation of the SMS/Email Spam Classifier.
- `/streamlit`: Streamlit web application code.
- `/images`: Image files used in the README or other documentation.


## Running the Streamlit App

To run the Streamlit app, execute the provided Python script:

```bash
streamlit run https://github.com/AdeHumble/Bharat-Internship-Project2
/blob/main/app.py


