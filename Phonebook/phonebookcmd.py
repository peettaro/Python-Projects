
# CREATING A COMMAND LINE APP TO INTERACT WITH SQLITE DATABASE
# IMPORTING THE REQUIRED MODULES
import sqlite3
import time

#CREATING THE ACTUAL DATABASE

conn = sqlite3.connect("names.db")
cursor = conn.cursor()

# cursor.execute("""CREATE TABLE names(first_name TEXT, last_name TEXT, phone_number INTEGER)""")

def start():
	options = ["Add person", "Edit Person", "Delete person", "Search person", "View persons"]
	number = 1
	for i in options:
		print("{} : {}".format(number, i))
		number += 1
# --------------------------------------------------------------------------------------------------------
try:
	start()
except Exception:
	print("Something went wrong!")

try:
	user_sel = int(input("Select one of the options: "))
except ValueError:
	print("Enter a number between 1-5")

# CREATING THE CONTACTS FUNCTIONS

# CREATING THE ADD PERSON FUNCTION
def add():
	first_name = input("Enter first_name: ")
	last_name = input("Enter last name: ")
	phone_no = int(input("Enter phone number: "))

	cursor.execute("INSERT INTO names VALUES(?,?,?)", (first_name, last_name, phone_no))
	print("Changes made successfully!")

# CREATING THE EDIT PERSON CONTACT
def edit():
	edit_options = ["first_name", "last_name", "phone_number"]
	counter = 1
	for i in edit_options:
		print("{} : {}".format(counter, i))
		counter += 1

	edit_select = int(input("Select value to change: "))

	if edit_select == 1:
		prev_name = input("Enter the previous name: ")
		new_name = input("Enter the new name: ")
		cursor.execute("UPDATE names SET first_name = ? WHERE first_name = ?", (new_name, prev_name))
		print("Changes made successfully!")

	elif edit_select == 2:
		prev_name = input("Enter the previous name: ")
		new_name = input("Enter the new name: ")
		cursor.execute("UPDATE names SET last_name = ? WHERE last_name = ?", (new_name, prev_name))
		print("Changes made successfully!")

	else:
		prev_number = input("Enter previous phone number: ")
		new_number = input("Enter new phone number: ")
		cursor.execute("UPDATE names SET phone_number = ? WHERE phone_number = ?", (new_number, prev_number))
		print("Changes made successfully!")

# CREATING THE DELETE PERSON FUNCTION
def delete():
	get_first = input("Enter the first name: ")
	get_last = input("Enter the last name: ")
	cursor.execute("DELETE FROM names WHERE first_name = ? AND last_name = ?", (get_first, get_last))
	print("Changes made successfully!")

# CREATING THE SEARCH PERSONS FUNCTION
def search():
	get_name = input("Enter person's name: ")
	cursor.execute("SELECT * FROM names WHERE first_name = ? OR last_name = ?", (get_name, get_name))
	print(cursor.fetchall())

# CREATING THE VIEW PERSONS FUNCTION
def view():
	cursor.execute("SELECT * FROM names")
	# print(cursor.fetchall())
# GETTING BETTER SQLITE OUTPUT
	for row in cursor:
		print("{} : {}".format("first name", row[0]))
		print("{} : {}".format("last name", row[1]))
		print("{} : {}".format("phone number", row[2]))
		print()

# SELECTING THE OPTIONS
try:
	if user_sel == 1:
		add()

	elif user_sel == 2:
		edit()

	elif user_sel == 3:
		delete()

	elif user_sel == 4:
		search()

	else:
		view()

except ValueError:
	print("You need to enter a number between 1-5")

conn.commit()
conn.close()