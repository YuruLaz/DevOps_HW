def count_words(text):
    return len(text.split())


def count_characters(text):
    return len(text)


def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def reverse_text(text):
    return text[::-1]
