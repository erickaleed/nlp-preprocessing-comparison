from nltk.corpus import stopwords

def remove_stopwords(tokens):
    """Remove English stopwords from a list of tokens."""
    stop_words = set(stopwords.words("english"))
    return [t for t in tokens if t.lower() not in stop_words]
