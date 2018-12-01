def letters_in_common(w1, w2):
    return set(w1)&set(w2)

if __name__ == '__main__':
    print(letters_in_common("abc", "bcd"))