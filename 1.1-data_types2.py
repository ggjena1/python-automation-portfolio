'''
Escape sequences 
'''

print(1,"Hello\nworld")
print(2,"Hello\tworld")

print(3,"Hello\\world")
print(4,"C:\\Users\\Gautam")

print(5,"He said \"hello\"")
print(6,'He said \'hello\'')

print(7,'He said "hello"')
print(8,"He said 'hello'")

print(9,"Hello World\rWorld")
print(10,"Hello\bWorld!")
print("\a")

msg = f'''
*** Welcome to the Store!! ***

Item name:  
Item price: 12 USD
Quantity:   1
------------------
Final Price: 12 USD

'''

# print(msg)

# print("*** Welcome to the Store!! ***\nItem name:\tRadio\nQuantity:\t12 USD")
# print("------------------")
# print("Final Price: 12 USD")



'''
You have been tasked with creating a small piece of code that will generate a customized bill for a user. Below is the 
format. Assume the user can only buy one type of item. 
Get the item name from the user 
Get the number of items from the user.  
Get the quantity 

And calculate the final price. 

*******************************
Welcome to the Kabeer's Cool Electronics

        Final Bill 
        
Item: CD Player
Quantity: 7
Item Price: 56 USD
--------------------
Net Price: 56 USD
===================

Thank you for shopping at 
Tray Electronics. Come again
Soon!
******************************
'''





item_name = input("Please the name of the item: ")
quantity = int(input("Enter number of items you bought: "))
item_price = int(input("Enter price of item: "))
net_price = quantity * item_price


msg = f'''
*******************************
Welcome to the Kabeer's Cool Electronics

        Final Bill 
        
Item: {item_name}
Quantity: {quantity}
Item Price: {item_price} USD
--------------------
Net Price: {net_price} USD
===================

Thank you for shopping at 
Tray Electronics. Come again
Soon!
******************************
'''

print(msg)


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

