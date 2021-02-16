import random

class State:
    def __init__(self, state):
        self.state = state

    def evaluation(self):
        h = 0
        temp = 0
        for i in self.state: 
            temp = self.state.count(i) 
            if temp > 1:
                h += 1
                
        for i in range(0, len(self.state)): 
            for j in range(0, len(self.state)):
                if j > i:
                    if abs(i - j) == abs(self.state[i] - self.state[j]):
                       h += 1
        return h
    
    def neighbor(self): 
        neighbors = {}
        for i in range(0, len(self.state)):
            for j in range(0, len(self.state)):
                if j != self.state[i]:
                    temp = self.state.copy()
                    temp[i] = j
                    temp = State(temp)
                    neighbors[(i, j)] = temp.evaluation() 

        bestNeighbors = []
        best_h = self.evaluation()         
        for i, h in neighbors.items()
            if h < best_h: 
                best_h = h
            if h == best_h:
                best_neighbors.append(i)

        if len(bestNeighbors) > 0: 
            random_index = random.randint(0, len(best_neighbors) - 1)
            self.state[best_neighbors[random_index][0]] = best_neighbors[random_index][1]
        return State(self.state) 
