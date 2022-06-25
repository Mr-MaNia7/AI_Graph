

import random
from TSP.tspUiluty import Heler, State


class SimulatedAnnealing:
    def __init__(self):
        self.helper = Heler()

    def _schedule(self,t):
        if t ==100:
            return 0
        return t*100
        


    def annealing(self,initialState, graph):
            current = initialState
            t =0
            while True:
                T = self._schedule(t)
                if T ==0:
                    return current

                path = self._generatPath(graph)
                distance = self._huristicValue(path)
                next = State(path,distance)

                changeInEnerge = next.distance - current.distance

                if changeInEnerge < 0:
                    current =next
                elif changeInEnerge/T > random.randint(0,1):
                    current =next
                t = t+1 