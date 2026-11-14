# Zachary Becsei
# CIS256 Fall 2026
# Programming Assignment 4

from guess_the_word import (
    WORDS,
    display_word,
    is_word_guessed,
    process_guess,
    select_word,
)

def test_selected_word_is_from_word_list():
    """Verify that the selected word comes from the predefined list."""
    selected_word = select_word()

    assert selected_word in WORDS

def test_correct_guess():
    """Verify that a correct guess is processed properly."""
    word = "python"
    guessed_letters = set()

    result = process_guess(word, guessed_letters, "p")

    assert result is True
    assert "p" in guessed_letters

def test_correct_guess():
    """Verify that a correct guess is processed properly."""
    word = "python"
    guessed_letters = set()

    result = process_guess(word, guessed_letters, "p")

    assert result is True
    assert "p" in guessed_letters

def test_incorrect_guess():
    """Verify that an incorrect guess is processed properly."""
    word = "python"
    guessed_letters = set()

    result = process_guess(word, guessed_letters, "z")

    assert result is False
    assert "z" in guessed_letters

def test_display_word_reveals_correct_letters():
    """Verify that correctly guessed letters are displayed."""
    word = "python"
    guessed_letters = {"p", "t"}

    result = display_word(word, guessed_letters)

    assert result == "p _ t _ _ _"


def test_repeated_letters_are_revealed():
    """Verify that every occurrence of a guessed letter is displayed."""
    word = "database"
    guessed_letters = {"a"}

    result = display_word(word, guessed_letters)

    assert result == "_ a _ a _ a _ _"


def test_letters_can_be_guessed_in_any_order():
    """Verify that letters can be guessed in any order."""
    word = "python"
    guessed_letters = {"n", "p", "o"}

    result = display_word(word, guessed_letters)

    assert result == "p _ _ _ o n"


def test_word_is_completely_guessed():
    """Verify that a completed word is recognized."""
    word = "python"
    guessed_letters = {"p", "y", "t", "h", "o", "n"}

    assert is_word_guessed(word, guessed_letters) is True


def test_word_is_not_completely_guessed():
    """Verify that an incomplete word is not considered guessed."""
    word = "python"
    guessed_letters = {"p", "y", "t"}

    assert is_word_guessed(word, guessed_letters) is False
