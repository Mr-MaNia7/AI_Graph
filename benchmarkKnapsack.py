import random
from Knapsack.item import Item
import Knapsack.file as f
from cmath import inf
import math
import timeit
import matplotlib.pyplot as plt 
from Knapsack.genetic_algorithm import Genetic
from Knapsack.hill_climbing_algorithm import Hill
from Knapsack.simmulated_annealing import Annealing

hill = Hill("items_20.txt")
g = Genetic("items_20.txt")
s = Annealing("items_20.txt")

annealing = timeit.timeit(stmt = s.main, number = 1)
hill_climbing = timeit.timeit(stmt = hill.main,number = 1)
genetic_algorithm = timeit.timeit(stmt = g.main,number = 1)
search_mechanism = ["hill climbing","Annealing","genetic algorithm"]
average_time = [hill_climbing,annealing,genetic_algorithm]

print(hill_climbing)
print(annealing)
print(genetic_algorithm)
# creating the bar plot
plt.bar(search_mechanism,average_time, color ='maroon',
        width = 0.4)

plt.xlabel("")
plt.ylabel("Time Complexity")
plt.title("")
plt.show()