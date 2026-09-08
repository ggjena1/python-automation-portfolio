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


score_1 = 95
score_2 = 43
score_3 = 67

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

#creating a list
score = [23,54,64,34,65,30,28,43,56]

#print the list 
print(score)


#element- contents of the list
#index - unique address of each element. starts with 0. increments by 1 for eath element

print(score[0])
print(score[2])
print(score[-1])

#negative indexing
fruits= ['mango','kiwi','orange','melon']
#           0        1       2       3
#          -4       -3      -2      -1


'''
IN CLASS EXERCISE

Task: Create a list named space_crafts that contains three space missions: 

"Apollo", "Voyager", and "Cassini".

Instruction 1: Use a print statement to display the entire list.

Instruction 2: Use indexing to print only the first mission ("Apollo") from your list.

Instruction 3: Use negative indexing to print only the last mission ("Cassini") from your list.

'''

space_crafts = ["Apollo", "Voyager", "Cassini"]

print(space_crafts)
print(space_crafts[0])
print(space_crafts[-1])


fruits= ['mango','kiwi','orange','melon','papaya','banana','cherries']

#list slicing 
# list_name[start:end:step_size]
# start= where the slice should start (0 by default)
# end = where the slice ends (last element index by default)
# step = how many consecutive elements to includes (1 by default)

print(fruits[0:3:1])
print(fruits[4:7:1])

'''
In class problem
nums = [1,2,3,4,5,6,7,8,9,10,11,1213,14,15,16,17,18,19,20]

take the nums list and print 
- all odd numbers
- all even numbers
- all the multiples of 3
'''

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(nums[0:20:2])
print(nums[1:20:2])
print(nums[2:20:3])


#RANGE FUNCTION
#a function for creating uniform sequences of numbers
#range(start,end,step_size)
#start: starting of the sequence (0 by default)
#end : mandatory
#step size: how many consecutivie elements will get generated (1 by default)

#creating numbers from 1 to 10 
a = list(range(1,11,1))
print(a)

#EXERCISE
#print all the odd numbers, even numbers and multiples of 3 between 1 and 100 

a= list(range(1,101,2))
print(a)
b = list(range(2,101,2))
print(b)
c=list(range(3,101,3))
print(c)

# HOMEWORK

'''
1. A local coffee shop wants to keep track of its daily sales.

Create variables to store:

* The shop name
* The number of coffees sold
* The price of one coffee
* Whether the shop is open

Then use an if condition to display a message depending on whether the shop is open or closed.

2. A cinema wants to check whether a customer can watch a movie.

Ask the user for:

* Their name
* Their age

If the customer is 18 or older, display a message saying they can watch the movie.

Otherwise, display a message saying they must choose an age-appropriate movie.

3. A small grocery store wants to keep track of products in stock.

Create a list containing 6 different grocery products.

Then:

* Print the entire list
* Print the first product
* Print the last product
* Print the first 3 products using slicing
* Print the last 3 products using slicing

4. A school wants to record the names of students who joined different school clubs.

Create a list containing 10 student names.

Ask the user for a student name.

Use an if condition to check whether the name exists in the list.

If the student is in the list, display a message saying they are registered for a club.

Otherwise, display a message saying they are not registered.

5. A fitness center wants to check whether people are allowed to use a particular exercise machine.

Create a list containing the names of 8 members.

Ask the user for their name and age.

If the person's name is in the member list and their age is 16 or older, display a message saying they can use the machine.

Otherwise, display a message explaining that they cannot use the machine.

6. A delivery company has a list of delivery package weights from one day.

Create a list containing 10 package weights.

Use range() to create a sequence of numbers from 1 to 10.

Use the numbers to access the package weights from the list.

For each package, use an if condition to check whether its weight is greater than 10 kg.

Display whether each package is within the standard weight limit or requires special handling.

7. A wildlife research team is monitoring animals in a national park.

Create a list containing 10 animal names.

Ask the user to enter an animal name they want to search for.

If the animal exists in the list, display its position in the list using its index.

Also check whether the animal is one of the first 5 animals or one of the last 5 animals in the list.

If the animal does not exist in the list, display a message saying that the animal was not recorded.

Use variables, user input, if conditions, lists, indexing, list slicing, and range() where appropriate.

'''