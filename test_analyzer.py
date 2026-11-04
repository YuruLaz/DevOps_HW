from analyzer import count_words, count_characters, count_vowels, reverse_text


def test_count_words():
    assert count_words("hello world") == 2


def test_count_characters():
    assert count_characters("hello world") == 11


def test_count_vowels():
    assert count_vowels("hello world") == 3


def test_reverse_text():
    assert reverse_text("hello") == "olleh"
