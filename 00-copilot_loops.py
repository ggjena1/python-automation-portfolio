for i in range(1,6):
    print('Hello Gautam', i)


for i in range(1,11):
    print("Number:", i)

# loops + Condition
# print even numbers
for i in range(1,21):
    if i%2 == 0:
        print("Even:",i)


# loop through a list
fruit = ['apple', 'banana', 'mango', 'orange']
for i in fruit:
    print('I like', i)


# loop through a characters in a string
word = 'PYTHON'
for i in word:
    print('Letter is ', i)


# Nested Loops
# Understand how loops work inside loops
for i in range(1,4):
    for j in range(1,4):
        print('i:', i, 'j:',j)


# sum of numbers
total = 0
for i in range(1,11):
    total +=i

print('Total:', total)


# Understand break
# Goal is to understand break
for i in range(1,20):
    if i == 7:
        break
    print(i)

# Continue the loop
for i in range(1,10):
    if i==5:
        continue
    print(i)


# loop with user input
name = input("Enter your name: ")
for i in range(3):
    print("Hello", name)


# loop through dictionary
person = {
    "name": "Gau",
    "city": "Amsterdam",
    "Language": "Python"
}

for key, value in person.items():
    print(key, ":", value)



# Additional Questions from Copilot

'''Use nested loop to print every temperature
Add 2 degrees to each temperature and print the updated value.
'''

temps = [
    [21, 23, 25, 22],
    [19, 20, 18, 21],
    [24, 26, 27, 25]
]

for i in temps:
    for j in i:
        print(f'old temp is : {j} and updated value after additional 2 degree is: {j+2}')

'''
A school stores grades of 3 classes, each with 3 students:
1. Add 10 marks to each grade
2. Print “Pass” if updated grade ≥ 50, else “Fail”
3. Store all updated grades in a list
4. Print the highest updated grade
'''
grades = [
    [45, 55, 65],
    [35, 75, 85],
    [50, 40, 90]
]

updated_mark = []

for i in grades:
    for j in i:
        new_mark= j+10
        print(j, new_mark)

        if new_mark >= 50:
            print('Pass')
        else:
            print('Fail')
        updated_mark.append(new_mark)

highest_mark = max(updated_mark)
print(f'Highest Mark is :  {highest_mark}')