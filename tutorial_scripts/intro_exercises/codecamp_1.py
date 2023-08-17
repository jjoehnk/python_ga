# getting started with some classics

print('hello world')


print('   /|')
print('  / |')
print(' /  |')
print('/___|')


# VARIABLES

character_name = "John" #string --> selection of varying characters
character_age = 35 #integer or float --> whole numbers versus decimal
is_a_dude = False #boolean --> true or false value

print("There once was a man named " + character_name + ",")
print("he was " + str(character_age) + " years old.")
print("He really liked the name " + character_name + ",")
print("but didn't like being " + str(character_age) + ".")



# Working with Strings


phrase = "waaaaaaaaaassssssssssssssssuuuuuuuuuuuuuuupppppppppppp"
print("wasssssssuuuuuuuppppppp y'all\"hi")
print(phrase)
print(phrase + " " + character_name)
print(phrase.upper()) #.upper and .lower for some text manipulation
print(phrase.islower()) #checks if string is upper/lower
print(phrase.upper().isupper()) #make upper and then check if true
print(len(phrase)) #count length of string
print(phrase[0]) #pull specified character from number value (indexed starting with value 0)
print(phrase.index("ssss")) #PASSING A PARAMETER --> shows were a single or segment of a string STARTS
print(phrase.replace("waaa", "wooo")) #replace that waaa with a woo


# Working with Numbers

from math import *

my_num = 5
print(-2.0495+7)
print(str(my_num))
print(pow(3, 2))
print(min(4, 6))
print(round(3.7))
print(floor(3.7))
print(ceil(3.7))
print(int(sqrt(36)))


# Getting Input from Users

#name = input("Enter your name:")
#age = input("Enter your age:")
#print("Hello " + name + "! You are " + age + ".")



# Lists


lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Abby", "Lewis", "George", "Abby", "Sophie", "Jackson"]
# index ->   0        1        2
friends[0] = "Johanna"
print(friends[0])
#friends.extend(lucky_numbers)
friends.append("Euan")
friends.insert(1, "George")
friends.remove("Jackson")
#friends.clear()
friends.pop()
print(friends.index("Sophie"))
print(friends.count("George"))
friends.sort()
print(friends)
lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)



# Tuples

coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates[0])


# Functions

def sayhi(name, age):
   print("Hello " + name + ", you are " + age + ".") 

sayhi("Zumba", "2")
sayhi("Coco", "15")


# Return Statement

def cube(num):
   return num*num*num


result = cube(4)
print(result)


# If Statements

is_guy = False
is_short_king = True
if is_guy and is_short_king: 
   print("You are a bro and short king")
elif is_guy and not(is_short_king):
    print("why you not a short king bro")
elif not(is_guy) and is_short_king:
    print("hi short queen")
else: 
   print("You not a bro not a short king what is the point of living")


# If Statements and Comparisons

def max_num(num1, num2, num3):
   if num1 >= num2 and num1 >= num3:
      return num1
   elif num2 >= num1 and num2 >= num3:
      return num2
   else:
      return num3
   
print(max_num(3,4,5))


# Dictionaries 
# Key | Value
monthConversions = {
   "Jan": "January",
   "Feb": "February",
   "Mar": "March",
   "Apr": "April",
   "May": "May",
   "Jun": "June",
   "Jul": "July",
   "Aug": "August",
   "Sep": "September",
   "Oct": "October",
   "Nov": "November",
   "Dec": "December",
}

print(monthConversions.get("Luv", "Whadda mean"))


# While Loop

i = 1
while i <= 10:
   print(i)
   i += 1

print("finni")


# For Loop

friends = ["gay", "trans", "lesbian"]
for name in friends:
   print(name)


for index in range(3, 5):
   print(index)


# Exponent Function

def raise_to_power(base_num, pow_num):
   result = 1
   for index in range(pow_num):
      result = result * base_num
   return result

print(raise_to_power(3, 4))   


# 2D Lists and Nested Functions

number_grid = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9],
   [0]
]

for row in number_grid:
   for col in row:
      print(col)



# Comments

# This prints out a string
# woooooo 
'''
asdf 
'''
print("Comments are fun") 


# Try Except

'''try:
   number = int(input("Enter a number"))
   print(number)
#except ValueError:
   print("wooah try again bro")   
#except ZeroDivisionError:
   print("dividing by zero? come on")
'''

# Reading Files

# r == reads
# w == write
# a == append
# r+ == read and write

employee_file = open("cc_ex_reading_files.txt", "r")
for employee in employee_file.readlines():
   print(employee)
employee_file.close()

# Writing Files

employee_file = open("cc_ex_reading_files1.txt", "a")
employee_file.write("\nKelly - Customer Services")
employee_file.close()


# Modules and Pip

import random

print(random.randint(1, 6))


# Classes and Objects

from cc_student import Student

student1 = Student("Zumba", "Being Cute", 4.0)
student2 = Student("Coco", "Being sassy", 2.0)

print(student1.name)


# Class Function

from cc_student import Student

student1 = Student("Zumba", "Being Cute", 4.0)
student2 = Student("Coco", "Being sassy", 2.0)

print(student1.on_honor_roll())


# Inheritance 

from cc_chef import Chef
from cc_chinesechef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()


# Python Interpreter