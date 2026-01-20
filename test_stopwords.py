from src.stopwords import remove_stopwords

def test_remove_stopwords():
    tokens = ["This", "is", "a", "test"]
    filtered = remove_stopwords(tokens)
    assert "This" in filtered
    assert "test" in filtered
    assert "is" not in filtered
    assert "a" not in filtered
