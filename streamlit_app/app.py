import streamlit as st
import pandas as pd

from src.tokenizer import tokenize_text
from src.stopwords import remove_stopwords
from src.stemmer_comparison import compare_stemmers
from src.lemmatizer_comparison import compare_lemmatizers
from src.pos_tagger import tag_pos
from src.spacy_comparison import spacy_pipeline
from src.utils import build_summary_table

st.title("NLP Preprocessing Comparison Suite")

text = st.text_area("Enter text:", "We went again and had an even better experience!")

if st.button("Run NLP Pipeline"):
    tokens = tokenize_text(text)
    filtered = remove_stopwords(tokens)
    stems = compare_stemmers(filtered)
    lemmas = compare_lemmatizers(filtered)
    pos_tags = tag_pos(filtered)
    spacy_results = spacy_pipeline(text)

    df = build_summary_table(filtered, stems, lemmas, pos_tags, spacy_results)
    st.dataframe(df)

    st.subheader("Linguistic Difficulty Score")
    score = len(filtered) + len(set([p[1] for p in pos_tags])) + df.nunique().sum()
    st.write(f"Score: {score}")
