'''

Problem 5: The Email Filter ✉️


Your Goal

Create a list containing 6 email addresses (some ending in @gmail.com and some ending in @yahoo.com). Create a separate blank list called gmail_only. Use a loop to scan the original list, and copy only the Gmail addresses into your new list. Finally, print the gmail_only list.

Your Hints 💡

• The Text Scanner: Python strings have a built-in superpower tool called .endswith(). You can use it inside an if statement to check how text ends: if email.endswith('@gmail.com'):.
• The Copy Machine: Remember your warm-up challenge from earlier? To copy a matched item into your blank list, use the .append() method inside your if block: gmail_only.append(email).
Give this final challenge a shot and paste your code structure below!
Show me your email filtering script, or let me know if you want a template layout showing how to use .endswith()!
'''


'''
Problem 1: The Score Upgrader (Modifying Items)
Create a list containing 5 golf scores (numbers).
The player gets a handicap bonus, so you need to use square brackets [] and index positions to change the 2nd and 4th scores in the list to be 5 points lower. Print the final list.
• Muscle Memory Target: Working with zero-based index positions (list_name[1] = ...).
'''
golf_scores=[23,22,21,33,37]
golf_scores[1]-=5
golf_scores[3]-=5
print(golf_scores)


'''    
• Problem 2: The Security Guard (Removing Items)
Create a list of 5 guest names. A guest named "Jack" leaves the party. Use a built-in list tool to find and delete "Jack" from the list by his exact name string, then print the updated list.
• Muscle Memory Target: Using the .remove() value tool.
'''


'''
    
    
    • Problem 3: The Temperature Extremes (List Metrics)
Create a list of 7 daily temperatures. Without writing a loop or any if statements, use Python's built-in mathematical list functions to find and print the highest temperature, the lowest temperature, and the total number of days recorded.
	• Muscle Memory Target: Using max(), min(), and len().

    '''


'''

    • Problem 4: The Inventory Scanner (Looping over Lists)
Create a list of 5 grocery items. Use a single basic for loop to look at each item individually and print them out in a clean sentence like: "Item on shelf: milk".
	• Muscle Memory Target: Standard item iteration (for item in groceries:).
'''