from src.tokenizer import tokenize_text

def test_tokenize_text_basic():
    text = "Hello world!"
    tokens = tokenize_text(text)
    assert "Hello" in tokens
    assert "world" in tokens
    assert "!" in tokens
