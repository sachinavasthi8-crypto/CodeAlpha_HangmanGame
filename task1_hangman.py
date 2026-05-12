import random

# Predefined word list
WORDS = ["python", "laptop", "cricket", "mango", "keyboard"]

# Hangman stages (6 wrong guesses allowed)
HANGMAN = [
    """
   -----
   |   |
       |
       |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
       |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
   |   |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|   |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\  |
       |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\  |
  /    |
       |
=========""",
    """
   -----
   |   |
   O   |
  /|\  |
  / \  |
       |
========="""
]

def play_hangman():
    # Random word choose karo
    word = random.choice(WORDS)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("\n🎮 HANGMAN GAME MEIN AAPKA SWAGAT HAI!")
    print("=" * 40)

    while wrong_guesses < max_wrong:
        # Hangman display karo
        print(HANGMAN[wrong_guesses])

        # Word display karo (guessed letters dikhao, baaki _ dikhao)
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(f"\nWord: {display_word}")
        print(f"Wrong Guesses Bache: {max_wrong - wrong_guesses}")
        print(f"Galat Letters: {', '.join(guessed_letters) if guessed_letters else 'Abhi koi nahi'}")

        # Check karo kya word complete ho gayi
        if "_" not in display_word:
            print("\n🎉 BADHAAI HO! Aapne word guess kar liya:", word.upper())
            break

        # User se letter lo
        guess = input("\nEk letter daalo: ").lower().strip()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Sirf ek letter daalo!")
            continue

        if guess in guessed_letters:
            print("⚠️  Ye letter pehle se try kar chuke ho!")
            continue

        guessed_letters.append(guess)

        # Check karo letter sahi hai ya galat
        if guess in word:
            print(f"✅ Sahi! '{guess}' word mein hai!")
        else:
            wrong_guesses += 1
            print(f"❌ Galat! '{guess}' word mein nahi hai!")

    else:
        # Game over
        print(HANGMAN[max_wrong])
        print(f"\n💀 GAME OVER! Sahi word tha: {word.upper()}")

    # Dobara khelna chahte ho?
    play_again = input("\nDobara khelna chahte ho? (haan/nahi): ").lower()
    if play_again == "haan" or play_again == "h":
        play_hangman()
    else:
        print("\n👋 Khelte rehna! Bye!")

# Game start karo
if __name__ == "__main__":
    play_hangman()
