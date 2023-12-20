def test_元素記号():
    text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    fragments = text.split(" ")
    result = {}
    for i, fragment in enumerate(fragments):
        index = i+1
        if index in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            result[fragment[0]] = index
        else:
            result[fragment[:2]] = index

    assert result == {
        "H": 1,
        "He": 2,
        "Li": 3,
        "Be": 4,
        "B": 5,
        "C": 6,
        "N": 7,
        "O": 8,
        "F": 9,
        "Ne": 10,
        "Na": 11,
        "Mi": 12, # Mg
        "Al": 13,
        "Si": 14,
        "P": 15,
        "S": 16,
        "Cl": 17,
        "Ar": 18,
        "K": 19,
        "Ca": 20,
    }
