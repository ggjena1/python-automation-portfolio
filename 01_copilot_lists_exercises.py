# print all items of a list
names = ['Gautam', 'Ravi', 'Sita', 'Mohan']
for i in names:
    print(i) # Gautam # Ravi # Sita # Mohan


# Add items to a list
numbers = []
numbers.append(10)
numbers.append(20)
numbers.append(30)

print(numbers) # [10,20,30]

# Replace an item
cities = ['Eindhoven', 'Amsterdam', 'Rotterdam']
cities[1] = 'Utretcht'
print(cities) # Eindhoven Amsterdam Rotterdam


# Remove an item
languages = ['Python', 'Java', 'C++', 'Go']
languages.remove('Java')

print(languages)

# loop + condition
numbers = [1,2,3,4,5,6]
for n in numbers:
    if n%2 == 0:
        print('Even:', n)


# sum of list
nums = [10, 20,30,40]
total = 0

for n in nums:
    total +=n 
print('Total:', total)


# find the largest number
nums = [3,9,1,7,4]
largest = nums[0]

for n in nums:
    if n > largest:
        largest = n
print('largest:', largest)

# create a list from user input
items = []
for i in range(3):
    item = input("Enter item: ")
    items.append(item)
print(items)

# Nested list loop
matrix = [[1,2],[3,4],[5,6]]

for row in matrix:
    for num in row:
        print(num)

# Convert list to uppercase
words = ['Python', 'loops', 'lists']

for w in words:
    print(w.upper())

    
