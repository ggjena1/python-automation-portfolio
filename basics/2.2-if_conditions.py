'''

Get the bill value from the user. If it is higher than 1000 USD, offer a 10% discount. 
Check if the user is a member and if so apply another 10% discount.
Print the final bill value for the user
'''
final_bill = 0 
bill = int(input("Enter a bill value: "))

if bill > 1000:
    final_bill = bill - (bill * 0.1)

    membership=input("Are you a member? ('y' or 'n')")
    if membership =='y':
        additional_discount = final_bill - (final_bill * 0.1)
    else: 
        print(final_bill)
else:
    print('No Discount')


# HOMEWORK 
'''
------------------ NESTED IF LOOPS HOMEWORK ------------------------
Write a program that determines if a student is eligible for a school field trip based on their grade and parental consent. 
Use nested if statements with only one inner if loop.

The student must be in Grade 4, 5, or 6 to be eligible.
If the student is not in these grades, they are not eligible for the trip.
Parental Consent:

If the student is in an eligible grade, ask if they have parental consent.
If the answer is "yes", they can join the trip.
Otherwise, they cannot join the trip.

----------------------------------------------------------------
 Write a program that determines if a person is eligible for a library membership based on their age and residency status. 
 Use nested if statements and the or keyword.

Rules:
Age Requirements:

The person must be 12 years or older to be eligible.
If the person is younger than 12, they are not eligible for membership.
Residency Requirement:

If the person meets the age requirement, check if they are a resident of the town.
A person is considered a resident if they answer "yes" or "y".
If they are a resident, they are eligible for membership.
Otherwise, they are not eligible.

If the person is less than 12 years old, check if they are in kindergarten. 
If they are in kindergarten, print that they are eligible for art competion. 
Otherwise print that they can read books at the library. 

Hint: Start by collection below information 
age - int
is the user a resident- string
is the user in the kindergarten

Then apply the logic using nested if loops

Problem: Library problem
------------------------------------

A library categorizes books based on their genre and popularity. They use the following classification system:

If a book is of the "Fiction" genre:

If its popularity rating (out of 10) is 7 or above, classify it as "Popular Fiction."
Otherwise, classify it as "Regular Fiction."
If a book is of the "Non-Fiction" genre:

If its popularity rating (out of 10) is 7 or above, classify it as "Popular Non-Fiction."
Otherwise, classify it as "2
Regular NoI rescheduled to Thursday. Please feel free to reschedule again if the new time does not work.n-Fiction."


Problem: Restaurant Dish Classification
--------------------------------------------------------
A restaurant categorizes its dishes based on the type of cuisine and customer rating.
They use the following classification system:

    1. If a dish belongs to "Italian" cuisine:

        - If its rating (out of 10) is 8 or above, classify it as "Top Italian Dish".

        - Otherwise, classify it as "Regular Italian Dish".

    2. If a dish belongs to "Asian" cuisine:

        - If its rating (out of 10) is 8 or above, classify it as "Top Asian Dish".

        - Otherwise, classify it as "Regular Asian Dish".

Write a Python program that:

Asks the user to input the cuisine type and rating of a dish.

Prints the classification of the dish according to the rules above.

Problem: Movie Rating System

A streaming platform wants to classify movies based on their genre, viewer rating, and number of reviews.
The classification system works as follows:

1. If the movie is an "Action" movie:

   * If the rating is 8 or higher and there are more than 1000 reviews, classify it as "Blockbuster Action".
   * If the rating is 8 or higher but 1000 or fewer reviews, classify it as "Underrated Action".
   * Otherwise, classify it as "Regular Action".

2. If the movie is a "Drama" movie:

   * If the rating is 8 or higher and there are more than 500 reviews, classify it as "Critically Acclaimed Drama".
   * If the rating is below 8 but there are more than 1000 reviews, classify it as "Popular Drama".
   * Otherwise, classify it as "Regular Drama".

3. If the movie is a "Comedy" movie:

   * If the rating is 7 or higher, classify it as "Funny Hit".
   * Otherwise, classify it as "Average Comedy".

Write a Python program that:

* Asks the user to input:

  * The movie genre
  * The rating (out of 10)
  * The number of reviews
* Prints the classification according to the rules above.



##################### DIFFICULT PORBLLEMS - NO CLEAR INSTRUCTIONS ########################


1. A small grocery shop gives a warning message if a customer tries to enter a bill amount that is less than zero. Otherwise, it prints the bill amount. Design a program that behaves this way.

2. A cinema only allows entry to people aged 16 and above. If the person is younger, a message is shown saying they cannot enter. Create a program that decides what message to show based on age.

3. A food delivery app labels orders based on total cost. Orders below 500 are marked as "Low Value", and all others are marked as "High Value". Write a program that assigns this label.

4. A school assigns performance levels to students based on their score. Very low scores are labeled "Needs Improvement", mid-range scores are labeled "Satisfactory", and high scores are labeled "Excellent". Build a program that determines the correct label for a given score.

5. A bus service charges passengers differently based on age. Children travel for free, teenagers pay a reduced fare, and adults pay full fare. Write a program that determines which category a passenger belongs to.

6. An online store checks whether an order qualifies for a discount. If the order value is high enough, it then checks if the customer is a registered member to decide if an extra benefit is applied. Create a program that determines the final outcome.

7. A game awards players based on two factors: their level and their score. Players below a certain level are treated differently from advanced players. Among advanced players, only those with high scores receive special rewards, while others receive standard rewards. Write a program that determines what reward a player receives.
'''