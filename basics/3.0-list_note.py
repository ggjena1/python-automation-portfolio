'''
ROAD MAP

1. data types and variable- recording data/information in the code 
2. if conditions - make decisions based on our data
3. list- 
'''

name = 'John'
age = 34
weight = 55.6
isMarried = False
spouseName= None

'''
Student task1: 
Create variables to store the scores of 3 students in a class
Choose the appropriat variables names and the right data type
'''

student_one = 55
student_two= 76
student_three=89

'''
something to hold a collection of data
collections in python 

lists <<<<<<<<
tuples
sets
dictionaries

orderedDicts
namedTuples
namedDicts
'''


#int list
scores = [43,56,35,23,78,34,87,56,35,24]

#printing the entire list 
print(scores)

#printing 

#element- contents of the list
#index - unique address of each element. starts with 0. increments by 1 for eath element

print(scores[0])
# print(scores[100]

#student task: print the last element of below llist
scores = [43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,24,43,56,35,23,78,34,87,56,35,3834939493940]

#negative indexing
fruits= ['mango','kiwi','orange','melon']
#           0        1       2       3
#          -4       -3      -2      -1
print(fruits[-1])
print(fruits[-4])

friends = ['olivia', 'anaya', 'petra', 'farid', 'arun']

#list slicing 
# list_name[start:end:step_size]
# start= where the slice should start (0 by default)
# end = where the slice ends (last element index by default)
# step = how many consecutive elements to includes (1 by default)
print(friends[2:5:1])

'''
In class problem
nums = [1,2,3,4,5,6,7,8,9,10,11,1213,14,15,16,17,18,19,20]

take the nums list and print 
- all odd numbers
- all even numbers
- all the multiples of 3
'''

#getting the length of a list 
print(len(friends))

#RANGE FUNCTION
#a function for creating uniform sequences of numbers
#range(start,end,step_size)
#start: starting of the sequence (0 by default)
#end : mandatory
#step size: how many consecutivie elements will get generated (1 by default)

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#EXERCISE
#print all the odd numbers, even numbers and multiples of 3 between 1 and 100 


#list index out of range error
print(fruits[20])


#string lists
friends = ['olivia', 'anaya', 'petra', 'farid', 'arun']

#non-homogenous / heterogenous lists
johns_info= ['John', 45, 56.7, False,[1,2,3]]

#create an empty list
values= []

#CHANGING A LIST ELEMENT  
print(friends)
friends[0]= 'Pawan'
print(friends)

#ADDING AN ELEMENT TO THE END OF THE LIST 
print(friends)
friends.append("Zoi")
print(friends)

#explain the difference between a function and a method 
'''
Functions vs Methods 

function are like radios
methods are like car radios 

just like functions are independent. they can operate independently 
at any point

functions that we have learned so far 
print()
len()
input()
type()

methods are like car radios. they cannot exist by themselves.
they are always attached to their parent object (car). they only 
serve  the car. they go wherever the car goes

methods 

list_name.append()
extend()
insert()
pop()
remove()
count()
'''

# inserting "Nadia" between anaya and petra
friends.insert(2,"Nadia")
print(friends)

#inserting multiple elements to a list 
#cant do append or insert on repeat
friends2= ['Sam','Dean', 'Bobby', 'Castiel']

#creating a new list by comnbing two lists 
all_friends = friends + friends2
print(all_friends)
#editing in place
friends.extend(friends2)
print(friends)

#removing elements from the list 
print(friends)
result=friends.pop()
print(result)
print(friends)

#removing an arbitray element using pop 
res=friends.pop(2)
print(res)
print(friends)


#removing by value (not safe. Need to check if the value exists first) 
friends.remove('Dean')
print(friends)
friends.append('Praveen')
friends.remove('Praveen')
print(friends)

'''
You want to go to the supermarket. Simulate the actions done there
using a list. adding an item to the basket will be like adding an 
item to the basket list and etc. 

1. create empty basket
2. add cheese to it 
3. add bread and eggs to it 
4. replace the cheese with cottage cheese
5. add grapes between cottage cheese and bread
6. remove eggs
7. remove cottage cheese
8. print the contents of the basket
'''


