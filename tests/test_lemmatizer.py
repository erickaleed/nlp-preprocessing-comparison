from src.lemmatizer_comparison import compare_lemmatizers

def test_compare_lemmatizers():
    tokens = ["went"]
    results = compare_lemmatizers(tokens)
    assert results["verb"][0] == "go"
