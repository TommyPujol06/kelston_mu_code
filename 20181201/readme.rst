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

We used:
~~~~~~~~

* `open <https://docs.python.org/3.6/library/functions.html?highlight=open#open>`_
* `read <https://docs.python.org/3.6/library/io.html#io.TextIOBase.read>`_
* `write <https://docs.python.org/3.6/library/io.html#io.TextIOBase.write>`_
* `split <https://docs.python.org/3.6/library/stdtypes.html?highlight=split#str.split>`_
* `sorted <https://docs.python.org/3.6/library/functions.html?highlight=sorted#sorted>`_
* `upper <https://docs.python.org/3.6/library/stdtypes.html?highlight=upper#str.upper>`_

I also mentioned:
~~~~~~~~~~~~~~~~~

* `Asterisk words <https://en.wikipedia.org/wiki/Asterisk#Linguistics>`_
* `The use of "if __name__ == '__main__'" <https://docs.python.org/3.6/library/__main__.html>`_
* `Encodings (especially utf-8) <https://unicodebook.readthedocs.io/definitions.html>`_
* `UTF-8 Byte-order mark <https://en.wikipedia.org/wiki/Byte_order_mark>`_
