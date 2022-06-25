from Knapsack.script import Content
import Knapsack.genetic_algorithm as genetic
import Knapsack.hill_climbing_algorithm as hill
import Knapsack.simmulated_annealing as ann
import argparse

class Knapsack():
    def __init__(self) -> None:
        content = Content()
        content.main()
    
    def geneticImp(self, filename):
        gen = genetic.Genetic(filename)
        gen.main()

    def hillClimbingImp(self, filename):
        h = hill.Hill(filename)
        h.main()
    
    def simmulatedAnnealingImp(self, filename):
        s = ann.Annealing(filename)
        s.main()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm')
    parser.add_argument('--file')
    args = parser.parse_args()

    k = Knapsack()
    if args.algorithm =="ga":
        k.geneticImp(args.file)
    if args.algorithm =="sa":
        k.simmulatedAnnealingImp(args.file)
    if args.algorithm =="hc":
        k.hillClimbingImp(args.file)

