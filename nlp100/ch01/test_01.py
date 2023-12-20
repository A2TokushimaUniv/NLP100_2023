def test_パタトクカシーー():
    text = "パタトクカシーー"
    fragments = [text[0], text[2], text[4], text[6]]
    result = ''.join(fragments)
    assert result == "パトカー"
