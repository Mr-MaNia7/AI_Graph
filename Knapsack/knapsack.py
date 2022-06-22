import script
import genetic_algorithm as genetic
import hill_climbing_algorithm as hill
import simmulated_annealing as ann

class Knapsack():
    def __init__(self) -> None:
        content = script.Content()
        content.main()
    
    def geneticImp(self):
        gen = genetic.Genetic("Items/items_10.txt")
        gen.main()

    def hillClimbingImp(self):
        h = hill.Hill("Items/items_10.txt")
        h.main()
    
    def simmulatedAnnealingImp(self):
        s = ann.Annealing("Items/")
        s.main()

if __name__ == "__main__":
    k = Knapsack()

    k.geneticImp()
    # k.hillClimbingImp()
