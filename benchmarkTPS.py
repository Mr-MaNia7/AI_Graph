import timeit

from matplotlib import pyplot as plt
from TSP.graph import Graph
from TSP.graphGtility import BuildGraph, Search
from TSP.tspUiluty import Heler, State
from TSP.genetic_algorithm import Generic
from TSP.hill_climbing_algoritn import HillClimping
from TSP.simulatedAnnealing import SimulatedAnnealing

graph = BuildGraph("romania20.txt").giveMeGraph()
helper = Heler()
generic = Generic()
hillClimping = HillClimping()
simulatedAnnealing = SimulatedAnnealing()



path1 = helper.generatPath(graph)
distance1 = helper.huristicValue(path1)
state1 = State(path1, distance1)

path2 = helper.generatPath(graph)
distance2 = helper.huristicValue(path2)
state2 = State(path2, distance2)

path3 = helper.generatPath(graph)
distance3 = helper.huristicValue(path3)
    
state3 = State(path3, distance3)

path4 = helper.generatPath(graph)
distance4 = helper.huristicValue(path4)
       
state4 = State(path4, distance4)

initialPopulation = [state1,state2,state3,state4]

bestState2 = generic.genetic(initialPopulation)
print(bestState2.distance)



path = helper.generatPath(graph)
distance = helper.huristicValue(path)
initialState = State(path,distance)
bestState = hillClimping.hillClimbing(initialState, graph)
print(bestState.distance)

path = helper.generatPath(graph)
distance = helper.huristicValue(path)
initialState = State(path,distance)
bestState3 = simulatedAnnealing.annealing(initialState, graph)
print(bestState3.distance)




annealing = timeit.timeit(stmt = str(bestState3.distance),number = 1)
hill_climbing = timeit.timeit(stmt = str(bestState.distance),number = 1)
genetic = timeit.timeit(stmt = str(bestState2.distance),number = 1)

search_mechanism = ["Hill climbing","Annealing","Genetic"]
average_time = [hill_climbing,annealing,genetic]

print(hill_climbing)
print(annealing)
print(genetic)



# creating the bar plot
plt.bar(search_mechanism,average_time, color ='maroon',
        width = 0.4)

plt.xlabel("")
plt.ylabel("Time Complexity")
plt.title("")
plt.show()