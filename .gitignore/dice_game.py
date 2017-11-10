from __future__ import division
from random import *
from numpy import random
from collections import Counter

prob = [0.5, 0.5]
n = 100000
points = {"a": 0, "b": 0}

def dice(probabilities, number_choices):
    num_faces = len(probabilities)
    normalized_prob = [x/sum(probabilities) for x in probabilities]
    faces = [x for x in range(1,num_faces+1)]
    return random.choice(faces, number_choices, p = normalized_prob)

def roll_dice(n):
    for i in range(n):
        element = dice(prob, 4)
        if element[0] == element[1] and element[2] == element[3]:
            points["a"] += 1
        if element[0] == element[1] and element[0] == element[2]:
            points["b"] += 1
        prob_a = points["a"]/n
        prob_b = points["b"]/n
    return points, prob_a, prob_b

print(Counter(dice(prob, n)))
print(roll_dice(n))
