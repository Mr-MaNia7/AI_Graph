import script
import genetic_algorithm as genetic

class Knapsack():
    def __init__(self) -> None:
        content = script.Content()
        content.main()
    
    def geneticImpl(self):
        gen = genetic.Genetic()
        gen.main()

if __name__ == "__main__":
    k = Knapsack()
    k.geneticImpl()
