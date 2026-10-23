
#--------------- LISTS ------------

empty_list = []
numbers =[10,20,30]

#printing 10 
print(numbers[0])
print(numbers[-3])

#index starts by 0 and increments by 1 
#negative indexing starts at -1 (last element) and increase in reverse

#string list
friends =  ['olivia', 'anaya', 'petra', 'farid', 'arun']

#list slicing 
# list_name[start:end:step_size]

print("slice of friends:",friends[2:5:1])

#getting the length of the list 
print(len(friends))

#RANGE FUNCTION
#a function for creating uniform sequences of numbers
#range(start,end,step_size)
#creating a list of numbers from 1 to 10 

a = list(range(1,11))
print(a)

#homogeneous lists
friends = ['olivia', 'anaya', 'petra', 'farid', 'arun']
numbers =[10,20,30]

#non-homogenous / heterogenous lists
johns_info= ['John', 45, 56.7, False,[1,2,3]]

#changing a list element- change olivia to pawan
friends[0]= 'Pawan'

# adding an element to the end- add zoi to the end of friends list
friends.append("Zoi")

#adding nadia between anaya and petra
friends.insert(2,"Nadia")

#adding multiple elements at the same time - new lisst 
friends2= ['Sam','Dean', 'Bobby', 'Castiel']
all_friends = friends + friends2

#adding multiple elements at the same time - in line 
friends.extend(friends2)

#original friends list
#friends = ['olivia', 'anaya', 'petra', 'farid', 'arun']

#after extending the friends list look like below 
#friends = ['olivia', 'anaya', 'petra', 'farid', 'arun','Sam','Dean', 'Bobby', 'Castiel']

#removing the last element from the list
result=friends.pop()

#removing the element at index 2 
res=friends.pop(2)

#remove by value 
friends.remove('Dean')

#strings are character list 
# append, insert, extend, pop, pop(2) work with strings

#membership testing
if 'Dean' in friends: 
    print("Dean is a friend")
else:
    print("Dean is not a friend")

#list repetion 
greeting = 'hi'
print(greeting*10)

scores = [84,39,49,67,90]
#additional useful functions
total = sum(scores)
highest = max(scores)
lowest = min(scores)
count = friends.count("farid")

# ------------------ FOR LOOPS ---------------

scores = [84,39,49,67,90]
# going over each value in scores, adding 10 to it and printing them 

#metho1 : going over elements themselves
for score in scores:
    print(score+10)

#method2: goign over elements using their indexes
for i in range(len(scores)):
    print(scores[i]+10)

# print the score id and the score # enumerate meaning keeping track of all the counts for example stair up the staircase and count the no of steps covered
print ("-------")
for id,score in enumerate(scores): # [(0,84),(1,39)]
    print(id, score)

# going over each character in a string
word = "Python"

for letter in word:
    print(letter)

#combining for loops with if loops 

prices = [500, 1500, 800, 2500, 1200]

for price in prices:
    if price > 1000:
        print(price)

# using break with for loop 
products = ["Mouse", "Keyboard", "Laptop", "Monitor"]

for product in products:
    if product == "Laptop":
        print("Product found")
        break

#using continue with for loop

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        continue

    print(number)

# nested for loops 

for table in range(1, 3): #[1,2]
    #table =1
    for seat in range(1, 4): #[1,2,3]
        print("Table", table, "Seat", seat)

# output
# Table 1 Seat 1
# Table 1 Seat 2 
# Table 1 Seat 3
# 2 1 
# 2 2
# 2 3

#---------------- WHILE LOOPS ---------------

'''
METHOD 1: WHILE LOOP RUNS UNTIL THE CONDITION IS TRUE
while CONDITION: 
    action 
    update the condition 

METHOD 2: WHILE LOOP IS RUN WITH TRUE AND BROKEN WHEN NECESSARY

while True:
    action 
    if TIME_TO_BREAK:
        break

'''

#METHOD 1 : printing from 1 to 10 using a while loops

i = 1
while i<11:
    print(i)
    i+=1 # i = i + 1

# METHOD 2 : printing from 1 to 10 using while loop

i = 1
while True:
    print(i)
    i+=1
    if i>10:
        break

# continue key word will skip the current iteration and move on to the next one 
# print from 1 to 10, but skipping odd numbers


i = 1
while True:
    if i%2==1:
        continue 

    print(i)
    i+=1

    if i>10:
        break

==================================================
        MY WHILE TRUE LOOP CHEAT SHEET
==================================================

[THE STRUCTURE]
while True:
    
    1. SAFETY BREAK (Always put this first!)
       if i >= len(your_list):
           break

    2. TARGET BREAK (Stop early if a goal or limit is hit)
       if condition == True:
           break

    3. THE SKIP RULE (Skip an item, but ADVANCE THE INDEX FIRST)
       if item == "Bad_Item":
           i += 1      <-- DO NOT FORGET THIS!
           continue    <-- Jumps straight back to the top

    4. NORMAL PROCESSING (Do the work, then advance)
       total += item
       i += 1          <-- Moves to the next item
