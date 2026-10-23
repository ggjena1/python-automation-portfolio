'''
Print from 1 to 50 using a for loop

'''

# for _ in range(1,51):
#     print(_, end = ' ')


# for _ in range(1,51):
#     print(_)

'''
Get 5 numbers from the user. calculate and print the average of that number
'''

# nums = [] 
# sum_of_nums = 0

# for i in range(5):
#     num = int(input('Enter a number: '))
#     nums.append(num)

# sum_of_nums = sum(nums)
# average = sum_of_nums / 5
# print(average)

'''
Get a number from the user and print a half a pyramid pattern for that many rows. 
For an instance if the number user entered is 5, print below pattern 

*     1 x *
**    2 x *
***   3 x *
****  4 x *
***** 5 x *
'''

# num = int(input('Enter a number: '))

# for i in range(num):
#     print((i+1) * '*')


'''
Get a number from the user and print a pyramid pattern for that many rows. 
For an instance if the number user entered is 5, print below pattern 

    *         1 x * 
   ***        3 x *
  *****       5 x *
 *******      7 x *  
*********     9 x *

spaces are strings as well just like '*'
just like multiplying *, you can multiply spacess
apart from multiplying, you can add characters/strings together
'''
# num = int(input('Enter a number: '))
# for i in range(num):
#     print( (2*i+1) *  '*')

'''
Get 5 numbers from the user. 
Calculate the average and print it back.
'''

# numbers= []
# for i in range(5):
#     num=int(input('Enter numer: '))
#     numbers.append(num)
# print(numbers)
# average = sum(numbers) / 5
# print(average)

'''
get a number from the user
print the multiplication table for that number

1 x 7 = 7
2 x 7 = 14 
3 x 7 = 21


f string 
'''

# num= int(input('Enter a num: '))
# for i in range(1,13):
#     multi= i * num 
#     print(f'{i} x {num} = {multi}')
    
'''
Yuo have been given a list of temperature readings in farenheit
Convert them to Celcius

the equation to conver a farenheit value to celcius is 

°C = ( °F - 32 ) ÷ 1.8
'''

# temps = [32,54,11,56,86,34]

# for temp in temps:
#     cel = (temp - 32) / 1.8
#     print(cel) 

'''
Get 5 names from the user. 
Determine the length of each name and put the lengths into a list and print it back
'''

name_lens = []
names= []

for i in range(5):
    name = input('Enter a name: ')
    names.append(name)
    name_lens.append(len(name))
print(name_lens)

'''
You are creating a simple pos system 
ask the user how many unique number of products they got
then get 

- name
- price
- quantity 

for each type of product 
and the print the final bill with product name, price, quantity and final price 


product name    price_per_item    quantity    price   
apples          10                5           50
milk carton     15                2           30

full price                                    80

use f string for the bill 
perform string addition 
'''

n= int(input('Enter how many products: '))


