
'''
Shopping List Manager

Write a Python program to manage a shopping list.

Start with the following shopping list: rice, milk, eggs, and bread.

1. Print the shopping list.
2. Ask the user to enter an item they want to buy.
3. If the item is already in the shopping list, print "Item already exists".
4. Otherwise, add the item to the shopping list and print "Item added successfully".
5. Ask the user to enter an item they want to remove.
6. If the item exists in the shopping list, remove it and print "Item removed successfully".
7. Otherwise, print "Item not found".
8. Print the final shopping list and the total number of items remaining.
'''
# shopping_list=['rice','milk','eggs','bread']
# print(shopping_list)

# item=input('Entet the item you want to buy:')
# print(item)

# if item in shopping_list:
#     print('Item already exists')
# else:
#     shopping_list.append(item)
#     print(f'{item} is added successfully')

# remove_item=input('Enter the item you want to remove: ')
# print(remove_item)

# if remove_item in shopping_list:
#     shopping_list.remove(remove_item)
#     print('Item removed successfully')
# else:
#     print('Item not found')

# print(f'Final shopping list is: {shopping_list}')
# print(f'Total no of items remaining is: {len(shopping_list)}')

'''
1. A school stores the marks of five students in a list. 
Write a program that prints the first student's mark. 
If the mark is 50 or above, print "Pass". Otherwise, print "Fail".
'''
# student_marks=[89,32,44,66,78]
# print(student_marks[0])

# for i in range(len(student_marks)):
#     if student_marks[i]>=50:
#         print('Pass')
#     else:
#         print('Fail')

'''
2. A supermarket has a shopping list containing "Milk", "Bread", and "Eggs".
Check whether "Butter" is in the list. If it is not there, add it to the end of the list. 
Print the updated list.
'''
# shopping_list=['Milk', 'Bread', 'Eggs']

# if 'Butter' in shopping_list:
#     print(shopping_list)
# else:
#     shopping_list.append('Butter')
#     print(shopping_list)

'''
3. A music player stores songs in a playlist.
Print the last song using negative indexing. 
If "Imagine" is in the playlist, print "Favourite song found". 
Otherwise, print "Favourite song not found".
'''
# playlist=['Party', 'Eugene', 'Glamorous life']
# print(playlist[-1])

# if 'Imagine' in playlist:
#     print('Favorite song found')
# else:
#     print('Favorite song not found')

'''
4. A shop stores product prices in a list.
Print the highest and lowest prices. 
If the highest price is greater than 1000, print "Expensive product available". 
Otherwise, print "All products are affordable".
'''
# prices=[899,999,1099, 1000,2000,199]
# print(f'Highest price is :{max(prices)}')
# print(f'Lowest price is :{min(prices)}')

# if max(prices) >1000:
#     print('Expensive product available')
# else:
#     print('All products are affordable')

''' 
5. A teacher stores student marks in a list.
Count how many times the mark 75 appears.
If 75 appears in the list, print "Several students may have scored 75" if it appears more than once. 
Otherwise, print "75 appears once". 
If it does not appear, print "No student scored 75".
'''
# count = 0
# student_marks= [56, 65,89, 75, 79, 69, 66, 86, 75, 76, 79, 75]
# for i in range(len(student_marks)):
#     if student_marks[i] == 75:
#         count = count+1

# if count>1:
#     print('Several students may have scored 75')
# elif count==1:
#     print('75 appears once')
# else:
#     print('NO student scored 75')

# print('Total count =',count)

'''
6. A grocery store has a list of items.
Replace the second item with "Rice". 
If "Sugar" is in the list, remove it. 
Otherwise, add "Sugar" to the list. Print the final list.
'''
# items=['Butter', 'Bread', 'Milk', 'Pasta']
# print(items)
# items[1]='Rice'
# print(items)

# print(f'Items before remove: {items}')
# if 'Sugar' in items:
#     items.remove('Sugar')
#     print(f'Items after remove: {items}')
# else:
#     items.append('Sugar')
#     print(f'Item after added Sugar: {items}')

