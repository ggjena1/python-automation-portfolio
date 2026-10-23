'''
You are creating a studentn score dictionary 
Ask the teacher for the number of students. 

Collect the names and scores of those students and create a dictionary.
'''

# no_of_student = int(input('Enter no of students: '))
# i=1
# student_score={}



# while i<=no_of_student:
#     name= input('Enter the name')
#     score = int(input('Enter scores: '))
#     student_score[name]=score
#     i=i+1
# print(student_score)

'''

Create a program for a bookstore manager to log new book arrivals.

1. Ask for the total number of book titles to add to the inventory.
2. Use a loop to ask for the book title and its quantity for each book.
3. Store each book title and quantity if there are more than 50 books, as a key-value pair in a dictionary.
4. Print the average number of books in the inventory at the end. 
'''


# no_of_books_to_add = int(input('Enter the no of books to add in to the inventory: '))

# bookstore_inventory={}

# while True:
#     book_title=input('Enter the book title: ')
#     quantity = int(input('Enter the quantity: '))

#     if quantity >=50:
#         bookstore_inventory[book_title]=quantity

#     if len(bookstore_inventory)==no_of_books_to_add:
#         break


# average= sum(bookstore_inventory.values())/len(bookstore_inventory)
# print(average)



'''
C- Create
R- Read
U- Update
D- Delete

Store all product information in a dictionary. Use each product's name as the key and its stock quantity as the value.
Your program should display a menu repeatedly until the user chooses to exit.
1. Add a product: Ask the user for a product name and its stock quantity. Add the product to the dictionary. If the product already exists, display an error message.
2. View all products: Display the name and stock quantity of every product in the dictionary. If there are no products, display a suitable message.
3. Update stock: Ask the user for a product name. If it exists, ask for the new stock quantity and update the dictionary. Otherwise, display an error message.
4. Delete a product: Ask the user for a product name. If it exists, remove it from the dictionary. Otherwise, display an error message.
5. Exit: Stop the program.

'''

# product_info={}

# while True:
#     product_name= input('Enter product name: ')
#     product_quantity=int(input('Enter Quantity: '))

#     if product_name in product_info.keys():
#         print('Invalid , Prodcut exists')

    
#     else:
#         product_info[product_name]=product_quantity

#     if p



'''
1. Create a simple application with a dictionary for student score management. 
The program should always ask the student name and the score. every time they are provided add them to the dictionary and print
the entire dictionary. 
The program shoudl end if the user enters 'exit' for the student name. Otherwise the program should keep running.

2. Also add an option to update the existing students score. 

3. Add an option to remove a student and their score from the dictionary 

---------------------------

--------------------------



'''
msg = '''
1. Add a new student
2. Update existing student 
3. Remove student 
4. Exit 
'''
student_score={}

while True:
    print(msg)
    num=int(input('Select Number 1, 2 or 3 : '))

    if num == 1: 
        name  = input('Enter student name: ')    
        if name in student_score:
            score= int(input('Enter the new student score: '))
            student_score[name]=score

    elif num == 2: 
        # if the dictionary is empty, ask the user to add a student first
        name  = input('Enter student name: ')    
        if name in student_score:
            score= int(input('Enter the new student score: '))
            student_score[name]=score
        else:
            print('student not found!')
        

    elif num==3: 
        # if the dictionary is empty, ask the user to add a student first
        name = input("please enter student name to remove: ")
        if name in student_score:
            student_score.pop(name)
        else:
            print("student not found!")
    
    elif num == 4: 
        break

    else:
        print("invalid input!")





















