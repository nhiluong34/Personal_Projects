import random

import hangman_words
import hangman_art

word_list = hangman_words.word_list

lives = 6

logo = hangman_art.logo
print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""
    already_guess = []
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            already_guess.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            already_guess.append(guess)
            display += "_"
    if guess in already_guess:
        print(f"You've already guessed '{guess}'.")

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    stages = hangman_art.stages
    print(stages[lives])
