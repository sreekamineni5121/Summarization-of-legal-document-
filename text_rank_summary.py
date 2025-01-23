
import spacy
from summa import summarizer

# Load the SpaCy model for NLP tasks
nlp = spacy.load("en_core_web_sm")

# Use the TextRank algorithm for summarization
def text_rank_summary(text):
    summary = summarizer.summarize(text)
    return summary

# Test with a sample document
legal_document = """
    In the case of Smith vs. Johnson, the plaintiff claims that the defendant unlawfully infringed upon his intellectual property rights, 
    specifically patent rights for an invention related to machine learning algorithms. The court must determine whether the defendant 
    acted in bad faith, and if so, appropriate remedies, including damages, should be applied. Furthermore, the defendant denies any such 
    infringement and asserts that the plaintiff has failed to prove any unlawful activity.
"""

summary = text_rank_summary(legal_document)
print(summary)
