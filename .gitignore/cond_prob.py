from random import *
from numpy import random
from collections import Counter

prob = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
n = 100000

def dice(probabilities, number_choices):
    num_faces = len(probabilities)
    normalized_prob = [x/sum(probabilities) for x in probabilities]
    faces = [x for x in range(1,num_faces+1)]
    return random.choice(faces, number_choices, p = normalized_prob)

def roll_dice_cond(n):
    x_equal_z = 0
    x_equal_z_cond = 0
    total = 0
    for i in range(n):
        element = dice(prob, 3)
        if element[0] == element[2]:
            x_equal_z += 1
        if element[0] != element[1]:
            total += 1
            if element[0] == element[2]:
                x_equal_z_cond += 1
    dist = [x_equal_z/n, x_equal_z_cond/total if total else 0]
    return dist

print(Counter(dice(prob, n)))
print(roll_dice_cond(n))
