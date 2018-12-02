"""Illustrate importing a module

This module contains a noddy function which returns the letters
which two words have in common.

It also contains a section which is guarded by the
"if __name__ == '__main__'" idiom and which is therefore
not execute when this module is imported. Although it *is*
executed if the module is run.
"""
def letters_in_common(w1, w2):
    return set(w1)&set(w2)

if __name__ == '__main__':
    print(letters_in_common("abc", "bcd"))