# #DICTIONARY METHODS

# #GETTING A LIST OF KEYS
# print(student_score_info.keys())

# #GETTING A LIST OF VALUES
# print(student_score_info.values())

# #GETTING A LIST OF KEY,VALUE PAIRS
# print(student_score_info.items())

# ASSIGNMENT
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

# no_of_coffee_sold = int(input('Enter the no of coffee sold: '))
# no_of_tea_sold = int(input('Enter the no of tea sold: '))

# drinks_sold={'coffee': no_of_coffee_sold, 'tea':no_of_tea_sold}
# print(drinks_sold)


'''
2. A sports club keeps the names of players and their scores in a dictionary. 
Create a dictionary containing 5 players and their scores. 
Use a for loop to print each player's name and score. 
If a player's score is 50 or higher, also print that the player passed. 
Otherwise, print that the player failed.
'''
# sports_club={'Gautam': 77, 'Praveen':91, 'John':56, 'Max':50, 'Tally':45}
# for i , j in sports_club.items():
    
#     print(f'{i}: {j}')

#     if j >=50:
#         print('passed')
#     else:
#         print('failed')

'''
3. A supermarket wants to keep track of its stock. 
Create a dictionary containing 5 products and the number of items currently available. 
Use a for loop to display every product and its stock quantity. 
If the stock of a product is below 10, display a message saying that the product needs to be restocked.
'''
# stocks={'sweets':21, 'soap': 11, 'salt': 9, 'bread': 14, 'milk': 7}
# print(stocks)

# for i, j in stocks.items():
#     print(f'{i}:{j}')
#     if j<=10:
#         print(f'{i} needs to be restocked')

'''
4. A bus company wants to record the number of passengers travelling on several buses. 
Create a dictionary containing the bus number as the key and the number of passengers as the value. 
Use the keys() method to display all bus numbers. 
Use the values() method to calculate how many passengers are travelling in total. 
Then use items() to display each bus number and its passenger count.
'''

# bus_details={'NL521234': 23, 'NL236767': 24, 'NL524342': 33, 'NL121234': 31}
# print(bus_details)
# for i in bus_details.keys():
#     print(i)

# total_passenger = 0
# for j in bus_details.values():
#     total_passenger = total_passenger + j
# print(f'total_passenger: {total_passenger}')

# for k,l in bus_details.items():
#     print(f'{k}: {l}')


'''
5. A hospital reception system stores each patient's name and their assigned room number in a dictionary. 
Ask the user to enter the name of a new patient and their room number, then add the patient to the dictionary. 
Ask the user for a patient's name and display their room number if the name exists in the dictionary. 
If the name does not exist, display a suitable message.
'''
# patient_details = {'John': 12, 'Karl': 21, 'Max': 22, 'Lex':24, 'Kim': 9}

# name_patient= input('Enter name: ')
# room_number = int(input('Enter room number: '))

# patient_details[name_patient]=room_number
# print(patient_details)


# search_names=input('Enter patient name: ')


# if search_names in patient_details.keys():
#         print(f'{search_names} room number is {patient_details[search_names]} ')
# else:
#         print(f'{search_names} is not registered')
    
'''
6. A warehouse records the quantity of different products in a dictionary. 
Create a dictionary containing at least 6 products and their quantities. 
Use a while loop to repeatedly ask the user for a product name. 
If the product exists, display its current quantity. 
If the user enters "stop", end the program. 
Keep track of how many valid products the user searched for and display the total when the loop finishes.
'''
warehouse_records = {
    'salt': 102,
    'milk': 105,
    'biscuit' : 99,
    'lux' : 87,
    'dove' : 35,
    'cinthol' : 21
    }
count = 0
while True:
    product_name = input('Enter product name: ').lower().strip() # Sanitize & Clean: .lower().strip()

    if product_name =='':                                        # Guard Clause: if product_name == '': continue
        continue

    elif product_name == 'stop':                                # Exit Strategy: elif product_name == 'stop': break
        break

    elif product_name in warehouse_records.keys():              # Business Logic: elif product_name in warehouse_records.keys(): ... 
        print(f'{product_name} quantity is {warehouse_records[product_name]}')
        count += 1

    else:                                                       # Fallback: else: ...
        print(f'{product_name} is a invalid product name')
print(f'Total valid product searched is {count}')

'''
7. A delivery company wants to analyse the delivery performance of its drivers. 
Store each driver's name and number of successful deliveries in a dictionary. 
Use a for loop to examine every driver. 
Store the names of drivers who completed at least 20 deliveries in a list. 
Store the names of drivers who completed fewer than 20 deliveries in another list. 
Use a tuple to store the minimum and maximum delivery targets. 
Then use if conditions to determine which drivers met the minimum target and display the results. 
Finally, display the two lists and the target tuple.
'''





