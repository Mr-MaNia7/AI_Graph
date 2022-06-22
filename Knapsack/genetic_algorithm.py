import random
import file as f

class Population():
    def __init__(self, size, itemSize, withPermutation = True) -> None:
        self.size = size
        self.withPermutation = withPermutation
        self.population = [self.chromosome(itemSize) for _ in range(self.size)]
        self.PARENTELIGIBILITY = 0.3
        self.MUTATIONCHANCE = 0.1
        self.PARENTCHANCE = 0.07
    
    def chromosome(self, itemSize):
        if self.withPermutation:
            return [random.randint(0, 1) for _ in range(itemSize)]
        else:
            return [0 for _ in range(itemSize)]

    def mutate(self, chromosome):
        """Changes a random element of the permutation array from 0 -> 1 or from 1 -> 0.""" 
        rdm = random.randint(0, len(chromosome)-1)
        chromosome[rdm] = 1 - chromosome[rdm]

    def evolve(self):
        parentLength = int(self.PARENTELIGIBILITY * len(self.population))
        parents = self.population[:parentLength]
        nonparents = self.population[parentLength:]

        # Parents lottery
        for nonpt in nonparents:
            if self.PARENTCHANCE > random.random():
                parents.append(nonpt)

        # Mutation lottery
        for parent in parents:
            if self.MUTATIONCHANCE > random.random():
                self.mutate(parent)

        # Breeding
        children = []
        desiredLength = len(self.population) - len(parents)
        chosenChm = {}
        while len(children) < desiredLength:
            father = self.population[random.randint(0, len(parents)-1)]
            mother = self.population[random.randint(0, len(parents)-1)]

            half = int(len(father)/2)
            childChm = father[:half] + mother[half:] # take half from father and half from mother
            if self.MUTATIONCHANCE > random.random():
                self.mutate(childChm)
            children.append(childChm)
        parents.extend(children)
        
        return parents

class Genetic():
    def __init__(self, fname) -> None:
        file = f.File()
        self.MAXWEIGHT, self.items, self.weights, self.values = file.process(fname)
        self.POPULATIONSIZE = 10
        self.MAXGEN = 10 # maximum generation
  
    def fitness(self, chromosome):
        totValue = 0
        totWeight = 0
        for idx in chromosome:
            if idx == 1:
                totValue += self.values[idx]
                totWeight += self.weights[idx]
                    
        if totWeight > self.MAXWEIGHT:
            return 0
        else:
            return totValue

    def main(self):
        countGen = 1
        popObj = Population(self.POPULATIONSIZE, len(self.items), True)
        pop = popObj.population

        for _ in range(self.MAXGEN):
            print("Generation {} with {} population size.".format(countGen, self.POPULATIONSIZE))
            pop = sorted(pop, key = lambda x: self.fitness(x), reverse = True) # sort population based on fitness
            for chm in pop:
                print("{}, fit: {}".format(str(chm), self.fitness(chm)))
            pop = popObj.evolve()
            countGen += 1

if __name__ == "__main__":
    g = Genetic("Items/items_10.txt")
    g.main()
