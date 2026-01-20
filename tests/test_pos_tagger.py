from src.pos_tagger import tag_pos

def test_tag_pos():
    tokens = ["dog"]
    tags = tag_pos(tokens)
    assert tags[0][0] == "dog"
    assert isinstance(tags[0][1], str)
