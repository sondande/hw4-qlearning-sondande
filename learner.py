import sys
import matplotlib.pyplot as plt
import numpy as np
from grid import Grid
import random

# Get Alpha Value from arguments
alphaValue = float(sys.argv[1])

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

"""
    Creating an array from data collected in q_learning
    Optional use to get line chart of values
"""


def readFile(filename):
    # opens the file in read mode
    file = open(filename, "r")
    # puts the file into an array
    y_values = file.read().splitlines()
    file.close()
    return y_values


"""
Saving Information from Q-Learning to a File 
"""


def reward_save(filename, total_utility):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(filename, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(total_utility)


"""
    Implementation of 𝜖-greedy exploration-exploitation algorithm to find the best action for current state
"""


def find_best_action(currstate, q_table):
    # Choose a random value between 0 and 1
    rval = random.random()
    # Compare with input epsilon value and see if we do exploration or exploitation
    # If random value is less epsilon value, perform exploration by choosing a random action
    if rval < epsilonValue:
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


"""
    Implementation of Q-learning Algorithm
    Takes in established Q values in Q_table and n_dict that holds the amount of times a current state chose an action
    Utilizes:
        Alpha Value (learning rate 𝛼 in the Q-Learning update rule)
        Epsilon Value (exploration rate 𝜖 in the 𝜖-greedy exploration-exploitation algorithm)
    Finds the highest utility from all episodes of the world done, Q values, and overall times
    Stores information in policy file for further use
"""


def q_learning(q_table, n_dict):
    # Initializing Q_table with action list: given knowledge that there are 4 possible action choices
    # Indexes are associated with the following ['up', 'down', 'left', 'right']

    highestUtility = -100000

    for i in range(100):
        # Initializing currentState to startState location and our total utility for current episode
        currentState = startState

        totalUtil = 0
        # Loop to keep us exploring until our currentState is equal to the Goal State. Indicating that we are done
        # Exploring for this episode and repeats until done acting in the world
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
            # Store the reward for our current state and the current chosen action
            reward = grid.generateReward(currentState, action)
            # Add to our total utility
            totalUtil += reward
            Value = n_dict.keys()
            # Add chosen state count to n_dict to keep track of progress
            if (currentState, action) in n_dict.keys():
                n_dict[(currentState, action)] += 1
            else:
                n_dict[(currentState, action)] = 1
            # Generate a random next state after we take an action for our current state
            nextState = grid.generateNextState(currentState, action)
            # Check to see if nextState is a place we've explored. If not, set default values
            if nextState not in q_table.keys():
                q_table[nextState] = [0.0, 0.0, 0.0, 0.0]
            # Choose a random action from action list
            randomval2 = random.randint(0, 3)
            # Set the reward for action chosen by random as the max action
            maxaction = grid.generateReward(nextState, grid.actions[randomval2])
            # Go through all rewards for each action chose for the nextState and store the largest reward and action
            selactionnum = randomval2
            for x in range(0, 4):
                if grid.generateReward(nextState, grid.actions[x]) > maxaction:
                    maxaction = grid.generateReward(nextState, grid.actions[x])
                    selactionnum = x

            # Checks if user input for alpha value is 0. If so, we calculate the alpha value, if not, use input value
            if alphaValue == 0:
                alpha_value = 1 / n_dict[(currentState, action)]
            else:
                alpha_value = alphaValue
            # Use Q-Learning Update Rule to find overall Q value for current state and action stored in Q Table
            q_table[currentState][actionnum] = (1 - alpha_value) * q_table[currentState][actionnum] + alpha_value * (
                    reward + 0.99 * max(q_table[nextState]))
            # Set next current State
            currentState = nextState

        print(totalUtil)
        reward_save("q_learning_data_5.txt", str(totalUtil))
        # Stores the highest utility our of all episodes
        if totalUtil > highestUtility:
            highestUtility = totalUtil
    print("highest", highestUtility)


# Initialize Q Table including startState with default values
q_table = {startState: [0.0, 0.0, 0.0, 0.0]}

# Initialize N dictionary to keep track of the number of times the agents chosen action 'a' in state 's'
# Key: [state, action] Value: # of times state chosen action
n_dict = {}

# Clearing file before running program
# with open("q_learning_data.txt", 'r+') as f:
#     f.truncate(0)

# Run Program
q_learning(q_table, n_dict)

# # Plotting Graph Section
# plt.title("Experiment #1: Changing Alpha")
#
# # Storing data in arrays
# x = list(range(100))
# y = list(readFile("q_learning_data.txt"))
#
# # Using Matplotlib to plot data in line 1 0.9
# plt.plot(x, y, label="a = 0.9")
#
# # Storing data in arrays
# x = list(range(100))
# y = list(readFile("q_learning_data_2.txt"))
#
# # Using Matplotlib to plot data in line 2 0.65
# plt.plot(x, y, label="a = 0.65")
#
# # Storing data in arrays
# x = list(range(100))
# y = list(readFile("q_learning_data_3.txt"))
#
# # Using Matplotlib to plot data in line 3
# plt.plot(x, y, label="a =0.5")
#
# # Storing data in arrays
# x = list(range(100))
# y = list(readFile("q_learning_data_4.txt"))
#
# # Using Matplotlib to plot data in line 4
# plt.plot(x, y, label="a = 0.25")
#
# # Storing data in arrays
# x = list(range(100))
# y = list(readFile("q_learning_data_5.txt"))
#
# # Using Matplotlib to plot data in line 5
# plt.plot(x, y, label="a = 0")
# plt.legend()
# plt.show()

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
