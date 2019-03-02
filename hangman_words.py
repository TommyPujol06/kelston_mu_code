import random
import os, sys 

def read_possible_words():
    """Return a list of words read from a file
    """

    all_words = []

    with open("tommys_words.txt","r") as words_file:

        for word in words_file:

            all_words.append(word.strip())

    return all_words



def pick_a_word(words, n_letters=7):
    """Return a random word from the list of words
    of the preferred length

    words -> list of valid words
    n_letters -> how long a word to return
    """

    while True:

        random_num = random.randint(0,len(words)- 1)

        if len(words[random_num]) == n_letters:

            return words[random_num]
            break
            
 

def letter_is_good(letter, word):
    """Return whether a letter is good or failed
    """

    if letter in word.upper():
 	
        return True

    else:
 	
        return False



def update_word_so_far(real_word, word_so_far, guessed_letter):
    """Using the word so far and the chosen letter,
    return a new version of the word so far with the
    letter in the correct places.
    """
	
    dashed_word = word_so_far = ""


    for letter_or_dash in str(real_word):

        if letter_or_dash in guessed_letter:

            dashed_word += guessed_letter

        else:

            dashed_word += "_"

	
    return list(dashed_word)
    
    """	

    dashed_word = word_so_far = ""
	
	# every_item_in_the_guessed_letters_list
	
    for with_letter_or_dash in range(len(real_word)):

        if real_word[with_letter_or_dash] == guessed_letter:

            dashed_word += guessed_letter

        else:

				dashed_word += "_"
	"""


def update_failed_letters(failed_letters, letter):
    """Return the list of failed letters with the
    chosen letter added
    """
     	
    #if not letter in failed_letters:
 	
    failed_letters = [] = failed_letters.append(letter)
 	
    return failed_letters
 	
    #else:
 	
    #   failed_letters = failed_letters.append(letter)
 	
		#error = "Repeated Letter !!!"
    #    return failed_letters #, error
 	
		# Anyway would add the letter to the list but just a interesting thing to do.
 
if __name__ == "__main__":
    import testfile as t
    sys.exit(t.test())
