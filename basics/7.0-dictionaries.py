'''
ROAD MAP 

1. data type and variables - how to record data/ information in to programs
2. if conditions - making decisions based on data
3. lists - record data at scale
4. for loops - automate manipulating collections of data at scale
5. whlile - automate things, repeat things until a certain condition was satisfied 
6. tuples - helpes us with data integrity 
7. dictionaries - 
'''

#THE PROBLEM WITH LISTS
scores = [45,32,67,89,32]
names = ['Roy','Sharon','Threse','Niran','Ravi']

# How to 
#Roy got 45
for i in range(len(names)):
    print(f'{names[i]} got {scores[i]}')

'''
dictionary have key, value pairs

name gautam 
city holland

key leads to the value 
map that leads to the hidden pirate treasure 

the VALUE(ble) thing is hidden in the room locked by the KEY
'''

student_score_info = {
    'Roy':45,
    'Sharon':32,
    'Threse': 67, 
    'Niran':89, 
    'Ravi':32
    }

'''
Taleem was able to sell 3 apples, 9 grapes and 4 papapya at his fruit store. 
Create a dictionary that shows the fruits and the amout he sold 
'''
fruits_info={'apples':3,'grapes':9,'papaya':4}

'''
In class exercise

1. A school stores each student's name along with their age. What should be the key and what should be the value?
Key:student_name, Value: age_no 
2. A library stores each book's ISBN number along with its title. What should be the key and what should be the value?
key:ISBN number , value: title 
3. A shop stores each product's name along with its price. What should be the key and what should be the value?
Key: product_name, value: price 
4. A school stores each student's ID number along with their email address. What should be the key and what should be the value?
key: student_id, value: email id
5. A phone contacts app stores each person's name along with their phone number. What should be the key and what should be the value?
key: phone number , value: name
'''
#PRINTING THE ENTIRE DICTIONARY 
print(student_score_info)

#ACCESSING DICTIONARY DATA
print(student_score_info['Roy'])

print(student_score_info)
#MODIFY AN ELEMENT
student_score_info['Roy']=65
print(student_score_info)

#ADDING A NEW KEY VALUE PAIR 
student_score_info['Shiromi']=99

print(student_score_info)

'''

BRACKET USAGE IN PYTHON 
[] - square brackets

    - list creation 
    - list indexing
    - list slicing
    - tuple indexing
    - tuple slicing
    - dictionary indexing 
    
()- round brackets 

    - tuple creation 
    - functions and methods
    - classes

    
{} - chain brackets (curly brackets)
    - F strings 
    - dictionary creation 
    - set creation
'''

# --------- MCQ TEST ON BRACKET USAGE IN PYTHON -----------------
'''
1. Which type of brackets is used to create a list in Python?
A. ()
B. {}
C. [] : <-
D. <>



2. Which brackets are used for list indexing and slicing?
A. () 
B. []  : <-
C. {}
D. <>



3. Which bracket type is used to access a value in a dictionary using a key?
A. ()
B. [] : <-
C. {}
D. <>



4. Which brackets are used to create a tuple?
A. []
B. {}
C. () : <-
D. <>



5. Which bracket type is used when calling a function or a method?
A. []
B. {}
C. () : <-
D. <>


6. Which brackets are used when defining a class in Python?
A. []
B. () : <-
C. {}
D. <>


7. Which bracket type is used to create a dictionary?
A. ()
B. []
C. {} : <-
D. <>


8. Which brackets are required when using an f-string?
A. ()
B. []
C. {} : <-
D. <>


9. In the statement `fruits['cherries'] = 12000`, which brackets are used around the key?
A. ()
B. [] : <-
C. {}
D. <>


10. Which of the following correctly matches the bracket type with its usage?
A. () - dictionary creation X
B. [] - function calls X
C. {} - list slicing X
D. () - tuple creation : <-

'''

# Gautam scored 90%

#DICTIONARY METHODS

#GETTING A LIST OF KEYS
print(student_score_info.keys())

#GETTING A LIST OF VALUES
print(student_score_info.values())

#GETTING A LIST OF KEY,VALUE PAIRS
print(student_score_info.items())


