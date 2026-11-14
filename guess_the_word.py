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
