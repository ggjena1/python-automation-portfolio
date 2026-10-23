# Here is a simple function that calculates the total price of items in a shopping cart, applying a flat $5 discount if the total is over $50.

def calculate_total(prices):
    total = sum(prices)
    if total > 50:
        total -= 5
    return total





def test_test_calculate_total_with_discount():

    assert result == 5
