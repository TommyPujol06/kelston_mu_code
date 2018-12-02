Hangman I: Generate some words
==============================

Introduction
------------

In order for the computer to be able to play Hangman, either
as the player who chooses the word or as the one which guesses,
it must have access to a list of words.

We did this by selecting some texts with a lot of words (eg classic
novels from Gutenberg) and extracting the words. The plan later is
to filter out short or capitalised words.

Techniques
----------

In this session we opened files for reading, read their contents
as a string, split that string into words, and then stored all those
words in a file -- having made them uppercase -- in alphabetical order.

The program we generated is `here <https://github.com/KelstonClub/kelston_mu_code/blob/master/20181201/generate-words0.py>`_.
If you want to see something slightly more advanced, there is `a version <https://github.com/KelstonClub/kelston_mu_code/blob/master/20181201/generate-words2.py>`_
which adds to the existing set of words new ones which aren't there yet.

We used
~~~~~~~

* `open <https://docs.python.org/3.6/library/functions.html?highlight=open#open>`_ 
  to open a file so it could be read or written
* `read <https://docs.python.org/3.6/library/io.html#io.TextIOBase.read>`_
  to read the data from a file in one go
* `write <https://docs.python.org/3.6/library/io.html#io.TextIOBase.write>`_
  to write words back into a file one line at a time
* `split <https://docs.python.org/3.6/library/stdtypes.html?highlight=split#str.split>`_
   to split the string containing all the text into a list of individual words
* `sorted <https://docs.python.org/3.6/library/functions.html?highlight=sorted#sorted>`_ 
  to take the list of words and return it in alphabetical order
* `upper <https://docs.python.org/3.6/library/stdtypes.html?highlight=upper#str.upper>`_ 
  to turn each word into all uppercase (capital letters)

I also mentioned
~~~~~~~~~~~~~~~~

* `Asterisk words <https://en.wikipedia.org/wiki/Asterisk#Linguistics>`_ 
  which are words that linguists assume might have existed even though they haven't found them
* `The use of "if __name__ == '__main__'" <https://docs.python.org/3.6/library/__main__.html>`_ 
  which is how you can have code which happens when a module is run but not when it is imported by another module
* `Encodings (especially utf-8) <https://unicodebook.readthedocs.io/definitions.html>`_
  which are how non-English characters are stored so they be read back by other programs
* `UTF-8 Byte-order mark <https://en.wikipedia.org/wiki/Byte_order_mark>`_
  which is a pair of bytes at the start of a file to indicate that it's storing UTF-8

... and also
~~~~~~~~~~~~

* `Linguini <https://github.com/Linguini2004>`_ spotted a bug in the Mu editor and raised 
  an `issue on the tracker <https://github.com/mu-editor/mu/issues/715>`_.
