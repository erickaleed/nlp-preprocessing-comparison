from src.utils import build_summary_table
from src.stemmer_comparison import compare_stemmers
from src.lemmatizer_comparison import compare_lemmatizers
from src.pos_tagger import tag_pos
from src.spacy_comparison import spacy_pipeline

def test_build_summary_table():
    tokens = ["testing"]
    stems = compare_stemmers(tokens)
    lemmas = compare_lemmatizers(tokens)
    pos_tags = tag_pos(tokens)
    spacy_results = spacy_pipeline("testing")

    df = build_summary_table(tokens, stems, lemmas, pos_tags, spacy_results)
    assert "Word" in df.columns
    assert df.shape[0] == 1
