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
