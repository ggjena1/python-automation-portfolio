'''
Escape sequences 
'''

print(1,"Hello\nworld")
print(2,"Hello\tworld")

print(3,"Hello\\world")
print(4,"C:\\Users\\Gautam")

print(5,"He said \"hello\"")
print(6,'He said \'hello\'')

print(7,'He said "hello"')
print(8,"He said 'hello'")

print(9,"Hello World\rWorld")
print(10,"Hello\bWorld!")
print("\a")

msg = f'''
*** Welcome to the Store!! ***

Item name:  
Item price: 12 USD
Quantity:   1
------------------
Final Price: 12 USD

'''

# print(msg)

# print("*** Welcome to the Store!! ***\nItem name:\tRadio\nQuantity:\t12 USD")
# print("------------------")
# print("Final Price: 12 USD")



'''
You have been tasked with creating a small piece of code that will generate a customized bill for a user. Below is the 
format. Assume the user can only buy one type of item. 
Get the item name from the user 
Get the number of items from the user.  
Get the quantity 

And calculate the final price. 

*******************************
Welcome to the Kabeer's Cool Electronics

        Final Bill 
        
Item: CD Player
Quantity: 7
Item Price: 56 USD
--------------------
Net Price: 56 USD
===================

Thank you for shopping at 
Tray Electronics. Come again
Soon!
******************************
'''





item_name = input("Please the name of the item: ")
quantity = int(input("Enter number of items you bought: "))
item_price = int(input("Enter price of item: "))
net_price = quantity * item_price


msg = f'''
*******************************
Welcome to the Kabeer's Cool Electronics

        Final Bill 
        
Item: {item_name}
Quantity: {quantity}
Item Price: {item_price} USD
--------------------
Net Price: {net_price} USD
===================

Thank you for shopping at 
Tray Electronics. Come again
Soon!
******************************
'''

print(msg)




