correct_word = list("FLOWER")
guessed_word = ["-" for c in correct_word]
letters_so_far = set()
hangman = ""

while (hangman != "HANGMAN") and (guessed_word != correct_word):
    letter = input("Guess a letter: ").upper()
    if letter in letters_so_far:
        print("You've already tried", letter)
    else:
        letters_so_far.add(letter)
        positions = [p for (p, l) in enumerate(correct_word) if letter == l]
        if positions:
            for p in positions:
                guessed_word[p] = letter
            print("".join(guessed_word))
        else:
            hangman = "HANGMAN"[:1 + len(hangman)]
            print("Wrong!")
            print(hangman)

if guessed_word == correct_word:
    print("Congratulations; you win!")
else:
    print("You die!")