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
	
	try:
		with open("db.txt","a") as db:
		
			db.write(name+" "+age+" "+color+"\n")
	except:
		
		try:
			with open("db.txt","w+") as db:
		
				db.write(name+" "+age+" "+color+"\n")
		
		except:
			
			print("[*] Error")
	
def read_db(f_name):
	
	db = open("db.txt","r")
		
	for lines in db: 

		name = [lines.split()]
		name.append(name[0])
		
		age = lines.split()[1]
		age = "".join(age)
		
		color = lines.split()[2]
		color = "".join(color)
				
		for x in name:
			continue
			
		if x[0] == f_name:
						
			print("[+] Found :\n* Name : " + f_name,"\n* Age : " + age + "\n* Favourite color : " + color)

def menu():
		
	option = int(input("1- Write to DB\n2- Read the DB\n>>>"))	
	
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

