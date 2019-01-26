import os
os.chdir(r"C:\Users\tim\work-in-progress\kelston_mu_code\20190126")
f = open("high_scores.csv", "r")
for cheese in f:
    print(cheese)
f.close()