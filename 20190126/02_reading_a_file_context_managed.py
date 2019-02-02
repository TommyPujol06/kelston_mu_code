import os
HERE = os.path.dirname(__file__)

with open(os.path.join(HERE, "high_scores.csv"), "r") as f:
    for line in f:
        print(line)