# HOMEWORK
'''
1. A small cafe wants to keep track of the number of drinks sold today. Ask the user to enter the number of coffees sold and the number of teas sold. Store the two numbers in a dictionary using the drink names as keys. Print the dictionary and then print the number of coffees sold.

2. A sports club keeps the names of players and their scores in a dictionary. Create a dictionary containing 5 players and their scores. Use a for loop to print each player's name and score. If a player's score is 50 or higher, also print that the player passed. Otherwise, print that the player failed.

3. A supermarket wants to keep track of its stock. Create a dictionary containing 5 products and the number of items currently available. Use a for loop to display every product and its stock quantity. If the stock of a product is below 10, display a message saying that the product needs to be restocked.

4. A bus company wants to record the number of passengers travelling on several buses. Create a dictionary containing the bus number as the key and the number of passengers as the value. Use the keys() method to display all bus numbers. Use the values() method to calculate how many passengers are travelling in total. Then use items() to display each bus number and its passenger count.

5. A hospital reception system stores each patient's name and their assigned room number in a dictionary. Ask the user to enter the name of a new patient and their room number, then add the patient to the dictionary. Ask the user for a patient's name and display their room number if the name exists in the dictionary. If the name does not exist, display a suitable message.

6. A warehouse records the quantity of different products in a dictionary. Create a dictionary containing at least 6 products and their quantities. Use a while loop to repeatedly ask the user for a product name. If the product exists, display its current quantity. If the user enters "stop", end the program. Keep track of how many valid products the user searched for and display the total when the loop finishes.

7. A delivery company wants to analyse the delivery performance of its drivers. Store each driver's name and number of successful deliveries in a dictionary. Use a for loop to examine every driver. Store the names of drivers who completed at least 20 deliveries in a list. Store the names of drivers who completed fewer than 20 deliveries in another list. Use a tuple to store the minimum and maximum delivery targets. Then use if conditions to determine which drivers met the minimum target and display the results. Finally, display the two lists and the target tuple.

'''



'''
1. A small cafe wants to keep track of the number of drinks sold today. 
Ask the user to enter the number of coffees sold and the number of teas sold. 
Store the two numbers in a dictionary using the drink names as keys. 
Print the dictionary and then print the number of coffees sold.
'''

#DICTIONARY METHODS

#GETTING A LIST OF KEYS
print(student_score_info.keys())

#GETTING A LIST OF VALUES
print(student_score_info.values())

#GETTING A LIST OF KEY,VALUE PAIRS
print(student_score_info.items())

# no_of_coffee_sold = int(input('Enter the no of coffee sold: '))
# no_of_tea_sold = int(input('Enter the no of tea sold: '))

# drinks_sold={'coffee': no_of_coffee_sold, 'tea':no_of_tea_sold}
# print(drinks_sold)



'''
get the users age 
if the user is less than 18 print 'child'
otherwise print 'adult'
'''
# age = int (input('Enter the age: '))
# if age < 18:
#     print('child')
# else:
#     print('adult')

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


# basket=[]
# print(basket)
# basket.append('cheese')
# print(basket)
# basket.append('bread')
# basket.append('eggs')
# print('basket',basket)
# # replace an item
# basket[0]='cottage cheese'
# print(basket)

# # add items in between lists
# basket[1]='grapes'
# print(basket)

# # remove an item
# basket.pop()
# # remove cotton cheese
# # basket.remove('cottage cheese')
# basket.remove('cottage cheese')
# print(basket)

'''
You are creating a student score management system. Get the number of student from the teacher. 
This number cannot be negative or over 10
Invallid numbers should be rejected with a proper error message and question should be asked again 

Then collect the names and score of students 
Calculate the average score
Print names of the student who scored above average
'''

while True:
    no_of_student=int(input('Enter the no of students: '))
    if 1 < no_of_student <10:
        break
    else:
        print('Invalid number , enter number between 0 and 9')

names=[]
scores=[]

for i in range(no_of_student):
    name=input('Enter name: ')
    names.append(name)
    score= int(input('Ente scores: '))
    scores.append(score)

print(names)
print(scores)
    
average=sum(scores)/no_of_student
print(average)

for i in range(len(scores)): #[0,1,2,3]
    if scores[i] > average:
        print(names[i])




# Homework 
# while Lookup
# for lopp
# range function         
    
# while loop , for loop, range function

'''
1. You are creating a movie review system. Get the number of movies from the user.

The number of movies must be between 1 and 10.

Invalid numbers should be rejected with a proper error message and the question should be asked again.

Then collect the title of each movie and its rating out of 10.

Calculate the average rating.

Print the titles of movies that received a rating above the average.
'''





'''
2. You are creating a warehouse inventory system. Get the number of products being tracked.

The number of products must be between 1 and 10.

Invalid numbers should be rejected with a proper error message and the question should be asked again.

Then collect the name of each product and its current stock quantity.

Calculate the total number of items in stock.

Print the names of products that have fewer than 5 items in stock.

3. You are creating a bus passenger tracking system. Get the number of buses.

The number of buses must be between 1 and 10.

Invalid numbers should be rejected with a proper error message and the question should be asked again.

Then collect the bus number and the number of passengers currently on each bus.

Calculate the average number of passengers.

Print the bus numbers that have more passengers than the average.

Also print the total number of passengers across all buses.

4. You are creating a small restaurant sales system. Get the number of menu items sold today.

The number of items must be between 1 and 10.

Invalid numbers should be rejected with a proper error message and the question should be asked again.

Then collect the name of each menu item and the amount of money earned from selling that item.

Calculate the total revenue and average revenue per item.

Print the names of items that generated more revenue than the average.

Also print the name of the item that generated the highest revenue.

5. You are creating a water usage monitoring system for an apartment building. Get the number of apartments being monitored.

The number of apartments must be between 1 and 10.

Invalid numbers should be rejected with a proper error message and the question should be asked again.

Then collect the apartment number and its water usage in litres.

Calculate the average water usage.

Print the apartment numbers that used more water than the average.

Also calculate how many apartments used more than 500 litres and print that number.

'''

