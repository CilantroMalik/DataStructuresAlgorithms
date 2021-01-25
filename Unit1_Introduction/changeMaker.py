"""
--- Change Maker ---
Calculates how to most efficiently give change in bills and coins for a given transaction.
Transaction amounts are randomly simulated between $1.00 and $100.00
"""

import random
import sys

# Ask for the user's first and last name separately.
first_name, last_name = input("Enter your first name: "), input("Enter your last name: ")

# Print a greeting.
print("Welcome to Embezzlement Bank Incorporated,", first_name, last_name)

# randomly generate the transaction amount (in cents)
amount_to_be_paid = int(100.00 + (random.random() * 9900.00))
print(f"Total to be paid: ${amount_to_be_paid / 100}")

# Ask for user's payment amount. This should be stored in a variable as dollars.
amount_given = float(input("Amount paid: $"))
amount_cents = 100 * amount_given  # also storing the amount as cents for convenience

# Calculate amount of change that should tendered.
# subtract the amount paid from the amount needed; if not enough was paid, set to -1 as a flag for the next line.
change = amount_cents - amount_to_be_paid if amount_cents >= amount_to_be_paid else -1
if change == -1:  # if the person did not pay enough, tell them and close the program.
    sys.exit("Pay up.")
print(f"Change: ${change / 100}")

# Calculate amount of every denomination that should be given
denominations = [2000, 1000, 500, 100, 25, 10, 5, 1]
num_bills = []
# loop through each denomination and append the maximum number of those that fits in the amount without going over
# then update the amount to reflect the bills removed and move on to the next denomination.
for denomination in denominations:
    num_bills.append(change // denomination)
    change %= denomination
num_bills = list(map(lambda x: int(x), num_bills))  # convert each element, which is currently a float, to an integer

# Print all information in a meaningful, readable manner.
print("----------------")
for i, denomination in enumerate(denominations):
    print(f"${denomination / 100}'s:".ljust(9), num_bills[i])  # left justify to make the amounts line up neatly
print("----------------")
print("Thank you for your business.")
