import random

def hangman():
    # Predefined word list
    words = ["python", "hangman", "random", "program", "simple"]
    word = random.choice(words)   # Pick a random word
    guessed_letters = []          # Letters the player has guessed
    attempts = 6                  # Maximum incorrect guesses allowed
    guessed_word = ["_"] * len(word)  # Word display (with underscores)

    print(" Welcome to Hangman!")
    print("Guess the word:")
    print(" ".join(guessed_word))

    # Game loop
    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠ You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(" Good guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f" Wrong guess! Attempts left: {attempts}")

        print(" ".join(guessed_word))
        print(f"Guessed letters: {', '.join(guessed_letters)}")

    # Game over check
    if "_" not in guessed_word:
        print("\n Congratulations! You guessed the word:", word)
    else:
        print("\n Game Over! The word was:", word)

# Run the game
hangman()