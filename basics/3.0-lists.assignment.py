# List - Basic Operation 
space_crafts = ['Apollo', 'Voyager', 'Cassini']
print(space_crafts)
print(space_crafts[0])
print(space_crafts[-1])

fruits = ['mango', 'kiwi', 'melon', 'papaya', 'banana', 'cherries']
# list slicing
# list_name[start:end:step_size]
# start = where the slice should start (0 by default)
# end = where the slice ends (last element index by default)
# step = how many consecutive elements to includes (1 by default)

print(fruits[0:3:1])
print(fruits[4:6:1])

'''
nums = [1,2,3,4,5,6,7,8,9,10,11,1213,14,15,16,17,18,19,20]
take the nums list and print 
- all odd numbers
- all even numbers
- all the multiples of 3
'''
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(nums)
print(nums[0:20:2])
print(nums[1:20:2])
print(nums[2:20:3])

# RANGE FUNCTION
# a function for creating uniform sequences of numbers
# range(start,end,step_size)
# start : starting of the sequence (0 by default)
# end = mandatory
# step size : how many consecutive elements will get generated (1 by default)

# creating numbers from 1 to 10
a = list(range(1,11,1))
print(a)

#EXERCISE
#print all the odd numbers, even numbers and multiples of 3 between 1 and 100

b = list(range(1,101,2)) 
print(b)
c = list(range(2,101,2))
print(c)
d = list(range(3,100,3))
print(d)


# HOME WORK
'''
1. A local coffee shop wants to keep track of its daily sales.
Create variables to store:
* The shop name
* The number of coffees sold
* The price of one coffee
* Whether the shop is open

Then use an if condition to display a message depending on whether the shop is open or closed.
'''
shop_name = 'KoffieKupje'
no_of_coffee_sold = int(input('Enter total_no_of_coffee_sold:' ))
price_of_each_coffee = 3.7
is_open = True

if is_open == True :
    print('KoffieKupje is Open')
else:
    print('KoffieKupje is Closed')

'''
2. A cinema wants to check whether a customer can watch a movie.
Ask the user for:
* Their name
* Their age
If the customer is 18 or older, display a message saying they can watch the movie.
Otherwise, display a message saying they must choose an age-appropriate movie.
'''
name = input('Enter your name: ')
age = int(input('Enter your age: '))

if age >=18:
    print('You can watch the movie')
else:
    print('Sorry !!! you must choose an age-appropriate movie  ')

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
groceries = ['salt', 'museli', 'eggs', 'milk', 'sugar', 'oil']
print(groceries)
print(groceries[0])
print(groceries[-1])
print(groceries[0:3])
print(groceries[3::])

'''
4. A school wants to record the names of students who joined different school clubs.
Create a list containing 10 student names.
Ask the user for a student name.
Use an if condition to check whether the name exists in the list.
If the student is in the list, display a message saying they are registered for a club.
Otherwise, display a message saying they are not registered.
'''
names = ['Gautam', 'Ram', 'Rahul', 'Rishi', 'Rishi', 'Rocky', 'Ranjan', 'Raghu', 'Rayan', 'Roul']

a = input('Enter the student name please : ')

if a in names:
    print('Already Registered')
else:
    print('Not Registered')


'''
5. A fitness center wants to check whether people are allowed to use a particular exercise machine.

Create a list containing the names of 8 members.

Ask the user for their name and age.

If the person's name is in the member list and their age is 16 or older, display a message saying they can use the machine.

Otherwise, display a message explaining that they cannot use the machine.
'''

member = ['Rohith', 'Roxy', 'Rocky', 'Raj', 'Rahul', 'Ram', 'Ronald', 'Rooijaker']

name = input('Enter your name :')
age = int(input('Enter your age: '))

if name in member:
    if age >= 16:
        print('You can use the machine')
    else:
        print('You can not use the machine')
else: 
    print('You are not a member. Please register yourself')


'''
6. A delivery company has a list of delivery package weights from one day.
Create a list containing 10 package weights.
Use range() to create a sequence of numbers from 1 to 10.
Use the numbers to access the package weights from the list.
For each package, use an if condition to check whether its weight is greater than 10 kg.
Display whether each package is within the standard weight limit or requires special handling.
'''

package_wights = [26.3, 11,12, 13, 14, 32, 33,23, 29.0,12.4]

for i in range(len(package_wights)):
    print(i, package_wights[i])    
    if package_wights[i] > 10:
        print('Additional charges required')


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
animal = ['elephant', 'giraffe', 'tiger', 'lion', 'monkey', 'wolf']

name= input('Enter the animal name you want search: ').lower()
if name in animal:
    print(animal.index(name))

    if animal in animal[:5:]:
        print('Within first 5 elements')
    else:
        print('within last 5 elements')
else: 
    print('Animal is not recorded')


    




# 15-09-2026 # HOME WORK # Assignment
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