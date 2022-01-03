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


# Initializing n dictionary for (State, Action): number of times gone to action

# BELOW IS COMMENTED OUT CODE FOR THE FOLLOWING EDITS I TRIED TO MAKE AND THEN GOT WORSE RESULTS:
# Picking based on reward to current action as opposed to two actions ahead
# Seperating action and epsilon greedy decisions into their own function
# Pulled q_table out of the q leaning function

# returns value found in n_dict for current state and action
def n(s, a):
    return


"""
    Implementation of 𝜖-greedy exploration-exploitation algorithm to help us find the best action choice for our current
    state

"""


def find_best_action(currstate, q_table):
    # Choose a random value between 0 and 1
    rval = random.random()
    # Compare with input epsilon value and see if we do exploration or exploitation
    # If random value is less epsilon value, perform exploration by choosing a random action
    if (rval < epsilonValue):
        # Randomly pick an action
        randomval = random.randint(0, 3)
        return [randomval, grid.actions[randomval]]

    # Perform exploitation by choosing the best action from q_table for the current state
    else:
        # Finds max value for action
        maxQ = max(q_table[currstate])
        # Identifies index to return action's string value
        maxDecision = q_table[currstate].index(maxQ)
        return [maxDecision, grid.actions[maxDecision]]


def q_learning(q_table, n_dict):
    # Initializing currentState to startState value
    # currentState = startState
    # Initializing Q_table with action list: given knowledge that there are 4 possible action choices
    # Indexes are associated with the following ['up', 'down', 'left', 'right']
    # Repeat until done acting in the world

    highestUtility = -100000

    for i in range(100):
        # Initializing currentState to startState location and our total utility for current episode
        currentState = startState
        totalUtil = 0
        # Loop to keep us exploring until our currentState is equal to the Goal State. Indicating that we are done
        # exploring for this episode
        while currentState != grid.ABSORBING_STATE:
            # Checks if currentState exists in Q_table. If not, adds it with default values. Allows us to use prior
            # values for learning through each episode
            if currentState not in q_table.keys():
                q_table[currentState] = [0.0, 0.0, 0.0, 0.0]

            # Determine what is our best action choice for our currentState using information in q_table
            action_list = find_best_action(currentState, q_table)
            # Stores String representation of action
            action = action_list[1]
            # Stores unique identifier of action
            actionnum = action_list[0]
            reward = grid.generateReward(currentState, action)
            totalUtil += reward
            nextState = grid.generateNextState(currentState, action)
            if nextState not in q_table.keys():
                q_table[nextState] = [0.0, 0.0, 0.0, 0.0]
            randomval2 = random.randint(0, 3)
            maxaction = grid.generateReward(nextState, grid.actions[randomval2])
            selactionnum = randomval2
            for x in range(0, 4):
                if grid.generateReward(nextState, grid.actions[x]) > maxaction:
                    maxaction = grid.generateReward(nextState, grid.actions[x])
                    selactionnum = x
            q_table[currentState][actionnum] = (1 - alphaValue) * q_table[currentState][actionnum] + alphaValue * (
                        reward + 0.99 * max(q_table[nextState]))
            currentState = nextState
        print(totalUtil)
        if totalUtil > highestUtility:
            highestUtility = totalUtil


# Initialize Q Table including startState with default values
q_table = {startState: [0.0, 0.0, 0.0, 0.0]}

# Initialize N dictionary to keep track of the number of times the agents chosen action 'a' in state 's'
# Key: [state, action] Value: # of times state chosen action
n_dict = {}

# Run Program
q_learning(q_table)

# BELOW IS THE ORIGINAL CODE WHICH DOESN'T WORK BUT GIVES FAR BETTER RESULTS
""" def q_learning():
    # Initializing currentState to startState value
    currentState = startState
    # Initializing Q_table with action list: given knowledge that there are 4 possible action choices
    # Indexes are associated with the following ['up', 'down', 'left', 'right']

    q_table = {currentState: [0.0, 0.0, 0.0, 0.0]}
    # Repeat until done acting in the world

    highestUtility = -100000

    for i in range(100):
        currentState = startState
        totalUtil = 0
        while currentState != grid.ABSORBING_STATE:
            # Initialize the Q(s, a) values for known state/action pairs
            if currentState not in q_table.keys():
                q_table[currentState] = [0.0, 0.0, 0.0, 0.0]
            # Note: Since we use the generateNextState to get our next state, we can check if the state we are looking at
            # exists in our table
            # if is in q_table.keys() update values

            # Generate Q values for currentState
            rval = random.random()
            if(rval < epsilonValue):
                # Randomly pick an action
                randomval = random.randint(0,3)
                nextState = grid.generateNextState(currentState, grid.actions[randomval])
                if nextState not in q_table.keys():
                    q_table[nextState] = [0.0, 0.0, 0.0, 0.0]
                curraction = grid.generateReward(currentState, grid.actions[randomval])
                randomval2 = random.randint(0,3)
                maxaction = grid.generateReward(nextState, grid.actions[randomval2])
                selactionnum = randomval2
                for x in range(0,4):
                    if(grid.generateReward(nextState, grid.actions[x]) > maxaction):
                        maxaction = grid.generateReward(nextState, grid.actions[x])
                        selactionnum = x
                q_table[currentState][randomval] = (1 - alphaValue) * q_table[currentState][randomval] + alphaValue * (grid.generateReward(currentState, grid.actions[randomval]) + 0.99 * q_table[nextState][selactionnum])
                currentState = nextState
                totalUtil += curraction
            else:
                for counter in range(len(grid.actions)):
                    # Use Q-learning updating rule to generate Q values for possible actions
                    # Generating random value between 0 and 1
                    #print(grid.actions[counter])
                    nextState = grid.generateNextState(currentState, grid.actions[counter])
                    if nextState not in q_table.keys():
                        q_table[nextState] = [0.0, 0.0, 0.0, 0.0]
                    # If we generated a number less than our epsilon value
                    # Otherwise pick the action that has the max value
                    maxaction = grid.generateReward(nextState, grid.actions[0])
                    selactionnum = 0
                    for x in range(1,4):
                        if(grid.generateReward(nextState, grid.actions[x]) > maxaction):
                            maxaction = grid.generateReward(nextState, grid.actions[x])
                            selactionnum = x
                    curraction = maxaction
                    selaction = grid.actions[selactionnum]
                    q_table[currentState][counter] = (1 - alphaValue) * q_table[currentState][counter] + alphaValue * (grid.generateReward(currentState, grid.actions[counter] ) + (0.99 * q_table[nextState][selactionnum]))
                maxQ = max(q_table[currentState])
                maxDecision = q_table[currentState].index(maxQ)
                currutil = grid.generateReward(currentState, grid.actions[maxDecision])
                currentState = grid.generateNextState(currentState, grid.actions[maxDecision])
                totalUtil += currutil
        #print(totalUtil)
        if(totalUtil > highestUtility):
            highestUtility = totalUtil
    print(highestUtility)
q_learning() """
