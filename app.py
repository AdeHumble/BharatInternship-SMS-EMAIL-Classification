import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


ps = PorterStemmer()

def clean_message(msg):
    # Lowercase the text
    msg = msg.lower()

    # Tokenize the text
    msg_tokens = nltk.word_tokenize(msg)

    # Initialize stemmer
    ps = PorterStemmer()

    # Create a list to store cleaned tokens
    cleaned_tokens = []

    for token in msg_tokens:
        # Remove non-alphanumeric characters
        cleaned_token = ''.join(char for char in token if char.isalnum())
        if cleaned_token:
            cleaned_tokens.append(cleaned_token)

    # Remove stopwords and punctuation
    cleaned_tokens = [token for token in cleaned_tokens if
                      token not in stopwords.words('english') and token not in string.punctuation]

    # Stemming
    cleaned_tokens = [ps.stem(token) for token in cleaned_tokens]

    # Join the cleaned tokens into a string
    cleaned_text = " ".join(cleaned_tokens)

    # Remove non-ASCII characters
    cleaned_text = ''.join(char for char in cleaned_text if ord(char) < 128)

    return cleaned_text


try:
    tfidf_max = pickle.load(open('vectorizer.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading 'vectorizer.pkl': {e}")


model = pickle.load(open('model.pkl', 'rb'))

# The indented lines below might be useful for debugging purpose
# For Checking model characteristics
        #st.write("Model Type:", type(model))
        #st.write("Model Parameters:", model.get_params())

st.title('BHARAT VIRTUAL INTERNSHIP')
st.subheader('PROJECT NAME: SMS/EMAIL SPAM CLASSIFIER')
input_msg = st.text_area('PLease, enter your message here')

if st.button('Predict'):
    # preprocess
    transformed_msg = clean_message(input_msg)
    #st.write("Transformed Message:", transformed_msg)  # Add this line
    # vectorize
    vectorized_msg = tfidf_max.transform([transformed_msg])


    # predict
    result = model.predict(vectorized_msg)[0]
    # display
    if result == 1:
        #st.success('Not Spam')
        st.header('Spam')
    else:
        #st.success('Spam')
        st.header('Not Spam')

    # The indented line below might be useful for debugging purpose
    # In case, you want to compare the model result with your app output
            #st.write("Model Prediction:", 'Not Spam' if result == 0 else 'Spam')