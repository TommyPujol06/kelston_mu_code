#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  db.py
#  
#  Copyright 2019 Tommy Pujol <tommy@pujol.cf>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


from sys import exit 

def write_db(name, age, color):
	"""Writes the given information to the database / text file.	
	If can't create file give as output Error.
	"""

	try:
		with open("db.txt","a") as db:

			db.write(name+" "+age+" "+color+"\n")			

	except OSError:

		print("\n[*] Error\n")

			
def read_db(f_name):
	"""The read_db function only gives as output the resolut of the search.
	If db :{
	Tommy 21 Green
	}
	And I am looking for Tommy it will give as output the line in the db.
	Else it will say Not Found.

	C = Counter. The counter is used to 'know' if there are more than one person 
	with the same name. If not that it will say Not Found for every line with no 
	person found. 
	"""
	
	c = 0
	
	with open("db.txt","r") as db:
		
		for lines in db: 

			name, age, color = lines.split()
		
			if name == f_name:
			
				c += 1
					
				print("\n[+] Found :\n\n* Name : " + name,"\n* Age : " + age + "\n* Favourite color : " + color + "\n")
						
		
			if not name == f_name:
			
				if c <= 1:
					pass
				
				else:
					print("\n[*] Not Found ")
					exit()
			
def menu():
	"""Menu function ask's for an option wich depending on the given answer
	will call a function or another. Also ask's for requirements for the functions.
	"""
	
	try:

		option = int(input("1- Write to DB\n2- Read the DB\n>>>"))	

		
	except ValueError:
		
		print("\nMust Be Only A Number")
		exit()
	
	if option == 1:	
		
		name = input("\nName : ")
		age = input("Age : ")
		color = input("Favourite color : ")

		write_db(name,age,color)			

	elif option == 2:
		
		f_name = input("\nName : ")
		read_db(f_name)
		
	else:

		print("\nNot A Valid Option")
		exit()
	
	
if __name__ == "__main__":
	exit(menu())

