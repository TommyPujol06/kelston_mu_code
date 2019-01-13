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

def main(input_filepath, output_filepath="words.txt"):
    words = set()
    with open(input_filepath, encoding="utf8") as f:
        for line in f:
            for word in line.split():
                if len(word) < 4:
                    continue
                if word[0].isupper():
                    continue
                if not word.isalpha():
                    continue
                words.add(word.upper())

    with open(output_filepath, "w") as f:
        for word in sorted(words):
            f.write(word + "\n")

if __name__ == '__main__':
    main(*sys.argv[1:])
