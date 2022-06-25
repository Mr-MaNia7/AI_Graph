import argparse
import random
from TSP.graph import Graph
from TSP.graphGtility import BuildGraph, Search
from TSP.tspUiluty import Heler, State
from TSP.genetic_algorithm import Generic
from TSP.hill_climbing_algoritn import HillClimping
from TSP.simulatedAnnealing import SimulatedAnnealing
 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm')
    parser.add_argument('--file')
    args = parser.parse_args()
    graph = BuildGraph(args.file).giveMeGraph()
    helper = Heler()
    generic = Generic()
    hillClimping = HillClimping()
    simulatedAnnealing = SimulatedAnnealing()

     # generic
    if args.algorithm == "ga":
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
        print([str(node) for node in bestState2.path], bestState2.distance, sep = "\n")


    #hill climping    
    if args.algorithm == "hc":
        path = helper.generatPath(graph)
        distance = helper.huristicValue(path)
        initialState = State(path,distance)
        bestState = hillClimping.hillClimbing(initialState, graph)
        print([str(node) for node in bestState.path], bestState.distance, sep = "\n")

 


    # analog
    if args.algorithm == "sa":
        path = helper.generatPath(graph)
        distance = helper.huristicValue(path)
        initialState = State(path,distance)
        bestState3 = simulatedAnnealing.annealing(initialState, graph)
        print([str(node) for node in bestState3.path], bestState3.distance, sep = "\n")
   
main()  

        