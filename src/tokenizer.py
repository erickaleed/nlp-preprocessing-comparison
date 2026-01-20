from nltk.tokenize import word_tokenize

def tokenize_text(text: str):
    """Return a list of tokens using nltk's word_tokenize."""
    return word_tokenize(text)
