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
'''




'''
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

'''



'''
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

'''

'''
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

'''




'''

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
''' 




'''

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




# HOMEWORK
'''
1. A hotel wants to determine the room type a guest should receive based on their age.

Ask the guest for their age.

Classify them as:

0 to 12: Child Guest
13 to 17: Teen Guest
18 to 55: Adult Guest
56 and above: Senior Guest

If the age is negative, print "Invalid age".

Print the guest's classification.

2. A fitness center wants to decide whether a person can join a particular training program.

Ask the user for their age and fitness level.

If the person is 18 or older, check their fitness level.

If the fitness level is "beginner", print "Beginner Program".
If it is "intermediate", print "Intermediate Program".
If it is "advanced", print "Advanced Program".

If the person is under 18, print "Youth Program".

Use nested if statements.

3. A cinema wants to calculate how many tickets a customer needs to buy.

Ask the user how many people are attending.

Use a while loop to repeatedly ask for the age of each person.

Store all the ages in a list.

After collecting the ages, use a for loop to count:

Children: under 13
Teenagers: 13 to 17
Adults: 18 to 59
Seniors: 60 and above

Print the number of people in each category.

4. A delivery company wants to calculate the delivery fee for several packages.

Create a function called calculate_delivery_fee() that receives the weight of a package.

Use these rules:

Weight below 1 kg: $5
1 kg to below 5 kg: $10
5 kg to below 10 kg: $15
10 kg or more: $25

Ask the user how many packages they want to send.

Use a for loop to get the weight of each package and call the function.

Store the package weights in a list and print the total delivery fee.

5. A school is organizing students into sports teams.

Ask the user how many students are participating.

Use a while loop to collect each student's name and age.

Store each student's information as a tuple containing their name and age.

Store all the tuples inside a list.

Use a for loop to examine every student.

Students aged 18 or above should be classified as "Senior Team".
Students aged 13 to 17 should be classified as "Junior Team".
Students below 13 should be classified as "Youth Team".

Print each student's name and team.

6. A supermarket wants to evaluate a customer's shopping basket.

Ask the user to enter the prices of items one at a time.

Keep asking for prices until the user enters 0.

Store the prices in a list.

Create a function called calculate_total() that receives the list and returns the total price.

Then classify the customer's purchase:

Below $50: Small Purchase
$50 to below $100: Medium Purchase
$100 to below $250: Large Purchase
$250 or above: Premium Purchase

If the customer spent $100 or more, ask whether they have a membership.

If they answer "yes", apply a 10% discount.

Print the original total, discount if applicable, and final total.

7. A company is building a training evaluation system for its employees.

Create a function called evaluate_employee() that receives an employee's age, training score, and number of completed projects.

The function should classify the employee using these rules:

If the employee is under 18, return "Not eligible".

For employees aged 18 or above:

If the score is 80 or above:
If completed projects are 5 or more, return "Senior Candidate"
Otherwise, return "High Performer"

If the score is between 50 and 79:
If completed projects are 3 or more, return "Developing Employee"
Otherwise, return "Needs More Experience"

If the score is below 50:
return "Training Required"

In the main program, use a while loop to collect information for multiple employees.

Store each employee's name, age, score, and completed projects as a tuple inside a list.

Use a for loop to evaluate every employee by calling the function.

Print each employee's name and evaluation result.

'''



