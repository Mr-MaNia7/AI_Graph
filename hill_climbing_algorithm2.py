import file as f
import script

class Bag():
    def __init__(self, limit, items, weights, values) -> None:
        self.items, self.weights, self.values = items, weights, values
        self.weight = 0
        self.limit = limit
        
        self.knapsack = {}
        self.repeatedItem = []
        self.heu = {}
        self.hueList = []
        self.wvList = []

        self.main()

    def fillBag(self, weight, value, res):
        self.knapsack[(weight, value)] = res
        self.weight += weight
    
    def heuristic(self, item, weight, value):
        res = value / weight
        self.wvList.append((weight, value))
        self.hueList.append(res)
        self.hueList.sort(reverse = True)

        self.heu = dict(zip(self.wvList, self.hueList))
        # print(self.heu)

    def removeItem(self):
        # is repeated
        # weight --
        pass

    def main(self):
        for idx in range(len(self.items)):
            i, w, v = self.items[idx], self.weights[idx], self.values[idx]
            self.heuristic(i, w, v)
        
        for wv, res in list(self.heu.items()):
            w, v = wv[0], wv[1]
            if w + self.weight <= self.limit:
                self.fillBag(w, v, res)


if __name__ == "__main__":
    content = script.Content()
    content.main()
    file = f.File()
    MAXWEIGHT, items, weights, values = file.process("Items/items_10.txt")
    bag = Bag(MAXWEIGHT, items, weights, values)
    print(
    "Items in the bag: {}".format(bag.knapsack), 
    "Number of items in a bag: {}".format(len(bag.knapsack)), 
    "Weight of the bag: {}".format(bag.weight),
    "Maximum Weight: {}".format(bag.limit),
    sep = "\n")