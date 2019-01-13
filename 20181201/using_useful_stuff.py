"""Import another module, showing that the __main__ code is not run
"""
import useful_stuff

print(useful_stuff.letters_in_common("dog", "cat"))
print(useful_stuff.letters_in_common("cow", "cot"))