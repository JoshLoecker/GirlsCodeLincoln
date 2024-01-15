import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    heads_tails_list = []
    for i in range(100):
        heads_tails_list.append(random.randint(0, 1))
    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 0
    for i in range(len(heads_tails_list) - 1):
        if heads_tails_list[i] == heads_tails_list[i + 1]:
            streak += 1
        else:
            streak = 0
        if streak == 6:
            numberOfStreaks += 1
            break
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
