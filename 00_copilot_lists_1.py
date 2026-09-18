# List: is a collection of items stored in one variable.
fruits = ['apple', 'banana', 'mango']
# a list can contain strings, numbers, booleans, mixed types, even other lists
mixed = [10, 'Gautam', True, 3.14]
# why lists are important? because you use them for : loops, automation, file processing, web scraping, excel automation, APIs etc. Lists are everywhere.

# Basic list operation
# access items
fruits = ['appel', 'banana', 'mango']
print(fruits) # appel banana mango
print(fruits[0]) # appel
print(fruits[1]) # banana

# change items
fruits[1] = 'Orange'
print(fruits) # appel Orange mango

# Add items
fruits.append('grapes')
print(fruits) # appel Orange mango grapes

# Remove items
fruits.remove('appel') 
print(fruits) # Orange mango grapes

# length of list
print(len(fruits)) # 3

# loop through list
for fruit in fruits:
    print(fruit) # Orange # mango # grapes 


    









