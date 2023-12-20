import re

def is_lower_alphabet(char: str):
    pattern = "[a-z]"
    result = re.match(pattern, char)
    return result is not None

def cipher(text: str):
    fragments = []
    for char in text:
        if is_lower_alphabet(char):
            fragments.append(str(219-ord(char)))
        else:
            fragments.append(char)
    result = "".join(fragments)
    return result

def test_暗号文():
    text = "abc123"
    result = cipher(text)
    assert result == f"{219-ord('a')}{219-ord('b')}{219-ord('c')}123"
