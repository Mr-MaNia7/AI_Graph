import script
import genetic_algorithm as genetic
import hill_climbing_algorithm as hill

class Knapsack():
    def __init__(self) -> None:
        content = script.Content()
        content.main()
    
    def geneticImp(self):
        gen = genetic.Genetic()
        gen.main()

    def hillClimbingImp(self):
        h = hill.Hill()
        h.main()

if __name__ == "__main__":
    k = Knapsack()

    k.geneticImp()
    # k.hillClimbingImp()
