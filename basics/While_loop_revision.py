'''
==================================================================
                 THE ULTIMATE WHILE LOOP CHEAT SHEET
==================================================================

[ THE CORE SKELETON ]

i = 0  # 1. ALWAYS start with your index counter at 0

while True:  # 2. Start the infinite loop
    
    # -----------------------------------------------------------
    # STEP 1: SAFETY BREAK (Put this at the VERY TOP)
    # -----------------------------------------------------------
    if i >= len(your_list_name):
        break  # Stops the loop when you run out of items (Prevents IndexError)


    # -----------------------------------------------------------
    # STEP 2: GRAB THE CURRENT ITEM
    # -----------------------------------------------------------
    item = your_list_name[i]


    # -----------------------------------------------------------
    # STEP 3: THE STOP RULE (Optional Early Exit)
    # -----------------------------------------------------------
    if item == "End_Condition" or status == "Goal_Reached":
        break  # Shuts down the loop immediately


    # -----------------------------------------------------------
    # STEP 4: THE SKIP RULE (The "Continue Trap")
    # -----------------------------------------------------------
    if item == "Bad_Item_Or_Bug":
        i += 1      # <--- CRUCIAL! Move to the next index FIRST...
        continue    # <--- ...then skip and jump straight back to the top!


    # -----------------------------------------------------------
    # STEP 5: NORMAL PROCESSING (If it passes all rules above)
    # -----------------------------------------------------------
    total_running_score += item
    print(f"Processed: {item}")


    # -----------------------------------------------------------
    # STEP 6: ADVANCE THE INDEX (At the VERY BOTTOM)
    # -----------------------------------------------------------
    i += 1  # Moves to the next item for the next loop turn

==================================================================
                      THE 3 GOLDEN LAWS
==================================================================
1. IF THE TERMINAL FREEZES: You forgot 'i += 1' somewhere. 
   Press [Control + C] on your keyboard to force it to stop.

2. BEFORE YOU 'CONTINUE': You MUST write 'i += 1' right above the 
   word 'continue', otherwise you will get stuck in an infinite loop.

3. ORDER MATTERS: Put your rules at the top to intercept items 
   BEFORE you print them or add them to your totals.
==================================================================
''' 





'''
The Goal: Loop through numbers from 1 to 10 using while True:.
• Rule 1: If the number is 5, use continue to skip printing it.
• Rule 2: If the number hits 9, use break to stop the loop completely.
• Normal Processing: Otherwise, just print the number.

'''
# num =1
# while num < 10:

#     if num == 5:
#         num+=1
#         continue

#     if num == 9:
#         break

#     print(num)
#     num = num +1 


##############

# num =1

# while True:
#     if num >= 10:
#         break

#         if num ==5:
#             num +=1
#             continue
#         if num==9:
#             break

#         print(num)
#         num=num+1
################
 
'''
🏋️ Loop Training: Challenge 2 (The VIP Lounge)

Let's test your skills with a new scenario using a while True: loop.
The Scenario: You are managing a queue for a VIP club. The club only allows a maximum of 3 people in tonight. Loop through this list of guests:
guests = ["Alice", "Bob", "Bug_System", "Charlie", "David", "Emma"]
The Rules:
1. Safety Break: Stop if you run out of guests in the list.
2. The Skip Rule: If a guest's name is "Bug_System", it's an error. Skip them using continue.
3. The Stop Rule: Once your entered_count reaches 3, the club is full. Stop the loop using break.
4. Normal Processing: Print "[Name] has entered the club" and increase your entered_count by 1.
Give this VIP Lounge challenge a try using a while True: loop in VS Code. Paste your code below when you are ready!

'''

# guests = ["Alice", "Bob", "Bug_System", "Charlie", "David", "Emma"]
# entered_count = 0
# i = 0

# while True:
#     if i >= len(guests):
#         break
    
#     guest = guests[i]

#     if entered_count == 3:
#             break

#     if guest == "Bug_System":
#             i+=1
#             continue

#     print(f'{guest} has entered the club.')

#     entered_count += 1
#     i+=1
    
# print("--- Loop Finished ---")

'''
Practice Problem 1: The Video Game Energy Drink
You are coding a video game character's inventory system. 
The character has an energy level starting at 50. They are chugging a list of items.

items = ["Apple", "Energy_Drink", "Poison_Mushroom", "Energy_Drink", "Shield", "Energy_Drink"]
energy = 50
i = 0

Use code with caution.
The Rules:
1. Safety Break: Stop if i reaches the end of the items list.
2. The Skip Rule: If the item is "Poison_Mushroom", skip it entirely using continue (don't increase i without changing something first!).
3. The Target Break: If energy reaches 100 or higher, the character is fully charged. Stop the loop immediately using break.
4. Normal Processing: If they process an "Energy_Drink", add 25 to their energy level and print the current energy.
For any other item, just print "Ignoring [item name]". Remember to advance i += 1.
'''
# items = ["Apple", "Energy_Drink", "Poison_Mushroom", "Energy_Drink", "Shield", "Energy_Drink"]
# energy = 50
# i = 0

# while True:

#     if i>=len(items):
#         break

#     item = items[i]

#     if energy >=100:
#         break

#     if item == "Poison_Mushroom":
#         i+=1
#         continue

#     if item == "Energy_Drink":
#         energy+=25
#         print(f'Current Energy is :{energy}')
#     else:
#         print(f'Ignoring {item}')
#     i+=1 


