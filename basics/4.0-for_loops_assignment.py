#Homework: Assignment
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

# 2nd solution: final solution for review
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

# 2nd solution: final solution for review
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

    
