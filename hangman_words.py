import random

def read_possible_words():
    """Return a list of words read from a file
    """
    #print("I don't do anything yet")

    all_words = []

    with open("words.txt","r") as words_file:

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
        print(random_num)
        print(words[random_num])
        print(n_letters)
        if len(words[random_num]) == n_letters:
            return words[random_num]


def letter_is_good(letter, word):
    """Return whether a letter is good or failed
    """
    #print("I don't do anything yet")
    print(letter)
    print(word)
    if letter in word.upper():
        return True
    else:
        print(word)
        return False



def update_word_so_far(real_word, word_so_far, guessed_letter):
    """Using the word so far and the chosen letter,
    return a new version of the word so far with the
    letter in the correct places.
    """

    dashed_word = ""


    for letter_or_dash in str(real_word):

        if letter_or_dash in guessed_letter:

            dashed_word += guessed_letter

        else:

            dashed_word += "_"



    return list(dashed_word)



def update_failed_letters(failed_letters, letter):
    """Return the list of failed letters with the
    chosen letter added
    """
    #print("I don't do anything yet")



if __name__ == "__main__":
    read_possible_words()



