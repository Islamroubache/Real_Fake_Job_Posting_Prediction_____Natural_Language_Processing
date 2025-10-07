from flask import Flask, render_template_string, request  # type: ignore
import re
import string
import nltk  # type: ignore
import joblib  # type: ignore
from nltk.corpus import stopwords  # type: ignore
from nltk.stem import WordNetLemmatizer  # type: ignore
import os

# Initialize NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load the trained model (includes vectorizer and classifier)
best_model = joblib.load('bes_model.pkl')

# NLTK resources for stopwords and lemmatization
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Regular expression for cleaning emojis (using raw strings to fix unicode error)
emoji_pattern = re.compile(
    r"[\U00010000-\U0010FFFF"
    r"\u2640-\u2642"
    r"\u2600-\u26FF"
    r"\u2700-\u27BF"
    r"\u2300-\u23FF"
    r"\u2B50"
    r"\u203C"
    r"\u2049"
    r"]+",
    flags=re.UNICODE
)

# Function to clean and preprocess the job posting text
def clean_text(text):
    text = re.sub(emoji_pattern, "", text)
    text = text.replace('\r', '').replace('\n', ' ').lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'@\S+', '', text)
    text = re.sub(r'#\S+', '', text)
    text = re.sub(r'[^\x00-\x7f]', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [word for word in text.split() if word not in stop_words]
    text = ' '.join(text)
    text = ' '.join(word for word in text.split() if len(word) < 14)
    text = re.sub(r"can\'t", "can not", text)
    text = re.sub(r"n\'t", " not", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'s", " is", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'t", " not", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'m", " am", text)
    text = ' '.join(word for word in text.split() if ('$' not in word) and ('&' not in word))
    text = re.sub(r"\s\s+", " ", text)
    tokenized = nltk.word_tokenize(text)
    text = ' '.join([lemmatizer.lemmatize(word) for word in tokenized])
    return text

# Initialize Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        job_posting = request.form['job_posting']
        cleaned_text = clean_text(job_posting)
        pred = best_model.predict([cleaned_text])[0]
        prediction = "✅ Annonce Réelle" if pred == 0 else "⚠️ Annonce Frauduleuse"

    html_file_path = os.path.join(os.getcwd(), 'index.html')
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    return render_template_string(html_content, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