# HOMEWORK 
'''
------------------ NESTED IF LOOPS HOMEWORK ------------------------
Write a program that determines if a student is eligible for a school field trip based on their grade and parental consent. 
Use nested if statements with only one inner if loop.

The student must be in Grade 4, 5, or 6 to be eligible.
If the student is not in these grades, they are not eligible for the trip.
Parental Consent:

If the student is in an eligible grade, ask if they have parental consent.
If the answer is "yes", they can join the trip.
Otherwise, they cannot join the trip.

----------------------------------------------------------------
 Write a program that determines if a person is eligible for a library membership based on their age and residency status. 
 Use nested if statements and the or keyword.

Rules:
Age Requirements:

The person must be 12 years or older to be eligible.
If the person is younger than 12, they are not eligible for membership.
Residency Requirement:

If the person meets the age requirement, check if they are a resident of the town.
A person is considered a resident if they answer "yes" or "y".
If they are a resident, they are eligible for membership.
Otherwise, they are not eligible.

If the person is less than 12 years old, check if they are in kindergarten. 
If they are in kindergarten, print that they are eligible for art competion. 
Otherwise print that they can read books at the library. 

Hint: Start by collection below information 
age - int
is the user a resident- string
is the user in the kindergarten

Then apply the logic using nested if loops

Problem: Library problem
------------------------------------

A library categorizes books based on their genre and popularity. They use the following classification system:

If a book is of the "Fiction" genre:

If its popularity rating (out of 10) is 7 or above, classify it as "Popular Fiction."
Otherwise, classify it as "Regular Fiction."
If a book is of the "Non-Fiction" genre:

If its popularity rating (out of 10) is 7 or above, classify it as "Popular Non-Fiction."
Otherwise, classify it as "2
Regular NoI rescheduled to Thursday. Please feel free to reschedule again if the new time does not work.n-Fiction."


Problem: Restaurant Dish Classification
--------------------------------------------------------
A restaurant categorizes its dishes based on the type of cuisine and customer rating.
They use the following classification system:

    1. If a dish belongs to "Italian" cuisine:

        - If its rating (out of 10) is 8 or above, classify it as "Top Italian Dish".

        - Otherwise, classify it as "Regular Italian Dish".

    2. If a dish belongs to "Asian" cuisine:

        - If its rating (out of 10) is 8 or above, classify it as "Top Asian Dish".

        - Otherwise, classify it as "Regular Asian Dish".

Write a Python program that:

Asks the user to input the cuisine type and rating of a dish.

Prints the classification of the dish according to the rules above.

Problem: Movie Rating System

A streaming platform wants to classify movies based on their genre, viewer rating, and number of reviews.
The classification system works as follows:

1. If the movie is an "Action" movie:

   * If the rating is 8 or higher and there are more than 1000 reviews, classify it as "Blockbuster Action".
   * If the rating is 8 or higher but 1000 or fewer reviews, classify it as "Underrated Action".
   * Otherwise, classify it as "Regular Action".

2. If the movie is a "Drama" movie:

   * If the rating is 8 or higher and there are more than 500 reviews, classify it as "Critically Acclaimed Drama".
   * If the rating is below 8 but there are more than 1000 reviews, classify it as "Popular Drama".
   * Otherwise, classify it as "Regular Drama".

3. If the movie is a "Comedy" movie:

   * If the rating is 7 or higher, classify it as "Funny Hit".
   * Otherwise, classify it as "Average Comedy".

Write a Python program that:

* Asks the user to input:

  * The movie genre
  * The rating (out of 10)
  * The number of reviews
* Prints the classification according to the rules above.



##################### DIFFICULT PORBLLEMS - NO CLEAR INSTRUCTIONS ########################


1. A small grocery shop gives a warning message if a customer tries to enter a bill amount that is less than zero. Otherwise, it prints the bill amount. Design a program that behaves this way.

2. A cinema only allows entry to people aged 16 and above. If the person is younger, a message is shown saying they cannot enter. Create a program that decides what message to show based on age.

3. A food delivery app labels orders based on total cost. Orders below 500 are marked as "Low Value", and all others are marked as "High Value". Write a program that assigns this label.

4. A school assigns performance levels to students based on their score. Very low scores are labeled "Needs Improvement", mid-range scores are labeled "Satisfactory", and high scores are labeled "Excellent". Build a program that determines the correct label for a given score.

5. A bus service charges passengers differently based on age. Children travel for free, teenagers pay a reduced fare, and adults pay full fare. Write a program that determines which category a passenger belongs to.

6. An online store checks whether an order qualifies for a discount. If the order value is high enough, it then checks if the customer is a registered member to decide if an extra benefit is applied. Create a program that determines the final outcome.

7. A game awards players based on two factors: their level and their score. Players below a certain level are treated differently from advanced players. Among advanced players, only those with high scores receive special rewards, while others receive standard rewards. Write a program that determines what reward a player receives.
'''






 ##### LIST PROGRAMS ###########
 # 
 # # HOME WORK
