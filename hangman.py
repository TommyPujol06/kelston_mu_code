import random

with open("words.txt", encoding="utf-8") as f:
    words = f.read().split()
chosen_word = random.choice(words)
correct_word = list(chosen_word)
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
    print("The word was:", chosen_word)