'''
🏦 Practice Problem 2: The ATM Withdrawal System

An ATM allows a user to withdraw money until they run out of cash or hit their daily transaction limit.
python
requested_withdrawals = [200, 500, 50, 1000, 300, 100]
account_balance = 1200
transactions_count = 0
i = 0
Use code with caution.
The Rules:
1. Safety Break: Stop if you run out of requested withdrawals.
2. The Stop Break: If account_balance hits 0, stop the loop immediately.
3. The Skip Rule: If a withdrawal amount is greater than the current account_balance, print "Insufficient Funds" and skip it using continue.
4. Normal Processing: Deduct the amount from account_balance, increase transactions_count by 1, and advance i.
'''
# requested_withdrawals = [200, 500, 50, 1000, 300, 100]
# account_balance = 1200
# transactions_count = 0
# i = 0

# while True:
#     if i>=len(requested_withdrawals):
#         break

#     withdraw = requested_withdrawals[i]

#     if account_balance == 0:
#         break

#     if withdraw > account_balance:
#         print('Insufficient Funds')
#         i+=1
#         continue
#     else:
#         account_balance = account_balance - withdraw
#         print(f'Balance is: {account_balance}')
#         transactions_count+=1

#     i+=1

'''
📦 Practice Problem 3: The Delivery Truck Loader

You are loading packages onto a delivery truck. The truck has a strict weight limit.
package_weights = [15, 40, 5, 120, 30, 10]
current_truck_weight = 0
max_limit = 200
i = 0
Use code with caution.
The Rules:
1. Safety Break: Stop if there are no more packages left to check.
2. The "Too Heavy" Skip Rule: If adding the current package's weight would push current_truck_weight over the max_limit, 
print "Package too heavy, skipping" and skip it using continue.
3. Normal Processing: Add the package weight to current_truck_weight, print the new total truck weight, and advance i.
'''
# package_weights = [15, 40, 5, 120, 30, 10]
# current_truck_weight = 0
# max_limit = 200

# i = 0
# while True:

#     if i>=len(package_weights):
#         break

#     package = package_weights[i]


#     if current_truck_weight + package > max_limit:
#         print('Package too heavy')
#         i+=1
#         continue

#     else:
#         current_truck_weight += package
#         print(f'The new total truck weight is: {current_truck_weight}')
#     i+=1


'''
Get the age from the user. 
If the age is less than 1 or higher than 100, reject it with a suitable message and ask the question again. 
The program should keep asking the question until the user entres a valid age or 'exit' is entered to the answer. 

'''
while True:
    user_input = input('Enter age: ')

    if user_input== 'exit':
        print("Ending the program")
        break

    #if user_input a number of a word
    if user_input.isdigit():
        age = int(user_input)
        if age < 1 or age >100:
            print('Invalid age')
        else:
            print(f"user age accepted: {age}")
            break


'''
1\. A library asks visitors to enter their membership ID. 
The ID must contain only digits and must be between 1000 and 9999.
If the ID is invalid, display a suitable error message and ask again.
Allow the visitor to enter "exit" to stop the program.
'''





'''
2\. A cinema ticket booking system asks the customer to enter their age.
Customers aged between 1 and 100 are accepted. 
Ask the customer to enter their ticket type, which must be either "standard" or "student". 
If the age or ticket type is invalid, display an error message and ask again. 
Allow the customer to enter "exit" at any time to stop the program.
'''





'''
3\. A supermarket checkout system asks the cashier to enter the price of each product. 
Each price must be a valid positive number. Keep accepting prices until the cashier enters "done".
If the cashier enters an invalid price, display an error message and ask again. 
Store all valid prices in a list and display the total price and the number of products entered at the end.
'''






'''
4\. A hotel reservation system collects the ages of guests checking into a hotel. 
Keep asking for ages until the receptionist enters "done". 
Each age must be a number between 1 and 100. 
Reject invalid entries and continue asking. Store accepted ages in a list. 
At the end, display the number of guests, the youngest guest's age, the oldest guest's age, and the average age.
'''





'''
5\. A delivery company needs to record the delivery distances for its daily orders. 
Ask the employee to enter each distance in kilometers. 
A valid distance must be greater than 0 and no more than 500. 
Continue asking until the employee enters "done". 
Reject invalid entries and store valid distances in a list. 
At the end, display all accepted distances, the total distance, and the number of deliveries. 
Also display how many deliveries were longer than 100 kilometers.

'''





'''
6\. A small business wants to track its daily sales. 
Repeatedly ask the employee to enter a product name and its sales amount. 
Product names must not be empty, and sales amounts must be positive numbers. 
Allow the employee to enter "done" as the product name to finish. 
Store each product name and its sales amount in a dictionary. 
If an invalid sales amount is entered, ask for the amount again without requesting the product name again. 
At the end, display each product with its sales amount, the total sales, and the product with the highest sales amount.

'''


'''
7\. A vehicle rental company needs a program to manage vehicle rentals. 
Create a dictionary containing vehicle registration numbers as keys and rental prices per day as values. 
Repeatedly display a menu with the options to view available vehicles, rent a vehicle, return a vehicle, and exit. 
When renting a vehicle, ask for the registration number and the number of rental days. Reject unknown registration numbers, invalid day counts, and vehicles that are already rented. 
When returning a vehicle, verify that the registration number belongs to a currently rented vehicle. 
Track rented vehicles separately from available vehicles. 
Use a while loop to keep the menu running until the user selects exit. 
Use for loops to display vehicles and calculate the rental cost. 
Include suitable error messages and use try-except to handle invalid numeric input.

'''
