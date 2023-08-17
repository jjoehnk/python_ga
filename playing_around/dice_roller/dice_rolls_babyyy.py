import random


#roll a dice w/ option of advantage or disadvantage: 

dice_num = int(input('What dice are we rolling?'))
adv_dis = input('Is this with advantage or disadvantage? (n/a/d)')
roll = random.randint(1, dice_num)
roll2 = random.randint(1, dice_num)
if adv_dis == 'n':
    result = roll
elif adv_dis == 'a':
    result = max(roll, roll2)
elif adv_dis == 'd':
    result = min(roll, roll2)
print(result)
print("dice rolled were: " + str(roll) + ", " + str(roll2))