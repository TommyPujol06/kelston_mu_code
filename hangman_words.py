def read_possible_words():
    """Return a list of words read from a file
    """
    #print("I don't do anything yet")

    with open("words.txt","r") as words_file:

        for lines in words_file:

            separate_words = lines.split()

        return separate_words



def pick_a_word(words, n_letters=7):
    """Return a random word from the list of words
    of the preferred length

    words -> list of valid words
    n_letters -> how long a word to return
    """
    print("I don't do anything yet")
    if len(words) == n_letters:

        return words


def letter_is_good(letter, word):
    """Return whether a letter is good or failed
    """
    #print("I don't do anything yet")

    correct = True
    incorrect = False

    word_in_letters = word.split()

    for correct_letter in word:

        if word_in_letters == letter:

            letter_is_good = correct
            return letter_is_good, letter

        else:

            letter_is_good = incorrect
            return letter_is_good, letter

def update_word_so_far(real_word, word_so_far, letter):
    """Using the word so far and the chosen letter,
    return a new version of the word so far with the
    letter in the correct places.
    """
    #print("I don't do anything yet")

    pass




def update_failed_letters(failed_letters, letter):
    """Return the list of failed letters with the
    chosen letter added
    """
    #print("I don't do anything yet")








