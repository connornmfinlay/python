# Python Problem Set 2
#
# Student Name      - Connor Finlay
# Student Number    - EC1950697
# Date              - 18/11/2020
#
'''
Save this python script in your code folder as problem_set_2.py
then run it, and edit the file, once complete upload to the moodle.
'''
# Q1 Can you add some comments to this python program so that it is more understandable,
# can you also change the variable name to mean something sensible,
# the program is meant to be for a user to enter their name:
# your code below this line:

username = input('Enter your name?:')  #this is asking the user to enter there name
print('Hello', username ,'!')    #printing the username
print('Exiting program')        #informing the user that the program is finished


# Q2 Make the following program more readable and add an in-line comment at the end of
# each line, and fix any syntax errors.
number_entered = int(input('Enter a number and i will square it:')) # asking user to enter value
number_squared = number_entered * number_entered
print('The number squared is,', number_squared,'!')


# Q3 Fix the syntax in this program so that it runs, add a comment to explain what it is doing?
# the program should sum two numbers and have 3 variables

first_number = 1
second_number = 2
number_total = print(first_number + second_number) #the program is adding variables "number1" and "number2", adding them together saving the answer in the variable "number4" and then displaying the variable "number4"


# Q4 Create a program with sensible comments and variable names that
# takes a number and divides it by 2.54. The title of the program should be
# "Inches to cm Converter"
# your code here:
print("Welcome to the cm to Inch converter!")
measurement = int(input("Please enter your measurement:"))
m_inches = measurement / 2.54
print("This is your measurement in inches:", m_inches)

