"""
Write a program that asks users for their sandwich preferences.

The program should use PyInputPlus to ensure that they enter valid input, such as:
  - Using inputMenu() for a bread type: wheat, white, or sourdough.
  - Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
  - Using inputYesNo() to ask if they want cheese.
    - If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
  - Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
  - Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.

Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.
"""
import pyinputplus as pyip

# Sandwich prices
bread_prices = {'wheat': 1.00, 'white': 1.00, 'sourdough': 1.50}
protein_prices = {'chicken': 2.00, 'turkey': 2.00, 'ham': 2.00, 'tofu': 1.50}
cheese_prices = {'cheddar': 1.00, 'swiss': 1.00, 'mozzarella': 1.50}
extras_prices = {'mayo': 0.25, 'mustard': 0.25, 'lettuce': 0.25, 'tomato': 0.25}

# Ask user for sandwich preferences
bread = pyip.inputMenu(list(bread_prices.keys()), numbered=True)
protein = pyip.inputMenu(list(protein_prices.keys()), numbered=True)
cheese = pyip.inputYesNo(prompt='Would you like cheese? ')
if cheese == 'yes':
    cheese = pyip.inputMenu(list(cheese_prices.keys()), numbered=True)
else:
    cheese = None

extras = pyip.inputYesNo(prompt='Would you like mayo, mustard, lettuce, or tomato? ')
if extras == 'yes':
    extras = pyip.inputMenu(list(extras_prices.keys()), numbered=True)
else:
    extras = None

quantity = pyip.inputInt(prompt='How many sandwiches would you like? ', min=1)

# Calculate total cost
total = bread_prices[bread] + protein_prices[protein]
if cheese:
    total += cheese_prices[cheese]
if extras:
    total += extras_prices[extras]
total *= quantity
