'''
Create 5 variables (should include string, int, float, none and bool) about your favourite book/movie or sport.
Print two of those variables
'''

book_name = 'Alchemist'
no_of_copies_sold = 100
selling_price = 12.2
Author = None
is_available = False


print(book_name)
print(is_available)

'''
print a descriptive sentence about  the book using 3 of the above variables
Hint: use f-strings

The Alchemist is a book that costs 12.2 where 100 copies has been sold.
'''

#1. string concatenation 
# use a combination of string literals and string variables together to form the sentence 
 
print("The " + book_name + " is a book that costs " +  str(selling_price) + " where " + str(no_of_copies_sold) + " copies has been sold." )

#2. using print parameters
# include every string literal and string variable as a parameter of the print function
print("The",book_name,"is a book that costs",str(selling_price))

#3. f-strings
print(f"The {book_name} is a book that costs {selling_price} where {no_of_copies_sold} copies has been sold.")

'''
Create 5 variabes about a vehicle and print a descriptive sentence using 3 of those variables
Use f-strings
'''
car_model = "BMW"
engine_type = 1.2
series = 100
model_active = None
is_automatic = False


print(f"This {car_model} belongs to series {series} with engine type {engine_type} and GOA as {is_automatic} and active status as {model_active}")

'''

VARIABLE NAMING RULES IN PYTHON 

Rules- you have to follow. Otherwise you will get in trouble. In Python, if you don't follow the rules, your program will not even run 
Conventions- It is not strictly necessary to follow them, but not following them will cause problems down the line. 

Below are the rules related to variable naming in Python.

1. no spaces between words
travel history - not valid
travelhistory - is valid

2. cannot start with a number. numbers can be included from the second character onwards
p2p - valid
2pp - not valid

3. only allowed characters are a-z/A-Z/0-9/_

4. can't use reserved key words as variable names 
eg: for, if , with, is, class, def , while, list, tuple, dictionary , set, import , as, in, True, False, None, str, int, float, bool, None

5. do not use _ to start a variable name unless it is for a special purpose
Eg: _name should only be used in special occasions

IN CLASS EXERCISE: Mark invalid variable names and mention why they are invalid

userName  
2nd_place -> Invalid(starts with 2)
total$amount -> Invalid(Invalid character $)
final_score 
employee-name -> Invalid(Invalid character -)
_hiddenValue 
while  -> Invalid(Reserved keyward)
MAXSPEED 
pi_3.14 -> Invalid(.)
first name -> Invalid(blank space)
student_123 
True -> Invalid(Reserved keyward)
__private_var
discount% -> Invalid(Invalid character %)
myVariable

VARIABLE NAMING CONVENTIONS

the big red white car  - invalid name 
thebigredwhitecar- valid but not easy to read

We use below conventions to kill two birds with one stone 

the_big_red_white_car = Snake case (generic variable naming)
TheBigRedWhiteCar= Pascal case (naming classes)
theBigRedWhiteCar = camel case (generic variable naming)


PEP 8 Naming Conventions
Variables/functions: snake_case
Constants: ALL_CAPS
Classes: PascalCase

'''

'''
Lesson timings

if conditions - 1 lesson 
lists (array) - 2 lessons
for loops - 1 lesson 
while loos - 1 lesson 
tuples - 1 lesson 
dictionarries - 3 lesson s
functions - 5 lessons 
oop - 10 lessons 

logging - 2 lessons
file manipulation - 1 lesson 
os handling - 1 lessono 
modules and environments - 1 lesson 

regex (re)- 3 lessons

'''


# HOMEWORK

'''1. You are creating a profile for a football player.

Create 5 variables about the player. The variables should include:

* string
* int
* float
* None
* bool

Print two of the variables.

Then use an f-string to print a sentence describing the player using at least 3 of the variables.

'''
#1 
name = "Messi"
age = 35
height = 5.5
current_injury = None
is_captain = True

print(name)
print(is_captain)

print(f"My favorite player is {name} and his height is {height} and his age is {age}")

'''
2. You are building a small hotel booking system.

Create 5 variables about a hotel room. The variables should include:

* string
* int
* float
* None
* bool

Print a descriptive sentence using at least 3 variables.

Then print each variable separately.

3. You are creating a student record for a university.

Create variables for:

* student name
* age
* course
* GPA
* scholarship status

Use appropriate Python data types.

Print a sentence containing the student's name, course, and GPA using an f-string.

Then create a boolean variable that indicates whether the student is allowed to register for courses and print it.

4. You are building a food delivery application.

Create variables for:

* restaurant name
* number of items ordered
* delivery fee
* delivery person's name
* order delivered status

Use appropriate Python data types.

Print a sentence describing the order using an f-string.

Then create another variable for the total cost of the order and print a second sentence containing the restaurant name and total cost.

5. You are creating a small employee information system for a company.

Create variables for:

* employee name
* department
* years of experience
* monthly salary
* manager name

The manager name should initially be None because the employee has not been assigned a manager.

Print a sentence describing the employee using an f-string.

Then change the manager variable to a name and print another sentence showing the employee's updated manager.

Make sure all variable names follow Python's variable naming rules.

6. You are building a cinema ticket booking system.

Create variables for:

* movie title
* number of tickets
* ticket price
* customer name
* payment completed

Calculate the total ticket cost using the number of tickets and ticket price.

Print a sentence containing the movie title, customer name, number of tickets, and total cost.

Then use an if statement to print whether the booking is confirmed or not based on the payment status.

Use meaningful variable names that follow Python naming rules.

7. You are creating a simple online store order system.

Create variables for:

* product name
* quantity
* unit price
* customer name
* discount percentage
* order status

Calculate the original cost using the quantity and unit price.

Use an if statement to apply a discount only when the discount percentage is greater than 0.

Calculate the final cost after the discount.

Then use another if statement to determine whether the order should be shipped based on the order status.

Print a final descriptive sentence using an f-string that includes the customer name, product name, quantity, and final cost.

Make sure every variable name follows Python's variable naming rules.
'''


#2 
room_name = "Luxury Delux"
total_of_room = 2
room_no = 2.2211
is_room_available = False
current_guest = None

print(f"The room number is {room_no} and has {total_of_room} rooms and currently available guest {current_guest}")

#3
student_name = "Gautam"
age = 21
course = "Bachelor"
GPA = 9.8
scholarship_status = None
is_allowed_to_register = True

print(f"{student_name} is registered for the {course} and has GPA {GPA}")



#4 In_progress


#5
employee_name = "Rocks"
department = "Finance"
years_of_experience = 10
monthly_salary = 10500
manager_name = None

print(f"{employee_name} belongs to {department} and having {years_of_experience} years of experience")

#6
#6 
movie_title = "Titanic"
number_of_tickets = 2
ticket_price = 10
customer_name = "Gerrard"
payment_completed = True

total_ticket_cost = number_of_tickets * ticket_price

print(f"{movie_title} film ticket is sold to {customer_name} with {number_of_tickets} seats and for the amount {total_ticket_cost}")

#7 


a = 'hello world'
print(a)

