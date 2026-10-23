''' Exercise 1: Count from 1 to 10'''
# for i in range(1,11):
#     print("Iteration:", i)

'''Use a loop to calculate the sum of the numbers from 1 to 10, then print the total'''

# total=0
# for i in range(1, 11):
#     total += i
# print(f'The sum of numbers from 1 to 10 is: {total}')


'''Use a loop to print the multiplication table of a given number (e.g., 5) from 1 to 10'''
# num=5
# for i in range(1, 11):
#     result=num*i
#     print(f'{num} x {i} = {result}')

'''Use a for loop to print the numbers from 10 down to 1.'''
# for i in range(10,0,-1):
#     print(i)


'''Use a loop to print all the even numbers from 2 to 20.'''
# for i in range (2,21,2):
#     print(i)

'''Use a loop to calculate the sum of the numbers from 1 to 100, then print the total'''
# total = 0
# for i in range(1, 101):
#     total += i
# print(f'The sum of numbers from 1 to 100 is: {total}')


# num= int(input("Enter a number to print its multiplication table: "))
# for i in range(1, 11):
#      result = num * i
#      print(f'{num} x {i} = {result}')



'''Use a while loop to print the numbers from 1 to 5.'''
# i=1
# while i<=5:
#     print(i)
#     i=i+1



# for i in range(1, 21):
#     print(i)

# for i in range(1, 20):
#     if i % 2 != 0:
#         print(i)

# for i in range(3, 31,3):
#     print(i)

# for i in range(20, 0, -1):
#     print(i)

# word='Python'
# for i in word:
#     print(i)


# count = 0
# for i in range(1, 51):  
#     if i % 5 == 0:
#         count += 1
# print(count)

'''
'''
'''Print numbers from 1 to 50 but skip multiples of 7.'''

for i in range(1,51):
    if i%7==0:
        continue
    print(i)

'''Print all even numbers between 10 and 30.'''

for i in range(10,31):
    if i%2==0:
        print(i, end=" ")

'''Print characters of `"integration"` but stop when you reach `'g'`.'''
word = 'integration'
for i in word:
    if i=='g':
        break
    print(i)

'''Print squares of numbers from 1 to 10'''
for i in range(1,11):
    print(i*i, end=" ")

'''Print numbers from 20 down to 1 (reverse loop).'''
for i in range(20,0,-1):
    print(i)