'''
1. A local coffee shop wants to keep track of its daily sales.
Create variables to store:
* The shop name
* The number of coffees sold
* The price of one coffee
* Whether the shop is open

Then use an if condition to display a message depending on whether the shop is open or closed.
'''
# shop_name = 'KoffieKupje'
# no_of_coffee_sold = int(input('Enter total_no_of_coffee_sold:' ))
# price_of_each_coffee = 3.7
# is_open = True

# if is_open == True :
#     print('KoffieKupje is Open')
# else:
#     print('KoffieKupje is Closed')

'''
2. A cinema wants to check whether a customer can watch a movie.
Ask the user for:
* Their name
* Their age
If the customer is 18 or older, display a message saying they can watch the movie.
Otherwise, display a message saying they must choose an age-appropriate movie.
'''
# name = input('Enter your name: ')
# age = int(input('Enter your age: '))

# if age >=18:
#     print('You can watch the movie')
# else:
#     print('Sorry !!! you must choose an age-appropriate movie  ')

'''
3. A small grocery store wants to keep track of products in stock.
Create a list containing 6 different grocery products.
Then:
* Print the entire list
* Print the first product
* Print the last product
* Print the first 3 products using slicing
* Print the last 3 products using slicing
'''

# groceries = ['salt', 'museli', 'eggs', 'milk', 'sugar', 'oil']
# print(groceries)
# print(groceries[0])
# print(groceries[-1])
# print(groceries[0:3])
# print(groceries[3::])

'''
4. A school wants to record the names of students who joined different school clubs.
Create a list containing 10 student names.
Ask the user for a student name.
Use an if condition to check whether the name exists in the list.
If the student is in the list, display a message saying they are registered for a club.
Otherwise, display a message saying they are not registered.
'''
# names = ['Gautam', 'Ram', 'Rahul', 'Rishi', 'Rishi', 'Rocky', 'Ranjan', 'Raghu', 'Rayan', 'Roul']

# a = input('Enter the student name please : ')

# if a in names:
#     print('Already Registered')
# else:
#     print('Not Registered')


'''
5. A fitness center wants to check whether people are allowed to use a particular exercise machine.

Create a list containing the names of 8 members.

Ask the user for their name and age.

If the person's name is in the member list and their age is 16 or older, display a message saying they can use the machine.

Otherwise, display a message explaining that they cannot use the machine.
'''

# member = ['Rohith', 'Roxy', 'Rocky', 'Raj', 'Rahul', 'Ram', 'Ronald', 'Rooijaker']

# name = input('Enter your name :')
# age = int(input('Enter your age: '))

# if name in member:
#     if age >= 16:
#         print('You can use the machine')
#     else:
#         print('You can not use the machine')
# else: 
#     print('You are not a member. Please register yourself')


'''
6. A delivery company has a list of delivery package weights from one day.
Create a list containing 10 package weights.
Use range() to create a sequence of numbers from 1 to 10.
Use the numbers to access the package weights from the list.
For each package, use an if condition to check whether its weight is greater than 10 kg.
Display whether each package is within the standard weight limit or requires special handling.
'''

# package_wights = [26.3, 11,12, 13, 14, 32, 33,23, 29.0,12.4]

# for i in range(len(package_wights)):
#     print(i, package_wights[i])    
#     if package_wights[i] > 10:
#         print('Additional charges required')


'''
7. A wildlife research team is monitoring animals in a national park.
Create a list containing 10 animal names.
Ask the user to enter an animal name they want to search for.
If the animal exists in the list, display its position in the list using its index.
Also check whether the animal is one of the first 5 animals or one of the last 5 animals in the list.
If the animal does not exist in the list, display a message saying that the animal was not recorded.
Use variables, user input, if conditions, lists, indexing, list slicing, and range() where appropriate.

sequence.index(element, start, end)

'''
# animal = ['elephant', 'giraffe', 'tiger', 'lion', 'monkey', 'wolf']

