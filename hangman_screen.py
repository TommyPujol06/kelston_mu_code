NUMBER_TO_FAIL = 10

def draw(word_so_far, failed_letters):
    """Draw the word so far and the hangman

    (Might also draw the list of failed letters)
    Useful:
      reset -- starts again with a clear screen
      write -- writes text to the screen
    """
    print("So far:", "".join(word_so_far))
    print("Failed: ", ", ".join(failed_letters))

def get_a_letter():
    """Prompt the user to enter a letter
    """
    #
    # HINT: turtle.textinput might help
    #
    return input("Letter? ").upper()[0]
    print("I don't do anything yet")

def get_difficulty():
    return int(input("How difficult?"))
