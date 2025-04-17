import random
# Dice Simulator

def roll_dice(user):
    '''Dice Simulator By - DexterityCoder'''
    faces = [1, 2, 3, 4, 5, 6]
    choice = random.choice(faces)
    print(f"{user}: {choice}")

print(roll_dice.__doc__)
print(random.choice.__doc__)
roll_dice("User")