# name= input('Enter the animal name you want search: ').lower()
# if name in animal:
#     print(animal.index(name))

#     if animal in animal[:5:]:
#         print('Within first 5 elements')
#     else:
#         print('within last 5 elements')
# else: 
#     print('Animal is not recorded')


    




# 15-09-2026 # HOME WORK
'''
1. A city bus company records the number of passengers boarding at different stops.
Create a list containing the number of passengers who boarded at 8 different stops.

Use indexing to:
Print the number of passengers at the first stop.
Print the number of passengers at the last stop.
Print the passengers at the first 3 stops.
Ask the user for a stop number.

Use an if condition to check whether the stop number is valid. If it is valid, display the number of passengers at that stop. Otherwise, display an error message.
''' 
psg_list = [11,8,23,22,17,15,4,5]
print(psg_list[0])
print(psg_list[-1])
print(psg_list[0:3])

'''
2. A mobile phone shop keeps a list of prices for 8 different phones.
Create a list containing the phone prices.

Ask the user to enter their budget.

Use an if condition to determine whether their budget is enough to buy the first phone in the list.

Also create a new list containing the last 3 phone prices and display it.
'''

mobile_prices = [999, 1999,2999,4999,9999,24999, 49999, 99999]
budget=int(input('Enter your budget:'))
if (budget >= 999):
    print(f'You can buy the phone with price {mobile_prices[0]}')
else:
    print(f'Please increase your minimum budget to {mobile_prices[0]} ')

mobile_prices_1 = mobile_prices[5:8]
print(mobile_prices_1)

'''
3. A hotel keeps a list of the number of guests staying in each of 10 rooms.
Create a list containing the guest counts.

Use range() to create a sequence that can be used to access every room in the list.

For each room, use an if condition to determine whether the room is empty or occupied.

Display the room number and whether it is empty or occupied.

'''

guest_count = [1,2,1,3,2,1,0,2,1,0]
for i in range(len(guest_count)):
    if guest_count[i] == 0:
        print(i, 'Empty' , guest_count[i])
    else:
        print(i, 'Occupied', guest_count[i])

'''
4. A supermarket has a list of 10 product names.
Create the list and then ask the user to enter the name of a product.

Use an if condition to check whether the product exists in the list.

If it exists:

Find its index.
Check whether it is located in the first half or second half of the list.
Display an appropriate message.
If it does not exist, display a message saying that the product is unavailable.

'''
product_list = ['Milk', 'Curd', 'Salt', 'Sugar', 'Bread', 'Butter', 'Paprika', 'Tomaten', 'Citroen', 'Eggs']
name = input('Enter the name of the product: ')

if name in product_list:
    print(product_list.index(name))
    half = len(product_list) // 2

    if product_list.index(name) < half:
        print('It is in the first half of the list.')
    else:
        print("It is in the second half of the list.")
else:
    print('The product is unavailable')

'''
5. A university records the marks of 10 students in a programming test.
Create a list containing the marks.

Use range() to access each mark.

For every student, use an if condition to determine whether the student has passed or failed. A mark of 50 or above is considered a pass.

Keep track of how many students passed and how many failed using variables.

Display the final number of passed and failed students.
'''
marks = [97,76,89,43,93,99,88,29,44,22]
for i in range(len(marks)):
    if marks[i] >= 50:
        print(i, marks[i], 'Passed')
    else:
        print(i, marks[i], 'Failed')

'''
6. A restaurant has a list of 10 menu items and a separate list containing their prices.
Ask the user to enter the number of a menu item.

Use an if condition to check whether the number is valid.

If it is valid:

Use the number to access the corresponding menu item.
Display the item and its price.
Ask the user whether they want to order it.
If they answer "yes", add the item to an order list.
If the menu number is invalid, display an appropriate message.
'''

items=['Burger', 'Pizza', 'Pasta', 'Salad', 'Cocacola', 'Pepsi', 'Lemonade', 'Coffee', 'Thee', 'Juice']
prices=[4.5, 10.5, 8.5, 4, 2.5, 2.5, 2.5, 2.75, 1.75, 2.95 ]

