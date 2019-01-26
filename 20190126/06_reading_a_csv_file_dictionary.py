import os
os.chdir(r"C:\Users\tim\work-in-progress\kelston_mu_code\20190126")
import csv

with open("high_scores.csv", newline="") as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line['Name'], "=>", line['Score'])