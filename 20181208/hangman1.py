import random

HANGMAN = "YOU-ARE-DEAD!"

def choose_random_word(words_filepath):
    with open("words.txt", encoding="utf-8") as f:
        words = f.read().split()
    return random.choice(words)

def get_letter():
    return input("Guess a letter: ").upper()

def check_letter(letter, chosen_word, guessed_word, hangman):
    word_so_far = guessed_word
    hangman_so_far = hangman

    positions = get_positions(letter, chosen_word)
    if positions:
        for p in positions:
            word_so_far[p] = letter
    else:
        hangman_so_far = HANGMAN[:1 + len(hangman_so_far)]

    return word_so_far, hangman_so_far

def main(words_filepath="words.txt"):
    chosen_word = list(choose_random_word(words_filepath))
    guessed_word = ["-" for c in correct_word]
    hangman = ""

    while (hangman != "HANGMAN") and (guessed_word != correct_word):
        print("So far:", guessed_word, "/", hangman)
        letter = get_letter()
        guessed_word, hangman = check_letter(letter, chosen_word, guessed_word, hangman)

    if guessed_word == correct_word:
        print("You win!")
    else:
        print("You lose! The word was:", correct_word)

if __name__ == '__main__':
    main(*sys.argv[1:])
