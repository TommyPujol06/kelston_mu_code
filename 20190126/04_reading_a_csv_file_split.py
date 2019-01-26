import os
os.chdir(r"C:\Users\tim\work-in-progress\kelston_mu_code\20190126")

with open("high_scores.csv") as f:
    for line in f:
        print(line.strip())
        words = line.split(",")
        print(words)