'''
7. A company stores daily sales figures in a list. 
Calculate the total sales and average sales. 
If the average is greater than or equal to 500, print "Sales target achieved". 
Otherwise, print "Sales target not achieved".
'''
# daily_sales=[100, 200, 400, 500, 300, 480, 600]
# total_sales=0

# for i in range(len(daily_sales)):
#     total_sales=total_sales+daily_sales[i]

# print(f'Total sales is: {total_sales}')

# average = sum(daily_sales)/len(daily_sales)
# print(f'Average sales: {average}')

# if average >=500:
#     print('Daily sales achieved')
# else:
#     print('Sales target not achieved')


'''
1. A local coffee shop wants to keep track of its daily sales.
Create variables to store:
* The shop name
* The number of coffees sold
* The price of one coffee
* Whether the shop is open
Then use an if condition to display a message depending on whether the shop is open or closed.
'''




'''
2. A cinema wants to check whether a customer can watch a movie.
Ask the user for:
* Their name
* Their age
If the customer is 18 or older, display a message saying they can watch the movie.
Otherwise, display a message saying they must choose an age-appropriate movie.
'''


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


'''
4. A school wants to record the names of students who joined different school clubs.
Create a list containing 10 student names.
Ask the user for a student name.
Use an if condition to check whether the name exists in the list.
If the student is in the list, display a message saying they are registered for a club.
Otherwise, display a message saying they are not registered.
'''





'''
5. A fitness center wants to check whether people are allowed to use a particular exercise machine.
Create a list containing the names of 8 members.
Ask the user for their name and age.
If the person's name is in the member list and their age is 16 or older, display a message saying they can use the machine.
Otherwise, display a message explaining that they cannot use the machine.
'''




'''
6. A delivery company has a list of delivery package weights from one day.
Create a list containing 10 package weights.
Use range() to create a sequence of numbers from 1 to 10.
Use the numbers to access the package weights from the list.
For each package, use an if condition to check whether its weight is greater than 10 kg.
Display whether each package is within the standard weight limit or requires special handling.
'''


'''
7. A wildlife research team is monitoring animals in a national park.
Create a list containing 10 animal names.
Ask the user to enter an animal name they want to search for.
If the animal exists in the list, display its position in the list using its index.
Also check whether the animal is one of the first 5 animals or one of the last 5 animals in the list.
If the animal does not exist in the list, display a message saying that the animal was not recorded.
Use variables, user input, if conditions, lists, indexing, list slicing, and range() where appropriate.
'''

#MULTI DIMENSIONAL LISTS
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
# print(matrix[1][2])  
# print(matrix[2][1]) 
# print(matrix[0][2])  




'''
A temperature measuring sensor takes 3 readings per day. 
it saves it in a list. and these lists are saved in a another list for the month. 

Hence the resulting list is a 30 x 3 matrix. 

Create a program that will simulate the temperature reading for two days. 
Print the resulting matrix at the end. 
Use input function to get the temp value from the user for each reading.
'''




# For loops 

''' 1. A delivery company stores the delivery times of five packages in a list. 
Write a program that goes through the list and prints each delivery time with an additional 15 minutes added to it.
'''
# delivery_times= [30, 45, 10, 15, 25]
# for i in delivery_times:
#     print(i+10)

''' 
2. A supermarket stores the prices of its products in a list. 
Write a program that uses enumerate() to print each product's position and price. 
If a product costs more than 2000, print "Expensive product" next to its price.
'''
# price_of_products=[1250,1333,1344,1900,2100,2200,2000]

# for position, price in enumerate(price_of_products):
#     if price > 2000:
#         print(f'position {position+1} price is {price} Expensive produce')
#     else:
#         print(f'position {position+1} price is {price} ')

''' 
3. A school stores the names of students in a list. 
Write a program that goes through each name and prints it. 
If the name is "Kamal", print "Student found" and stop checking the remaining names. 
If the name is "Nimal", skip printing that name and continue checking the remaining students. 
'''
# names_of_student=['Nimal', 'Riman', 'Gimon', 'Heman', 'Ironman', 'Lokman', 'Tilakman', 'Jhilakman', 'Kamal']
# for name in names_of_student:
#     if name == 'Nimal':
#         continue

#     if name == 'Kamal':
#         print(f'Student found')
#         break
#     print(name)
    
