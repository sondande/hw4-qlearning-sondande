import sys
from grid import Grid
import random

# Get Alpha Value from arguments
alphaValue = float(sys.argv[1])

# Case given in Assignment Instructions. Look at pseudocode.txt for quote
if alphaValue == 0:
    # TODO apply n(s,a) function to get value. Check pseudocode notes for purpose of function
    # alphaValue = 1 / n(s,a)
    alphaValue = 0

# Get Epsilon Value from arguments
epsilonValue = float(sys.argv[2])

# Create Grid Object
grid = Grid()

# Store Agent's Start State
startState = grid.generateStartState()

# TODO think of possible data structure to keep track of how many times the s,a pair has been gone down. Dictionary with state as key and array as value? 2D arrays?
# n(s,a) dictionary initialized with key being state and value is an array of size 4 with counter of how many times the pair has been gone down

# n_dict = {}

"""
Q - Learning Implementation
    -> Uses:
            -> Q-Learning Update Rule (Generates Q values)
            -> 𝜖-greedy exploration-exploitation algorithm (Action Selection Algorithm)
    -> Q Table => has 4 possible actions 
    
"""

#print(startState)
# Personal notes: not adding all states into Q table allows us to only worry about states we go down and limit the
# search. We also reduce the error where we add the obstacle states or pits into our Q table

def q_learning():
    # Initializing currentState to startState value
    currentState = startState
    # Initializing Q_table with action list: given knowledge that there are 4 possible action choices
    # Indexes are associated with the following ['up', 'down', 'left', 'right']
    q_action_list = [0.0, 0.0, 0.0, 0.0]

    q_table = {currentState: q_action_list}
    # Repeat until done acting in the world

    highestUtility = -100000

    for i in range(100):
        currentState = startState
        numsteps = 0
        totalUtil = 0
        while currentState != grid.ABSORBING_STATE:
            numsteps+=1
            # Initialize the Q(s, a) values for known state/action pairs
            if currentState not in q_table.keys():
                q_table[currentState] = q_action_list
            # Note: Since we use the generateNextState to get our next state, we can check if the state we are looking at
            # exists in our table
            # if is in q_table.keys() update values

            # Generate Q values for currentState
            rval = random.random()
            if(rval < epsilonValue):
                # Randomly pick an action
                randomval = random.randint(0,3)
                nextState = grid.generateNextState(currentState, grid.actions[randomval])
                for x in range(1,4):
                    maxaction = grid.generateReward(nextState, grid.actions[0])
                    selactionnum = 0
                    if(grid.generateReward(nextState, grid.actions[x]) > maxaction):
                            maxaction = grid.generateReward(nextState, grid.actions[x])
                            selactionum = x
                futureaction = grid.generateReward(nextState, grid.actions[selactionnum])
                q_value = ((1 - alphaValue) * q_table[currentState][randomval]) + (alphaValue * (grid.generateReward(currentState, grid.actions[randomval]) + (0.99 * futureaction)))
                q_table[currentState][randomval] = q_value
                currentState = nextState
                totalUtil += curraction
            else:
                for counter in range(len(grid.actions)):
                    # Use Q-learning updating rule to generate Q values for possible actions
                    # Generating random value between 0 and 1
                    q_action_list[counter] = 0.0
                    #print(grid.actions[counter])
                    nextState = grid.generateNextState(currentState, grid.actions[counter])
                    if nextState not in q_table.keys():
                        q_table[nextState] = q_action_list
                    # If we generated a number less than our epsilon value
                    # Otherwise pick the action that has the max value
                    maxaction = grid.generateReward(nextState, grid.actions[0])
                    selactionnum = 0
                    for x in range(1,4):
                        #print(nextState)
                        #print(grid.actions[x], grid.generateReward(nextState, grid.actions[x]))
                        if(grid.generateReward(nextState, grid.actions[x]) > maxaction):
                            maxaction = grid.generateReward(nextState, grid.actions[x])
                            selactionum = x
                    curraction = maxaction
                    selaction = grid.actions[selactionnum]
                    q_value = ((1 - alphaValue) * q_table[currentState][selactionnum]) + (alphaValue * (grid.generateReward(currentState, selaction) + (0.99 * curraction)))
                    q_table[currentState][counter] = q_value
                maxQ = max(q_table[currentState])
                maxDecision = q_table[currentState].index(maxQ)
                currutil = grid.generateReward(currentState, grid.actions[maxDecision])
                currentState = grid.generateNextState(currentState, grid.actions[maxDecision])
                totalUtil += currutil
        print(totalUtil)
        if(totalUtil > highestUtility):
            highestUtility = totalUtil
    print(highestUtility)
    return q_table

q_learning()


