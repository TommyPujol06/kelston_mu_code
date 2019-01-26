import os
os.chdir(r"C:\Users\tim\work-in-progress\kelston_mu_code\20190126")

with open("high_scores.csv") as f:
    for line in f:
        print(line.strip())

        words = []
        word_so_far = ""
        for c in line.strip():
            if c == ",":
                words.append(word_so_far)
                word_so_far = ""
            else:
                word_so_far += c
        words.append(word_so_far)
        print(words)