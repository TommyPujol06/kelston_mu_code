import fnmatch

def words_from_file(filepath):
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                yield word

def match_words(words, pattern):
    return fnmatch.filter(words, pattern)
