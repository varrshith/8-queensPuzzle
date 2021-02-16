from  random import shuffle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from State import State

initialState = [0, 0, 0, 0, 0, 0, 0, 0]

def hillClimbing(initialState):
    currentState = State(initialState)
    while True:
        bestNeighbor = currentState.neighbor()

        if bestNeighbor.evaluation() >= currentState.evaluation():
            return currentState.state
        currentState = bestNeighbor
    return currentState

def randomRestart(initialState):
    state = State(initialState)
    count = 0
    while State(initialState).evaluation() > 0 & count < 15:
        shuffle(initialState)
        state = hillClimbing(initialState)
        count += 1
    return state
	
# board graphic based on the solution
def board(solution): 
    matrix = np.zeros([8,8], dtype=int)
    matrix = matrix.tolist()
    for item in solution:
        for i in range(len(solution)):
            if i == item:
                for j in range(len(solution)):
                    if  j == solution.index(item):
                        matrix[i][j] = 1
                        
    l =[]
    for i in range(1, len(solution)+1):
        l.append(i)
    
    plt.figure(figsize=(5,5))
    sns.heatmap(matrix, linewidths=.8, cbar=False, cmap='Set3', xticklabels=l, yticklabels=l)
    
