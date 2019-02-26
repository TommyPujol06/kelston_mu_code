"""MIT License
Copyright (c) 2019 Tommy Pujol
This is the testfile for the hangman_words_file. It does not give any output but 
if it does not give any error looks right !!!
"""

import os, sys, time, platform
from hangman_words import *

def clear():
	
	os_name = platform.system()
	
	if os_name == "Linux":
		
		os.system("clear")
	
	elif os_name == "Windows":
		
		os.system("cls") 
	
	else:
		
		os.system("echo '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'")
		test()

def run():
	
	os_name = platform.system()
	
	if os_name == "Linux":
		
		os.system("python3 hangman.py")
	
	elif os_name == "Windows":
		
		os.system("py -3 hangman.py") 
	
	else:
		
		os.system("echo 'Not Supported For The TESTFILE'")
		clear()
		test()
	
		
def test():
	
	print("""
1 => read_possible_words
2 => pick_a_word
	* Need Word List
3 => letter_is_good
	* Random Choosen Word 
	* Given Letter
4 => update_word_so_far
	* Random Choosen Word 
	* Word So Far Of The Game 
	* Guessed Letters
5 => update_failed_letters
	* Failed Letters
	* The Given Letter
6 => ALL
	""")
	
	try:
		global test
		test = int(input("@=> "))
	
	except ValueError:
		
		clear()
		test_menu()
	
	if test == 1:
		
		read_possible_words()
		
	elif test == 2:
		
		inp = input("Word List : \n").split(",")
		
		pick_a_word(inp)
		
	elif test == 3:
	
		word = input("Input the 'real' word : ")
		given_letter = input("Input the given letter : ")
		
		letter_is_good(word, given_letter)
	
	elif test == 4:
		
		word = input("Input the 'real' word : ")
		word_so_far = input("Input the word so far e.g. H_LL_ : ").split() 
		new_letter = input("Input the given letter : ")
	
		update_word_so_far(word, word_so_far, new_letter)
	
	elif test == 5:
		
		f_letters = input("Input the failed letters separed by , : ").split(",")
		new_letter = input("Input the new given letter : ")
		
		update_failed_letters(f_letters, new_letter)

	elif test == 6:
		
		run()
		
	else:
		
		print("Invalid Option")
		time.sleep(2)
		clear()
		test()
		
if __name__ == "__main__":
    
	def update_word_so_far(real_word, word_so_far, guessed_letter):
		"""Using the word so far and the chosen letter,
		return a new version of the word so far with the
		letter in the correct places.
		"""

		dashed_word = word_so_far = ""
		
		# every_item_in_the_guessed_letters_list
		
		for with_letter_or_dash in range(len(real_word)):

			if real_word[with_letter_or_dash] == guessed_letter:

				dashed_word += guessed_letter

			else:

				dashed_word += "_"
		

		
		print(list(dashed_word))
		
		return list(dashed_word)
		
	update_word_so_far("hello",[],"h")
	
    #sys.exit(test())
