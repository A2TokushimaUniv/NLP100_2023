def test_パトカータクシー():
    text1 = "パトカー"
    text2 = "タクシー"
    fragments = [t1+t2 for t1, t2 in zip(text1, text2)]
    result = "".join(fragments)
    assert result == "パタトクカシーー"
