from nltk.stem import WordNetLemmatizer

def compare_lemmatizers(tokens):
    """Return noun and verb lemmatization results."""
    wnl = WordNetLemmatizer()

    lemmas_n = [wnl.lemmatize(t, pos="n") for t in tokens]
    lemmas_v = [wnl.lemmatize(t, pos="v") for t in tokens]

    return {"noun": lemmas_n, "verb": lemmas_v}
