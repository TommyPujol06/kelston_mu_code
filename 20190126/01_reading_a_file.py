import os
HERE = os.path.dirname(__file__)

f = open(os.path.join(HERE, "high_scores.csv"), "r")
for cheese in f:
    print(cheese)
f.close()