import random
from item import Item
import file as f
from cmath import inf
import math
import timeit
import matplotlib.pyplot as plt 
from genetic_algorithm import Genetic
from hill_climbing_algorithm import Hill
from simmulated_annealing import Annealing

hill = Hill("Items/items_10.txt")
g = Genetic("Items/items_10.txt")
s = Annealing("Items/items_10.txt")

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
plt.ylabel("No. of students enrolled")
plt.title("")
plt.show()