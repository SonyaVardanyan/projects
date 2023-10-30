#!/usr/bin/python3
import random

# List of words to choose from
word_list = ["python", "hangman", "programming", "computer", "gaming"]

# Choose a random word from the list
word_to_guess = random.choice(word_list)

# Convert the word to a list of characters
word_as_list = list(word_to_guess)

# Create a list to store the guessed letters
guessed_letters = []

# Set the number of allowed incorrect guesses
max_attempts = 6
attempts = 0

# Function to display the current state of the word with underscores for unguessed letters
def display_word(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
    return display

# Function to display the hangman figure
def display_hangman(attempts):
    stages = [
        """
           --------
           |      |
           |      O
           |
           |
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     /
           |
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
        """,
    ]
    
    return stages[attempts]

# Main game loop
while True:
    print("\nWord to guess:", display_word(word_to_guess, guessed_letters))
    print(display_hangman(attempts))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_as_list:
        print("Good guess!")
    else:
        print("Incorrect guess.")
        attempts += 1

    if attempts >= max_attempts:
        print("You ran out of attempts. The word was:", word_to_guess)
        break

    if set(guessed_letters) == set(word_as_list):
        print("Congratulations! You guessed the word:", word_to_guess)
        break