''' 
4. A cinema has 3 rows of seats, with 4 seats in each row. 
Write a program that uses nested for loops to print every seat number along with its row number. 
After that, use a list of ticket prices to check each price. 
Skip prices below 500, print "Discount ticket" for prices between 500 and 1000 inclusive, and print "Premium ticket" for prices above 1000.
'''

# for rows in range(1,4):
#     for seats in range(1,5):
#         print('Row No', rows, 'Seat No', seats)

# ticket_prices=[250, 450, 550, 1000, 1250]
# for price in ticket_prices:
#     if price <500:
#         continue

#     elif price <=1000:
#         print ('Price', price, 'Discount ticket')
    
#     else:
#         print('Price', price,'Premium ticket')



# Lists and for loops homework 

'''
1. A library stores the daily number of books borrowed over five days in a list. 
Write a program that prints the number of books borrowed on the first day and the last day. 
Then, use a for loop to print every daily borrowing count with 2 additional books added to each value.
If a daily count is greater than 10, print "Busy day" as well.
'''




'''
2. A grocery store keeps a list of fruit names.
Ask the user to enter a new fruit name. If the fruit is already in the list, print "Fruit already exists". Otherwise, add the fruit to the end of the list. Then, print the total number of fruits and display the first three fruits using list slicing.

'''




'''
3. A gym stores the names of its registered members in a list.
Ask the user to enter a member's name. If the name exists in the list, print "Member found". Otherwise, print "Member not found". Then, use a for loop with enumerate() to display the position and name of each member, skipping any member whose name starts with the letter "A". Finally, ask the user whether they want to remove a member. If they answer "yes", ask for the member's name and remove that member if the name exists in the list.
'''




'''
4. A hotel has 3 floors with 4 rooms on each floor. 
Use nested for loops and the range() function to display every floor number and room number. 
Then, create a list containing the prices of five room bookings. Use a for loop to calculate and print the total booking revenue, the highest booking price, and the lowest booking price. 
Ask the user to enter a minimum price and print only the booking prices that are equal to or greater than that amount. Skip any booking price below 1000 when displaying the qualifying prices.
'''


'''
Get 3 numbers from the user using a while loop
add the numbers to a list and print the average of the those numbers in the end
'''

# number_list=[]

# while True:
#     no=int(input('Enter no: '))
#     number_list.append(no)

#     if len(number_list) == 3:
#         break

# average=sum(number_list)/len(number_list)
# print(average)

'''
The Problem: The Smart Cash Register

You are building software for a smart cash register. The register processes a list of prices one by one. Write a program that uses a while loop to process items according to these specific business rules:
1. The Loop Setup: Loop through the list of item prices.
2. The continue Rule: If an item's price is negative, it represents a bug in the scanning system. Skip the item entirely without adding it to the total or counting it, and move to the next item.
3. The break Rule: If an item's price is exactly 0, it means the cashier has scanned the special "End of Transaction" barcode. Stop processing immediately and exit the loop (do not look at any remaining items in the list).
4. Normal Processing: Otherwise, add the valid price to the running total_bill and increase the item_count by 1.
'''

# item_prices = [23,65,-3,459,2432,-78,398,233]
# total_bill = 0
# item_count = 0
# i=0

# while i < len(item_prices):
#     current_price = item_prices[i]


#     if current_price == 0:
#         break


#     if current_price < 0:
#         i=i+1
#         continue  

#     total_bill += current_price
#     item_count +=1

#     i=i+1

# print("--- Transaction Summary ---")
# print(f'Total bill is : {total_bill}')
# print(f'Item count is : {item_count}')

#####
# item_prices = [23,65,-3,459,2432,-78,398,233]
# total_bill = 0
# item_count = 0
# i=0

# while True:
#     if i >= len(item_prices):
#         break
    
#     current_price = item_prices[i]

#     if current_price == 0:
#         break


#     if current_price < 0:
#         i=i+1
#         continue  

#     total_bill += current_price
#     item_count +=1

#     i=i+1

# print("--- Transaction Summary ---")
# print(f'Total bill is : {total_bill}')
# print(f'Item count is : {item_count}')





