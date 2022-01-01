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

print(startState)

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
    while currentState == grid.ABSORBING_STATE:
        # Initialize the Q(s, a) values for known state/action pairs
        if currentState not in q_table.keys():
            q_table[currentState] = q_action_list
        # Note: Since we use the generateNextState to get our next state, we can check if the state we are looking at
        # exists in our table
        # if is in q_table.keys() update values

        # Generate Q values for currentState
        for counter in range(len(grid.actions)):
            # Use Q-learning updating rule to generate Q values for possible actions

            # Generating random value between 0 and 1
            rval = random.random()
            
            # If we generated a number less than our epsilon value
            if(rval < epsilonValue):
                # Randomly pick an action
                randomval = random.randint(0,3)
                selaction = q_action_list[randomval]
                curraction = grid.generateNextState(currentState, grid.actions[randomval])
                q_value = (1 - alphaValue) * q_table[currentState][counter] + (alphaValue * (grid.generateReward(currentState, grid.actions[counter] + (0.99 * curraction))))
            else:
                # Otherwise pick the action that has the max value
                maxaction = grid.generateNextState(currentState, grid.actions[0]
                selactionnum = 0
                for x in range(1,4):
                    if(grid.generateNextState(currentState, grid.actions[x]) > maxaction):
                        maxaction = grid.generateNextState(currentState, grid.actions[x])
                        selactionum = x
                curraction = maxaction
                selaction = q_action_list[selactionnum]
                q_value = (1 - alphaValue) * q_table[currentState][counter] + (alphaValue * (grid.generateReward(currentState, grid.actions[counter] + (0.99 * curraction))))
                
        print(selaction)


    return ""



