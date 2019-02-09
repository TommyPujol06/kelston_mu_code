import os, sys
sys.path.append(os.path.dirname(__file__))
import hangman_screen     
import hangman_words
alive = True
word_so_far = []
failed_letters = []
correct = False


# Read a list of words
word_list = hangman_words.read_possible_words()

# Ask the user for a difficulty level (length of word)
difficulty = hangman_screen.get_difficuty()
    
# Pick a random one(giving Tommy values)
random_word = hangman_words.pick_a_word(word_list, int(difficulty))

# Loop until you win or you lose
word_so_far = ["_"] * difficulty
while alive == True:
    #   Draw the current position
    current_pos = hangman_screen.draw(words_so_far, failed_letters)
    #   Ask for a letter
    letter = hangman_screen.get_a_letter()
    #   If the letter is good
    if hangman_words.letter_is_good(letter, random_word):
        #      Update the word-so-far
        word_so_far = hangman_words.update_word_so_far(random_word, word_so_far, letter)
    else:
        #      Update the failed-letters
        failed_letters = hangman_words.update_failed_letters(failed_letters, letter)
#   If the word-so-far is complete
    if list(random_word) == word_so_far:
        print("YOU WIN!")


#   If the failed-letters is too many
    if len(failed_letters) == hangman_screen.NUMBER_TO_FAIL:
        print("YOU LOSE!")
#      "You Lose!"