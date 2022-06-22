from importlib.resources import path
import random
from graph import Graph
from utility import BuildGraph, Search


class State:
    def __init__(self, path, distance):
        self.path= path
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance
    

    def update(self, path, distance):
        self.path= path
        self.distance = distance

        
def generatPath(graph = BuildGraph('romania.txt').giveMeGraph()):
    path = []
    nodes = graph.nodes()
    while len(nodes)>0:
        index = random.randint(0,len(nodes)-1)
        node = nodes[index]
        path.append(node)
        nodes.remove(node)
    return path

# hill climping algorthem
def huristicValue(path):
    search = Search()
    distance = 0
    for i in range(len(path)):
        firest = path[i]
        if i+1 < len(path):
            second = path[i+1]
        else:
            second = path[0]
        distance = distance +search.dijkstra_search(firest, second)
    return distance


def hillClimbing(initialState):
    current = initialState
    while True:
        path =generatPath()
        distance = huristicValue(path)
        neighbor = State(path,distance)
        if neighbor.distance >= current.distance:
            return current
        if neighbor.distance < current.distance:
            current = neighbor


# generic algorthem

def genetic(initialStates):
    population = initialStates
    limit = 0
    while True:
        # population = crossOver(population)
        population.sort()
        for state in population:
            mutatedState = mutate(state)

            if population[-1] < mutatedState:
                population[-1] = mutatedState
        if limit >20:
            population.sort()
            return population[0]
        limit = limit+1


def fitnessValue(path):
    search = Search()
    graph = Graph()
    distance = 0
    punishement = 0
    for i in range(len(path)):
        firest = path[i]
        if i+1 < len(path):
            second = path[i+1]
        else:
            second = path[0]

        edge = graph.get_edge(firest, second)  
        if edge == None:
             distance = distance + punishement
        distance = distance +search.dijkstra_search(firest, second)

    return distance



def mutate(state):
        path = state.path
        index1 = random.randint(0,len(path)-1)
        index2 = random.randint(0,len(path)-1)
        index3 = random.randint(0,len(path)-1)
        node1 =path[index1]
        node2 =path[index2]
        node3 =path[index3]
        path[index1] = node2
        path[index2] = node3
        path[index3] = node1
        distance = fitnessValue(path)
        state.update(path, distance)

        return state

# helper function for crossover
def arrange(state1,state2):
    for node in state2.path:
        if node not in state1.path:
            state1.path.append(node)
    return state1


def crossOver(inPopulation):
    state1 = inPopulation[0]
    state2 = inPopulation[1]
    state3 = inPopulation[2]
    state4 = inPopulation[3]

    index1 = random.randint(0,len(state1.path)-1)

    path1 = state1.path
    path2 = state2.path
    path3 = state3.path
    path4 = state4.path

    for state in inPopulation:
        state.path = []

    state1.path.extend(path1[:index1])
    state1 = arrange(state1, state2)

    state2.path.extend(path2[:index1])
    state2 = arrange(state2, state1)

    state3.path.extend(path3[:index1])
    state3 = arrange(state3, state4)

    state4.path.extend(path4[:index1])
    state4 = arrange(state4, state3)

    outPopulation = [state1, state2,state3,state4]

    return outPopulation
 


def schedule(t):
    if t ==100:
        return 0
    return t*100
    

def annealing(initialState):
        current = initialState
        t =0
        while True:
            T = schedule(t)
            if T ==0:
                return current

            path =generatPath()
            distance = huristicValue(path)
            next = State(path,distance)

            changeInEnerge = next.distance - current.distance

            if changeInEnerge < 0:
                current =next
            elif changeInEnerge/T > random.randint(0,1):
                current =next
            t = t+1 


def main():
    graph = BuildGraph('romania.txt').giveMeGraph()
    path =generatPath(graph)
    distance = huristicValue(path)
    initialState = State(path,distance)
    bestState = hillClimbing(initialState)
    print(bestState.distance)

    # generic

    path1 =generatPath(graph)
    distance1 = huristicValue(path1)
    state1 = State(path1, distance1)

    path2 =generatPath(graph)
    distance2 = huristicValue(path2)
    state2 = State(path2, distance2)

    path3 =generatPath(graph)
    distance3 = huristicValue(path3)
    state3 = State(path3, distance3)

    path4 =generatPath(graph)
    distance4 = huristicValue(path4)
    state4 = State(path4, distance4)

    initialState = [state1,state2,state3,state4]

    bestState2 = genetic(initialState)
    print(bestState2.distance)


    # analog

    path =generatPath(graph)
    distance = huristicValue(path)
    initialState = State(path,distance)
    bestState3 = annealing(initialState)
    print(bestState.distance)






   
main()  









        