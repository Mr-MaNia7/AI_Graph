import random
from item import Item
import file as f

class Hill():
    def __init__(self, fname) -> None:
        file = f.File()
        self.MAXWEIGHT, self.items, self.weights, self.values = file.process(fname)
        self.ITEMS = [Item(self.items[i], self.weights[i], self.values[i]) for i in range(len(self.items))]
        self.tempItems = []

    def generateList(self):
        self.tempItems = [item for item in self.ITEMS]
        # print(self.tempItems) #debug
        totweight = 0
        lst = []
        while totweight <= self.MAXWEIGHT:
            index = random.randint(0, len(self.tempItems)-1)
            p = self.tempItems.pop(index)
            totweight += p.weight
            lst.append(p)
        return lst

    def huristicValue(self, lst):
        totalValue = 0
        for item in lst:
            totalValue += item.value
        return totalValue

    def main(self):
        previous_list = self.generateList()
        previous_value = self.huristicValue(previous_list)
        # print(previous_list, previous_value) # debug
        for i in range(10):
            current_list = self.generateList()
            current_value = self.huristicValue(current_list)
            if previous_value < current_value:
                previous_list = current_list
                previous_value = current_value
            else:
                return previous_list, previous_value

if __name__ == "__main__":
    hill = Hill("Items/items_10.txt")
    print(hill.main())
