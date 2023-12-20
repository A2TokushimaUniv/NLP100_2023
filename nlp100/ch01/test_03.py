def clean_text(text: str):
    return text.replace(',', '').replace('.', '')

def test_円周率():
    text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    fragments = text.split(' ')
    result = [len(clean_text(fragment)) for fragment in fragments]
    assert result == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
