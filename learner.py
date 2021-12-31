import sys
from grid import Grid

# Get Alpha Value from arguments
alphaValue = sys.argv[1]

# Case given in Assignment Instructions. Look at pseudocode.txt for quote
if alphaValue == 0:
    # TODO apply n(s,a) function to get value. Check pseudocode notes for purpose of function
    # alphaValue = 1 / n(s,a)
    alphaValue = 0

# Get Epsilon Value from arguments
epsilonValue = sys.argv[2]

# Create grid object
grid = Grid()

# Store agent's start location
startLocation = grid.generateStartState()

"""
Q - Learning Implementation
    -> Uses:
            -> Q-Learning Update Rule (Generates Q values)
            -> 𝜖-greedy exploration-exploitation algorithm (Action Selection Algorithm)
"""


def q_learning():
    return
