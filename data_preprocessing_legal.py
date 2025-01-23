
import spacy
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Sample legal document text
document = """
    In the case of Smith vs. Johnson, the plaintiff claims that the defendant unlawfully infringed upon his intellectual property rights, 
    specifically patent rights for an invention related to machine learning algorithms. The court must determine whether the defendant 
    acted in bad faith, and if so, appropriate remedies, including damages, should be applied.
"""

# Clean the document (remove special characters, extra spaces, and stop words)
def clean_text(text):
    # Remove special characters and extra spaces
    text = re.sub(r"[^A-Za-z0-9\s]+", "", text)
    # Tokenize and remove stop words
    doc = nlp(text)
    cleaned_text = " ".join([token.text for token in doc if token.text.lower() not in ENGLISH_STOP_WORDS])
    return cleaned_text

cleaned_document = clean_text(document)
print(cleaned_document)
