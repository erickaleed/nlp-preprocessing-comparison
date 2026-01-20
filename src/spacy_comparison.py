import spacy

nlp = spacy.load("en_core_web_sm")

def spacy_pipeline(text: str):
    """Return spaCy tokens, lemmas, and POS tags."""
    doc = nlp(text)
    return {
        "tokens": [t.text for t in doc],
        "lemmas": [t.lemma_ for t in doc],
        "pos": [t.pos_ for t in doc]
    }


