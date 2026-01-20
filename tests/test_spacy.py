from src.spacy_comparison import spacy_pipeline

def test_spacy_pipeline():
    text = "Testing the pipeline."
    results = spacy_pipeline(text)
    assert "Testing" in results["tokens"]
    assert len(results["lemmas"]) == len(results["tokens"])
