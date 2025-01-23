
# Example function for integrating the summarization model into an API
def summarize_document_for_case_review(legal_document):
    cleaned_doc = clean_text(legal_document)
    summary = text_rank_summary(cleaned_doc)
    entities, dependencies = extract_entities_and_dependencies(legal_document)
    return summary, entities, dependencies

# Example usage
legal_case = """
    The defendant, Acme Corp, is accused of violating antitrust laws in the market for cloud storage services.
    The case involves complicated legal precedents regarding monopolistic practices.
"""
summary, entities, dependencies = summarize_document_for_case_review(legal_case)
print("Summary:", summary)
print("Entities:", entities)
print("Dependencies:", dependencies)
