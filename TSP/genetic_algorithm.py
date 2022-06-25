import random
from TSP.tspUiluty import Heler



class Generic:
    def __init__(self):
        self.helper = Heler()


    def genetic(self,initialStates):
        population = initialStates
        limit = 0
        while True:
            population.sort()
            for states in population:
                mutatedState = self._mutate(states)

                if population[-1] < mutatedState:
                    population[-1] = mutatedState
            if limit >20:
                population.sort()
                return population[0]
            limit = limit+1



    def _mutate(self,state):
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
            distance = self.helper.fitnessValue(path)
            state.path = path
            state.distance = distance

           

            return state


    # helper function for crossover
    def _arrange(self,state1,path):
        for i in range(len(state1.path), len(path)):
            node = path[i]
            if node not in state1.path:
                state1.path.append(node)
        return state1



    def _crossOver(self,inPopulation):
        state1 = inPopulation[0]
        state2 = inPopulation[1]
        state3 = inPopulation[2]
        state4 = inPopulation[3]

        # index1 = random.randint(0,len(state1.path)-1)
        index1 = 10

        path1 = state1.path.copy()
        path2 = state2.path.copy()
        path3 = state3.path.copy()
        path4 = state4.path.copy()

        for state in inPopulation:
            # print(len(state.path))
            state.path = []
        
        state1.path = []
        state1.path.extend(path1[0:index1])
        state1 =self._arrange(state1, path2)

        state2.path = []
        state2.path.extend(path2[:index1])
        state2 = self._arrange(state2, path1)

        state3.path = []
        state3.path.extend(path3[:index1])
        state3 = self._arrange(state3, path4)

        state4.path = []
        state4.path.extend(path4[:index1])
        state4 = self._arrange(state4, path3)

        outPopulation = [state1, state2,state3,state4]
        for state in outPopulation:
            print(len(state.path))

        return inPopulation