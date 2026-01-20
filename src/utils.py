import pandas as pd

def build_summary_table(tokens, stems, lemmas, pos_tags, spacy_results):
    """Create a pandas DataFrame comparing all transformations."""
    df = pd.DataFrame({
        "Word": tokens,
        "Porter": stems["Porter"],
        "Lancaster": stems["Lancaster"],
        "Snowball": stems["Snowball"],
        "Lemma (n)": lemmas["noun"],
        "Lemma (v)": lemmas["verb"],
        "POS": [p[1] for p in pos_tags],
        "spaCy Lemma": spacy_results["lemmas"],
        "spaCy POS": spacy_results["pos"]
    })
    return df
