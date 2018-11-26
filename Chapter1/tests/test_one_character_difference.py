from Chapter1.OneCharacterDifference import is_one_char_away


def test_one_character_drop_char():
    assert is_one_char_away('pale', 'ple')


def test_one_character_add_char():
    assert is_one_char_away('pales', 'pale')


def test_one_character_replace_char():
    assert is_one_char_away('bale', 'pale')


def test_one_character_fail():
    assert not is_one_char_away('bake', 'pale')