'''
Create a program to manage a grocery shopping list.  

1. Start by creating an empty shopping list.
2. Add the following items to the list using the appropriate method:
   - Milk
   - Bread
   - Eggs
3. Realize you forgot to add "Butter" to the end of the list and "Bananas" at the beginning.
4. Access and print the third item on the list (using indexing).
5. Replace "Bread" with "Whole Grain Bread".
6. A friend gives you their list of items: ["Apples", "Oranges", "Cheese"]. Add all of these items to your list in one step.  
7. Remove "Cheese" from the list 
8. Remove "Whole grain bread" from the list 

Print the list after every step to make sure that you changes worked. 
'''

#STRINGS ARE CHARACTER LISTS

name = 'Van Helsing'
friends= ['V','a','n',' ','H','e','l','s','i','n','g']
print(f"{name[0]}. {name[4]}.")

#LIST REPETION
first_names=['yo'] 
print(first_names*10)

'''
IN CLASS EXERCISE
Get the users first name, second name and the family name 
Print the name with initials.
'''

#membership test of lists
if 'D' in full_name:
    print("The letter D is in the person's name")
else:
    print("The letter is not there")
   


#safely removing an element using remove mmethod with membership testing

#below will fail 
#friends.remove('Jericho')

name_to_remove='Dean'
if name_to_remove in friends:
   friends.remove(name_to_remove)
else:
   print(f"{name_to_remove} is not in friends list. please check again")


#USEFUL BUILT IN FUNCTIONS
scores = [43,56,35,23,78,34,87,56,35,24]
friends = ['olivia', 'farid','anaya', 'petra', 'farid', 'arun', 'farid']

total = sum(scores)
highest = max(scores)
lowest = min(scores)
count = friends.count("farid")

# IN CLASS ASSIGNMENT 
# calculate the average score from m
#

#MULTI DIMENSIONAL LISTS
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[1][2])        # prints 6

'''
ALGORITHEMIC THINKING

1. Find the largest number in a list
2. Find the smallest number in a list
3. Calculate the sum of a list
4. Count how many even numbers are in a list
5. Count occurrences of a particular value
6. Reverse a string
Check whether a string is a palindrome
Find the second-largest number
Remove duplicates from a list
Find common elements between two lists

'''

'''
Your program will manage a music playlist and use conditional statements to handle a task.

1. Initialize an empty playlist.
2. Add the songs "Imagine", "Bohemian Rhapsody", and "Hotel California" to the playlist.
3. Realize you forgot to add "Stairway to Heaven" at the end and "Yesterday" at the beginning.
4. Check if "Imagine" is the first song of the list. 
If that is the case check if "Bohemian Rhapsody" is the second song. If so add the song "Hymn for the weekend" to the playlist. If not remove the third song from the list.  
5. Create another playlist with 3 of your favourite songs and add them to the original playlist.

-----------------------------------------------------------

Your program will calculate a customer’s monthly phone bill based on usage and plan, then demonstrate list operations on the history of bills.

1. Use input() to prompt for the customer’s name and store it in a variable called customer_name.
2. Use input() to prompt for the total minutes used (as a float) and store it in minutes_used.
3. Use input() to prompt for the plan type ("Standard" or "Premium") and store it in plan_type.
4. If minutes_used is 200 or less, set rate to 0.20; if it’s between 201 and 500 inclusive, set rate to 0.15; otherwise set rate to 0.10.
5. Calculate bill_before_discount by multiplying minutes_used by rate.
6. If plan_type is "Premium", set discount_rate to 0.05; otherwise set discount_rate to 0.0.
7. Calculate discounted_amount by subtracting bill_before_discount × discount_rate from bill_before_discount.
8. Apply a 7% tax to discounted_amount and store the result in final_bill.
9. Use an f-string to print:
   Customer {customer_name}, your final bill for {minutes_used} minutes on the {plan_type} plan is ${final_bill:.2f}.
10. Define an empty list called bill_history.
11. Append final_bill to bill_history.
12. Access and print the first bill in bill_history using positive indexing.
13. Access and print the most recent bill using negative indexing.
14. If the first bill in bill_history is greater than 100, replace it with 100.
15. If there is a bill equal to 0 in bill_history, remove it.
16. Create another list called extra_charges containing [5.0, 10.0] and extend bill_history with it.
17. Print the updated bill_history list.

'''
#-------------------------------------------------------------------------------------------------------------------------------

'''
LIST SLICING TRAINING
'''

fruits = ['orange','grapes','cherries','banana','melon']

'''
1.  Print the first two fruits
2. Print the last two fruits
3. Print from grapes to banana (grapes and banana included)
'''