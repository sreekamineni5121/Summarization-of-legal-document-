
import spacy

# Load SpaCy's pre-trained model for NER
nlp = spacy.load("en_core_web_sm")

# Function to extract named entities and syntactic dependencies
def extract_entities_and_dependencies(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    dependencies = [(token.text, token.dep_) for token in doc]
    return entities, dependencies

# Example text
legal_text = """
    The plaintiff, John Smith, is suing the defendant, Jane Johnson, for patent infringement concerning an AI technology.
"""

# Extract entities and dependencies
entities, dependencies = extract_entities_and_dependencies(legal_text)
print("Entities:", entities)
print("Dependencies:", dependencies)
