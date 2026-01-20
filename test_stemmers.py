from src.stemmer_comparison import compare_stemmers

def test_compare_stemmers():
    tokens = ["running"]
    results = compare_stemmers(tokens)
    assert "run" in results["Porter"][0]
    assert len(results) == 3
