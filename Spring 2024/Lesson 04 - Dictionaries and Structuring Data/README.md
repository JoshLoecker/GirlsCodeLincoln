# Dictionaries and Structuring Data

## Getting Started

### Poetry

This project uses [Poetry](https://python-poetry.org/) for dependency management. To install Poetry, run the following
command:

```shell
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

Once Poetry is installed, you can install the project dependencies by running the following command:

```shell
poetry install
```

## Lesson Summary

This lesson will introduce the concept of dictionaries in programming. Students will learn about the syntax for creating
dictionaries and how to use common dictionary methods, such as `keys()`, `values()`, and `items()`. Students will also
learn about the differences between lists and dictionaries and how to use a combination of the two for modeling
real-world objects. Finally, students will learn about the importance of data validation in programming and how to use
if statements to ensure that user inputs are valid

## Learning Objectives
- **Master the Dictionary Data Type:** Define the dictionary data type and its role in organizing and accessing data.
  Understand the concept of key-value pairs in dictionaries. Identify the various data types that can serve as keys in
  dictionaries.
- **Compare Lists and Dictionaries:** Contrast the differences between lists and dictionaries in terms of structure and
  functionality. Recognize the advantages of using dictionaries, particularly in mapping one item to another, compared
  to the sequential nature of lists.
- **Apply Dictionaries in Data Modeling:** Explore how dictionaries can be effectively combined with lists to create
  complex data structures. Develop the ability to model real-world objects using dictionaries, enhancing program
  representation.
- **Hands-On: Create a Tic-Tac-Toe Data Structure:** Apply knowledge of dictionaries and lists to create a data
  structure for modeling a tic-tac-toe board. Understand the advantages of using a combination of dictionaries and lists
  for organizing complex game-related data.

## Weekly Projects

### Weekly Project #1: Chess Dictionary Validator

In this chapter, we used the dictionary value `{'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': '
wking'}` to represent a chess board. Write a function named `isValidChessBoard()` that takes a dictionary argument and
returns `True` or `False` depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces,
at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. The
piece names begin with either a `'w'` or `'b'` to represent white or black, followed
by `'pawn'`, `'knight'`, `'bishop'`, `'rook'`, `'queen'`, or `'king'`. This function should detect when a bug has
resulted in an improper chess board.

### Weekly Project #2: Fantasy Game Inventory

You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the
keys are string values describing the item in the inventory and the value is an integer value detailing how many of that
item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow':
12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.

Write a function named `displayInventory()` that would take any possible “inventory” and display it like the following:

```
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
Total number of items: 62
```

Hint: You can use a `for` loop to loop through all the keys in a dictionary.

```python
# inventory.py

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for key, value in inventory.items():
        pass
        # FILL THIS PART IN (remove the pass line above statement)
    
    print("Total number of items: " + str(item_total))


displayInventory(stuff)
```

### List to Dictionary Function for Fantasy Game Inventory

Imagine that a vanquished dragon’s loot is represented as a list of strings like this:

`dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']`

Write a function named `addToInventory(inventory, addedItems)`, where the `inventory` parameter is a dictionary
representing the player’s inventory (like in the previous project) and the `addedItems` parameter is a list like
`dragonLoot`. The `addToInventory()` function should return a dictionary that represents the updated inventory. Note
that the `addedItems` list can contain multiples of the same item. Your code could look something like this:

```python
def addToInventory(inventory, addedItems):
    pass
    # your code goes here (remove the `pass` statement)


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
```

The previous program (with your displayInventory() function from the previous project) would output the following:

```
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48
```
