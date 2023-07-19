import random

my_roll = 4

if my_roll == 1 or my_roll == 3 or my_roll == 5:
    print("you have rolled a {}. You miss a turn".format(my_roll))
elif my_roll == 2 or my_roll == 4 or my_roll == 6:
    print("you have rolled a {}. You can take another turn.".format(my_roll))

print('exiting...')