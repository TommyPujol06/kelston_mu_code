import hangman_screen
import hangman_words

#
# Read a list of words
# Ask the user for a difficulty level (length of word)
# Pick a random one
# Loop until you win or you lose
#   Draw the current position
#   Ask for a letter
#   If the letter is good
#      Update the word-so-far
#   Otherwise
#      Update the failed-letters
#
#   If the word-so-far is complete
#      "You Win!"
#   If the failed-letters is too many
#      "You Lose!"
#
#