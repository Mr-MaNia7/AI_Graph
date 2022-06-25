import random
from TSP.graph import Graph
from TSP.graphGtility import BuildGraph, Search


class Heler:
    def __init__(self):
        pass

    def generatPath(self,graph):
        path = []
        nodes = graph.nodes()
        while len(nodes)>0:
            index = random.randint(0,len(nodes)-1)
            node = nodes[index]
            path.append(node)
            nodes.remove(node)
        return path

    
    def huristicValue(self,path):
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

    
    def fitnessValue(self,path):
        search = Search()
        graph = Graph()
        distance = 0
        punishement = 5
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


class State:
    def __init__(self, path, distance):
        self.path= path
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance
    

