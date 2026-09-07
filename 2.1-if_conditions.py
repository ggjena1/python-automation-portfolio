'''

'''

#get users age and then classifiy them as adults or not 

# age = int(input("Please enter your name: "))

# if age>=18:
#     print("you are an adult")
# else:
#     print("you are a child")

# #two variables are the same
# name = input("Please enter the character name: ")
# characterName = 'Cullen'

# if name == characterName:admin
#     print("character confirmed")


'''
== are they equal? 
> bigger than 
< less than 
>= bigger than  or equal to 
<= less than or equal to 
!= is it not equal to?
'''

'''
Get the username from the user 
if the username is equal to admin, print 'Authorized!'
Otherwise print 'Unauthorized!'
'''

# uname=input("Please enter the username : ")
# charname= "Admin"

# if uname == charname:
#     print('Authorized')
# else:
#     print('Unauthorized')


'''
classify a given score as either 

good  75 (included) to 100
okay 45 (included) to 75
bad 0(include) to 45


------0------------45------------75-----------100------
          bad            okay          good
'''

# score = int(input("Please enter your score: "))
# if score<45:
#     classifcation= 'bad'
# elif score>44 and score<75:
#     classification = 'okay'
# else:
#     classification = 'good'

'''
Write a Python program to get the user’s age and print their life stage as shown below:

Age between 0 (included) and 12 → Child
Age between 12 (included) and 19 → Teenager
Age between 19 (included) and 60 → Adult
Age between 60 (included) and 120 → Senior
'''

age = int(input('Enter age: '))

if age <12:
    print('Child')
elif age>=12 and age <19:
    print('Teenager')
elif age>=19 and age <60:
    print('Adult')
else: 
    print('Senior')



