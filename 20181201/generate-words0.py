"""Generate a list of words usable by a hangman game

Take an input text file (expected to be, eg, a Gutenberg Dickens but could
be anything which has words). Extract all words which are:

* Are four letters long or more (to exclude short words)
* Do not start with a capital (to exclude proper names)
* Contain no apostrophes (to exclude ellided words like "can't" or "haven't")

Output the resulting words into a text file with one word per line. The words
should be capitalised and sorted. (The capitalisation is because that's how
they're going to be used in the game so it saves an extra step. The sorting is
optional but just helps the file be human-readable)

So a text such as this:

"There once was a boy called Eustace Clarence Scrubb and he didn't deserve it."

Will produce the file containing:

CALLED
DESERVE
ONCE

The missing words are either too short (was, a, boy, and, he, it) or start
with a capital letter (There, Eustace, Clarence, Scrubb) or have an apostrophe
(didn't)
"""
import os, sys

def get_words_from_text(text):
    """Take a chunk of text and return a list containing its words
    """
    return text.split()

def get_candidate_words(words):
    """Take a list of words and filters some out
    """
    return words

def write_words_to_file(words, filepath):
    """Take a list of words and write one line at a time to a file
    """
    new_file = open(filepath, "w", encoding="utf-8")
    sorted_words = sorted(set(words))
    for w in sorted_words:
        w = w.upper()
        new_file.write(w + "\n")
    new_file.close()
    
def main(input_filepath="bleak-house.txt", output_filepath="words.txt"):
    complete_text = open(input_filepath, "r", encoding="utf-8").read()
    separatewords = get_words_from_text(complete_text)    
    candidate_words = get_candidate_words(separatewords)
    write_words_to_file(candidate_words, output_filepath)


if __name__ == '__main__':
    main(*sys.argv[1:])