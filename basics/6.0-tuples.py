'''
lists are mutable tuples are not
lists start with [], tuples start with ()
creating single element tupes you have to hint python with ,
tuples support packing and unpacking, lists does not 
'''

#There is a program that makes use of 7 days of the week 
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

days.remove('Mon')

if days[0]=='Mon':
    print("Its the first day of the week. this is your timetable...")

#CREATING A LIST AND THEN CHANGING IT 
names = ['Valyrion', 'Octobar','Loraline']
names[0]='Milly'
print(names)

#TUPLES ARE IMMUTABLE (THEY CANNOT BE CHANGED AFTER CREATION)
names2 = ('Valyrion', 'Octobar','Loraline')
# names2[0]='Milly'
print(names2)

'''
INCLASS
Determine whether to use a tuple or a list in the given scenarios

1. A school stores the days of the week. The days will never be changed while the program is running. -> Tuple

2. A shopping cart stores the products a customer currently wants to buy. Products can be added or removed. -> List

3. A restaurant stores the coordinates of its location as latitude and longitude. These values should remain fixed. -> Tuple

4. A music player stores the songs in the user's current playlist. The user can add and remove songs. -> List

5. A student record stores a student's date of birth as day, month, and year. The values should not be changed. -> Tuple

'''


'''
Mutability/ Immutability in Python 

Objects that can be changed after creation are mutable 
- lists
- dictionaries
- sets
- bytearray

Immutable objects

- int
- float
- str
- tuple
- bool
- bytes
- none 

'''

# x = 45 (430493040303020)

# x = 35 (3293929392939)

# names  = ["milly","bobby","brown"] (4939293929929)

# DEMONSTRATION- MUTABLES OBJECTS ALLOW MODIFICATIONS

numbers = [10, 20, 30]
before = id(numbers)
print("Before:", numbers)
print("ID before:", before)

numbers.append(40)

after = id(numbers)

print("\nAfter:", numbers)
print("ID after:", after)

print("\nSame object:", before == after)


# DEMONSTRATION - IMMUTABLE OBJECTS RESIST MODIFICATIONS

number =10
before = id(numbers)
print("Before:", number)
print("ID before:", before)

number= 20

after = id(number)

print("\nAfter:", number)
print("ID after:", after)

print("\nSame object:", before == after)

#ILLEGALLY MODIFY A TUPLE
names2 = ('Varyion', 'Octobar','Loraline')
names2=list(names2)
names2[0]='Milly'
names2=tuple(names2)
print('-'*50)
print(names2)

#NESTED TUPLES
nested = ( (1,2), (3,4) )
print(nested[1][0]) #will print number 3

#CREATING A SINGLE ELEMENT TUPLE
little_name_list = ['Nuada']
print(type(little_name_list))

little_name_tuple = ('Nuada',)
print(type(little_name_tuple))

#WHY BRACKETS ARE IGNORED
#in equations round brackets are ignored
a = 1*3 
print(a)
b= (1*3)+2
print(b)

# tuple packing
name = 'Jonathan'
print(type(name))

information = 'Jonathan', 'Kelsington',56,True
print(type(information))

#trying to do the same thing with a list will convert it in to a tuple
info2=[]
info2='seth','gordon'
print(info2)
print(type(info2))

#TUPLE UNPACKING
first_name,family_name,age,married= information
print(first_name)
print(family_name)
print(age)
print(married)

#TUPLE CONCATENATION
t1 = (1,2)
t2 = (3,4)
t3 = t1 + t2  
print(t3)

#TUPLE SLICING
'''
LIST SLICING SYNTAX
list_name[start:end+1:step size]
'''
nums = [10, 20, 30, 40, 50]
print(nums[1:3:1])
print(nums[1:4:2])

nums = (10, 20, 30, 40, 50)
print(nums[1:3:1])
print(nums[1:4:2])

#MEMBERSHIP TESTING
if 10 in nums: 
    print("10 is in there")

#TUPLE REPETION
first_names=('hi',) 
print(first_names*10)


#GENERIC FUNCTIONS
print(len(nums))
print(min(nums))
print(max(nums))
print(sum(nums))

new_nums = (1,2,2,3)
new_nums.count(2)   # 2
new_nums.index(3)   # 3


#Homework
'''

Problem 1: Weekly Café Sales Tracker

A small café records its daily sales for a week and wants a simple program to analyze the data while preserving the fixed structure of the week.

Create a tuple named week_days containing the seven days of the week in order.

Create a list named daily_sales that stores the sales amount for each day using numbers.

Use a while loop to repeatedly ask the user to enter a sales threshold until they enter a positive number.

Use a for loop and if conditions to count how many days had sales greater than or equal to the threshold.

Use tuple membership testing to check whether 'Sun' is part of week_days and print a message if it is.

Print the total number of days that met the sales threshold.

----------------------

Problem 2: Smart Water Tank Monitoring System

A residential building uses a smart system to monitor daily water usage and tank safety.

Create a tuple named tank_limits that stores (minimum_safe_level, maximum_safe_level).

Create a list named daily_usage that stores water usage readings recorded every hour.

Use a while loop to repeatedly ask the user to enter a new hourly usage value until they enter a negative number to stop.

Inside the loop, use if conditions to:

Reject unrealistically high values above the maximum_safe_level.

Accept valid values and append them to daily_usage.

Use a for loop to calculate the total water usage for the day.

Use an if condition to check whether total usage exceeds the maximum_safe_level and print a warning.

Use membership testing to check whether a specific usage value exists in daily_usage.

----------------------------

Problem 3: Online Store Order Validation

An online store processes customer orders and applies rules based on fixed delivery zones.

Create a tuple named delivery_zones containing valid zone codes such as ('A', 'B', 'C').

Create an empty list named orders to store order amounts.

Use a while loop to ask the user to enter order amounts until they enter 0 to stop.

Inside the loop, use if conditions to:

Ignore negative values.

Append valid order amounts to the orders list.

Use a for loop to count how many orders are above a fixed minimum purchase amount.

Use tuple membership testing to check whether a user-entered delivery zone exists in delivery_zones.

Use list slicing to display the last three orders placed.

---------------------

Problem 4: School Bus Attendance Checker

A school tracks which students boarded the bus each morning while keeping route information fixed.

Create a tuple named route_info containing (route_number, max_capacity).

Create an empty list named boarded_students.

Use a while loop to ask the user to enter student names until they type 'done'.

Inside the loop, use if conditions to:

Stop input if capacity is reached.

Reject empty names.

Add valid names to boarded_students.

Use a for loop to print all boarded student names.

Use an if condition to compare the number of boarded students with max_capacity and print whether the bus is full or not.

Use membership testing to check whether a specific student name boarded the bus.

--------


Problem 5: Office Weekly Task Completion Tracker

An office team tracks task completion over a fixed work week.

Create a tuple named work_days containing the five weekdays.

Create a list named completed_tasks that stores the number of tasks completed each day.

Use a while loop to prompt the user to enter task counts until exactly five valid values are collected.

Inside the loop, use if conditions to reject negative numbers.

Use a for loop to calculate the average number of tasks completed.

Use tuple indexing to identify and print the last working day.

Use an if condition and list membership testing to check whether any day had zero completed tasks and print a message.
'''