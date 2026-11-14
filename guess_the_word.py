# Zachary Becsei
# CIS256 Fall 2026
# Programming Assignment 4

import random

# List of possible words for the game
WORDS = [
    "python",
    "computer",
    "programming",
    "database",
    "network",
    "software",
]


def select_word():
    """Select and return a random word from the word list."""
    return random.choice(WORDS)


def process_guess(word, guessed_letters, guess):
    """Process a letter guessed by the player."""
    guessed_letters.add(guess)

    if guess in word:
        return True

    return False


def display_word(word, guessed_letters):
    """Display guessed letters and hide unguessed letters."""
    displayed_letters = []

    for letter in word:
        if letter in guessed_letters:
            displayed_letters.append(letter)
        else:
            displayed_letters.append("_")

    return " ".join(displayed_letters)


def is_word_guessed(word, guessed_letters):
    """Check whether every letter in the word has been guessed."""
    return all(letter in guessed_letters for letter in word)


def get_valid_guess(guessed_letters):
    """Ask the player for a valid letter that has not been guessed."""
    while True:
        guess = input("Guess one letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter only.")
        elif guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            return guess


def play_game():
    """Run the word guessing game."""
    word = select_word()
    guessed_letters = set()
    incorrect_guesses = 0
    maximum_attempts = 6

    print("Welcome to the Word Guessing Game!")
    print(f"You have {maximum_attempts} incorrect attempts.")

    # Continue until the word is guessed or attempts run out
    while (
        not is_word_guessed(word, guessed_letters)
        and incorrect_guesses < maximum_attempts
    ):
        print()
        print("Word:", display_word(word, guessed_letters))
        print(
            "Attempts remaining:",
            maximum_attempts - incorrect_guesses,
        )

        guess = get_valid_guess(guessed_letters)

        if process_guess(word, guessed_letters, guess):
            print("Correct guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess.")

    # Display the final result of the game
    print()
    print("Word:", display_word(word, guessed_letters))

    if is_word_guessed(word, guessed_letters):
        print(f"Congratulations! You guessed the word '{word}'.")
    else:
        print(f"You ran out of attempts. The word was '{word}'.")
        

if __name__ == "__main__":
    play_game()
