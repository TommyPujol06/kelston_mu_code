import os
import glob
import gzip

for filepath in glob.glob("*.gz"):
    print(filepath)
    name, _ = os.path.splitext(filepath)
    print(name)
    with gzip.open(filepath, 'rb') as fin:
        with open(name, "wb") as fout:
            fout.write(fin.read())
    print("... done")
