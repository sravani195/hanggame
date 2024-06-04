import random

def select_random_word():
    words = ["python", "java","flight","large","kotlin", "javascript"]
    return random.choice(words)

def display_current_state(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    print("Current word: ", display)
    return display

def hangman_game():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while incorrect_guesses < max_incorrect_guesses:
        display = display_current_state(word, guessed_letters)
        
        if display == word:
            print("Congratulations! You've guessed the word correctly.")
            break

        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, {guess} is not in the word. You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

    if incorrect_guesses == max_incorrect_guesses:
        print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    hangman_game()