from TSP.tspUiluty import Heler, State


class HillClimping:
    def __init__(self):
        self.helper = Heler()
    
    
    def hillClimbing(self,initialState, graph):
        current = initialState
        while True:
            path =self.helper.generatPath(graph)
            distance = self.helper.huristicValue(path)
            neighbor = State(path,distance)
            if neighbor.distance >= current.distance:
                return current
            if neighbor.distance < current.distance:
                current = neighbor
