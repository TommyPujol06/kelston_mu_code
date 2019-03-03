import hangman_screen
from hangman_words import read_possible_words, pick_a_word, letter_is_good, update_word_so_far, update_failed_letters
import time
# Read a list of words
word_list = read_possible_words()

# Ask the user for a difficulty level (length of word)
difficulty = hangman_screen.get_difficulty()

# Pick a random one(giving Tommy values)
random_word = pick_a_word(word_list, int(difficulty))

# Loop until you win or you lose
word_so_far = []
failed_letters = []

while True: # alive from old Davide's code 

    #   Draw the current position
    #print(type(failed_letters))
    current_pos = hangman_screen.draw(word_so_far, failed_letters)

    #   Ask for a letter
    letter = hangman_screen.get_a_letter()

    #   If the letter is good
    if letter_is_good(letter, random_word):

        #      Update the word-so-far        
        #print("where we landing lads")
        word_so_far.append(letter)
        word_so_far = update_word_so_far(random_word, word_so_far)
        
    else:
        
        #      Update the failed-letters
        #print("GG")
        failed_letters = update_failed_letters(failed_letters, letter)

#   If the word-so-far is complete
    if list(random_word) == word_so_far:
        hangman_screen.win_or_lose(True)
        #print("YOU WIN!")
        time.sleep(5)
        break
		
#   If the failed-letters is too many
    if len(failed_letters) == hangman_screen.NUMBER_TO_FAIL:
        hangman_screen.win_or_lose(False)
        #print("YOU LOSE!")
        time.sleep(5)
        break
#      "You Lose!"
