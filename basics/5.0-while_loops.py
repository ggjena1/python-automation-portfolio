'''
WHILE LOOPS IN PYTHON

We use for loops when you want to  repeat a task a fixed number of times

asking the user for their age

-age must be positive
-age must be less than 90 

'''

'''
write a for loop that will print from 1 to 10 
'''
# for i in range(1,11):
#     print(i)

# i=1
# while i<=10:
#     print(i)
#     i=i+1

'''
Get the users age
the age should be above 0 and less than 90 
if the user enters an age that is beyond these given limits, the answer should be rejected and the question must be 
asked again. 

if the user enters an age that is out of bounds (less than 0 or above 90), print a suitable error message 
before prompting for the age again
'''


# while True: 
#     age=int(input('Enter the age: '))
#     if age>0 and age<90:
#         break
#     else:
#         print('Age is not correct')
    

'''
ask the user for a number
then collect that many numbers to a list
print the aveerage of those numbers
(don't use a for loop)
'''

number_of_elements_needed=int(input('Enter a no of element: '))
num_list=[]

sum=0

while True:
    num=int(input("Please enter a number: "))
    num_list.append(num)
    if len(num_list) == number_of_elements_needed:
        break
        
#calculate the average and print it
average = sum(num_list)/number_of_elements_needed
print(f'Average is : {average}') 


# HOMEWORKK 

'''
1. A shopping mall wants to create a simple age verification system for visitors. 
Write a Python program that asks the visitor to enter their age. 
If the age is greater than 0 and less than 90, print "Access granted". Otherwise, print "Invalid age". Use an if-else statement to check the age.
'''


while True:
    age=int(input('Enter Age:'))
    if age >0 and age <90:
        print('Access Granted')
        break
    else:
        print('Invalid Age, try again')






''' 
2. A supermarket wants to calculate the total cost of groceries purchased by a customer. 
Write a Python program that asks the user how many items they purchased. 
Then use a for loop to collect the price of each item. 
Calculate and display the total cost. If the total cost exceeds 10000, print "Eligible for a special discount". Otherwise, print "No discount available".
'''




'''

3. A fitness center wants to collect the daily step counts of its members. Write a Python program that asks the user how many days they want to record. Use a while loop to collect the step count for each day and store the values in a list. After collecting all the values, calculate and display the total steps and average daily steps. If the average is greater than or equal to 10000, print "Daily step goal achieved". Otherwise, print "Daily step goal not achieved". Do not use a for loop.

4. A company wants to develop an employee registration system. Write a Python program that asks the user to enter the number of employees to register. For each employee, collect their name and age using a for loop. The age must be greater than 0 and less than 90. If the entered age is invalid, display an error message and ask for the age again using a while loop. Store all employee names and ages in separate lists. Once all employees have been registered, display the names and ages of all employees.

5. A restaurant wants to develop a simple food ordering system. Create a Python program that asks the customer how many food items they want to order. Use a while loop to collect the price of each item and store the prices in a list. Each price must be greater than 0. If the customer enters an invalid price, display an error message and ask again. After collecting all prices, calculate the total bill and average item price. Use an if-else statement to apply a 10 percent discount if the total bill exceeds 5000. Finally, display the original bill, discount amount, and final bill.

6. A school wants to build a student marks management system. Write a Python program that asks the teacher how many students they want to record. For each student, ask for their name and marks in three subjects. Each mark must be between 0 and 100. Use while loops to validate the marks and repeat the question whenever an invalid mark is entered. Store the student names and their total marks in separate lists. Use a for loop to calculate each student's average and determine whether they passed or failed. A student passes if their average is at least 50 and they have scored at least 35 in every subject. Display each student's name, total marks, average, and result.

'''
'''
7. A delivery company wants to develop a daily delivery tracking system.
Write a Python program that asks the manager how many deliveries were completed during the day. 
The number of deliveries must be greater than 0 and less than 100. 
If an invalid number is entered, display an error message and ask again using a while loop. 

For each delivery, collect the delivery distance in kilometers and the delivery fee. 
Both values must be greater than 0. Validate each input using while loops. Store the distances and fees in separate lists.

After collecting all delivery records, use a for loop to calculate the total distance traveled, 
total delivery revenue, and average delivery distance. 
Determine the highest delivery fee and the longest delivery distance. 
If the total delivery revenue exceeds 20000, display "Daily revenue target achieved". 

Otherwise, display "Daily revenue target not achieved". 

Finally, display a summary of all deliveries, including the total number of deliveries, total distance, average distance, total revenue, highest delivery fee, and longest delivery distance.

'''
print()
while True:
    no_of_deliveries=int(input('Enter total no of deliveries: '))

    if no_of_deliveries >0 and no_of_deliveries < 100:
        print('Valid entries')
        break
    
    else:
        print('Invalid entry')

for 
