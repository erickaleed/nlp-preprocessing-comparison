from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer

def compare_stemmers(tokens):
    """Return a dictionary of stemmer outputs for each token."""
    stemmers = {
        "Porter": PorterStemmer(),
        "Lancaster": LancasterStemmer(),
        "Snowball": SnowballStemmer("english")
    }

    results = {name: [] for name in stemmers}

    for name, stemmer in stemmers.items():
        for word in tokens:
            results[name].append(stemmer.stem(word))

    return results