user_input = int(input('Enter the number of a menu item (1 to 10): '))
if user_input in range(10):
    print(f'The price of {items[user_input]} is ${prices[user_input]}')
else:
    print('Please enter a valid menu number.')

'''
7. A small electronics store wants to analyse its daily sales.
Create a list containing the sales amounts for 10 different days.

Use range() to access each value in the list.

For every day:

Use an if condition to determine whether sales were below 50000, between 50000 and 100000, or above 100000.
Display the day number and the appropriate sales category.
Then ask the user to enter a day number.

Check whether the day number is valid. If it is valid, display the sales amount for that day and determine its sales category using an if condition.
'''

sales_amount = [100000, 20000,30000,400000,50000,60000,70000,180000,190000,100000]
day_no = int(input('Enter a day number: '))

if day_no in range(len(sales_amount)):
    print(f'Day No is {day_no}')

    for i in range(len(sales_amount)):
        if i == day_no:
                     if sales_amount[i] < 50000:
                            print(f'Day No : {day_no} and sales below 50000')
                     elif 50000 <= sales_amount[i] <= 100000:
                            print(f'Day No is : {day_no} and sales between 50000 and 100000')
                     else:
                           print(f'Day No is : {day_no} sales above 100000')
else:
      print(f'Not a valid day {day_no}') 


#### LOOP PROGRAMS ####

#Homework:
'''
1. A weather station records the temperatures measured at 6 different times during the day.
Create a list containing 6 temperature values.
Use a for loop to go through the list and add 2 degrees to every temperature. Print each original temperature together with the adjusted temperature.
Use an if condition to check whether the adjusted temperature is above 30 degrees. Display "Hot" or "Normal" for each reading.
'''

temp = [23.2, 23.5, 29, 28.4, 22, 21.2]
for i in range(len(temp)):
    # print(i)
    # print(temp[i])
    # print(temp[i]+2)
    print(i, temp[i], temp[i]+2)

    if temp[i]+2 >= 30:
        print('Hot')
    else:
        print('Normal')

2nd solution: final solution for review
temp = [23.2, 23.5, 29, 28.4, 22, 21.2]
for i in range(len(temp)):
    print(temp[i], temp[i]+2)
    if(temp[i]+2) >=30:
        print('Hot')
    else:
        print('Normal')


'''
2. A supermarket records the number of customers entering the store during 8 different hours.
Create a list containing the customer counts.
Use a for loop to display each customer count.

Use an if condition to determine whether the number of customers is greater than 50.

Display whether each hour was "Busy" or "Not busy".

Also calculate and display the total number of customers using sum().
'''
customer_count = [35, 84, 32, 90, 21, 86, 34, 90]
sum = 0
for i in range(len(customer_count)):
    print(customer_count[i])
    if customer_count[i] >=50:
        print('Busy')
    else:
        print('Not busy')
    sum = sum+customer_count[i]
print(f'Total number of customers : {sum}')

2nd solution: final solution for review
customer_count = [35, 84, 32, 90, 21, 86, 34, 90]
for i in range(len(customer_count)):
    print(customer_count[i])
    if customer_count[i] >=50:
        print('Busy')
    else:
        print('Not busy')
    total = sum(customer_count)
print(f'Total number of customers : {total}')

'''
3. A fitness app stores the number of steps taken by a user over 7 days.
Create a list containing the step counts.
Ask the user to enter a number of extra steps they want to add to each day.
Use a for loop to go through the list and display the number of steps for each day after adding the extra steps.

Use an if condition to check whether the updated number of steps is at least 10000.

Display "Goal reached" or "Goal not reached" for each day.

Also display the highest and lowest updated step counts.
'''
updated_steps = []
step_counts = [12000, 6000, 9000, 13000, 15000,20000]
extra_steps = int(input('Enter no of additional extra steps to add: '))

for i in range(len(step_counts)):
    updated = step_counts[i]+extra_steps
    updated_steps.append(updated)
    print(i, updated)


    if step_counts[i]+extra_steps >= 10000:
        print('Goals reached')
    else:
        print('Goals not reached')

    highest = max(updated_steps)
    lowest = min(updated_steps) 

