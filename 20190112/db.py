#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  db.py
#  
#  Copyright 2019 Tommy Pujol <tommy@pujol.cf>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
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
	"""
Writes the given information to the database / text file.	
First try to append but if not file detected / found creates the db.
If can't create file give as output Error.
	"""

	try:
		with open("db.txt","a") as db:

			db.write(name+" "+age+" "+color+"\n")
	except:

		try:
			with open("db.txt","w+") as db:

				db.write(name+" "+age+" "+color+"\n")

		except:
	
			print("[*] Error ")
	

			
			
			
			
def read_db(f_name):
	"""
The read_db function only gives as output the resolut of the search.
If db :{
Tommy 21 Green
}
And I am looking for Tommy it will give as output the line in the db.
Else it will say Not Found.
	"""
	
	c = 0
	db = open("db.txt","r") 
		
	for lines in db: 

		data = [lines.split()[0],lines.split()[1],lines.split()[2]]
		name, age, color = data
		
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
	"""
Menu function ask's for an option wich depending on the given answer
will call a function or another. Also ask's for requirements for the functions.
	"""
	option = int(input("1- Write to DB\n2- Read the DB\n>>>"))	
	
	if not option:
		exit()

	if option == 1:	
		
		name = input("Name : ")
		age = input("Age : ")
		color = input("Favourite color : ")

		write_db(name,age,color)			

	elif option == 2:
		
		name = input("Name : ")

		read_db(name)	

	else:

		print("Not A Valid Option")
		exit()
	
if __name__ == "__main__":
	menu()