print(f'highest updated steps count {highest}')
print(f'lowest updated steps count {lowest}')

'''
4. A restaurant has a waiting list containing the names of customers waiting for tables.
Create a list containing 8 customer names.
Ask the user to enter their name.

Use an if condition to check whether the customer is already on the waiting list.

If the customer is not on the list, add the customer to the end of the list using append().

If the customer is already on the list, display their position using index().

Finally, display the updated waiting list.
'''
cust_names = ['Gautam', 'Ronald', 'Jerry', 'Max', 'Bill', 'Sundar', 'Mark', 'Jeff']
name = input('Enter your name in Pascal case : ')

if name in cust_names:
    print(f'Your position is in {cust_names.index(name)}')
else:
    cust_names.append(name)
    print(f'Your position is in {cust_names.index(name)} ')

'''
5. A delivery company records the weights of 8 packages.
Create a list containing the package weights.

Use range() and indexing to access each package weight.

For every package, use an if condition to determine whether the package is under 5 kg, between 5 kg and 10 kg, or above 10 kg.

Display the package number, weight, and appropriate category.

Also calculate and display the total weight of all packages.
'''

pkg_weights = [2.4, 5.4, 5.9, 3.2, 9.6, 3, 4, 7.4, 8.2, 12]
for i in range(len(pkg_weights)):
    print(i, pkg_weights[i])

    if pkg_weights[i] <=5:
        print(f'The package {i} is weight {pkg_weights[i]}kg and category is under 5 kg ')
    elif 5<= pkg_weights[i] <= 10:
        print(f'The package {i} is weight {pkg_weights[i]}kg and category is between 5 kg and 10 kg')
    else:
        print(f'The package {i} is weight {pkg_weights[i]}kg and category is above 10 kg')

total_weight = sum(pkg_weights)
print(f'Total weight of all the packages are {total_weight}')


'''
6. A school stores the marks of students from 3 different classes. Each class has 4 students.
Create a two-dimensional list containing the marks for all 3 classes.

Use nested for loops to access every mark.

Add 5 marks to each student's score and display the updated score.

Use an if condition to display "Pass" if the updated mark is 50 or above and "Fail" otherwise.

Finally, display the highest mark from all the scores.
'''
marks = [
    [30,40,50,60],
    [34,44,54,64],
    [29,39,49,59]
    ]
updated_mark = []
for i in marks:
    for j in i:
        new_mark = j+5
        print(j, new_mark)
        if new_mark >= 50:
            print('Pass')
        else:
            print('Fail')
        updated_mark.append(new_mark)

highest_mark = max(updated_mark)
print(f'Highest Mark is {highest_mark}')

'''
7. A small online store keeps a list of product names and a separate list containing their prices.
Create a list containing 8 product names and another list containing their prices.

Ask the user to enter a product name.

Use an if condition to check whether the product exists.

If the product exists, find its index and use that index to find the corresponding price.

Ask the user how many units they want to buy.

Calculate the total cost.

If the total cost is 5000 or more, apply a 10 percent discount. Otherwise, keep the original price.

Display the product name, price per unit, quantity, and final cost.

If the product does not exist, display a message saying that the product is unavailable.
'''
products = ['Laptop', 'Phone', 'Tablet', 'Headphones','Keyboard', 'Mouse', 'Monitor', 'Printer']
prices = [45000, 25000, 18000, 3000, 1500, 1000, 12000, 8000]

product_name = input('Enter product name: ')

if product_name in products:
    index = products.index(product_name)
    price_per_unit = prices[index]
    print(f'Price per unit for {product_name} is: {price_per_unit}')

    quantity = int(input('How many units do you want to buy? '))
    total_cost = price_per_unit * quantity

    if total_cost >=5000:
        final_cost = total_cost * 0.90 # 10% discount
    else:
        final_cost = total_cost

    print('Product : ', product_name)
    print('Price per unit: ', price_per_unit)
    print('Quantity: ', quantity)
    print('Final cost is : ', final_cost)

    
else:
    # product does not exists
    print('Product Unavailable')
