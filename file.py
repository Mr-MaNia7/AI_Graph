class File():
    def __init__(self, fname) -> None:
        self.maxWeight = 0
        self.items = []
        self.weights = []
        self.values = []
        self.maxChoice = 3
        self.process(fname)
    
    def process(self, fname):
        f = open(fname)
        lines = f.readlines()
        for line in lines:
            if line.startswith('item,weight,value'):
                continue
            line = line.rstrip()
            if line.find(',') == -1:
                self.maxWeight = line
                continue
            words = line.split(',')
            self.items.append(words[0])
            self.weights.append(words[1])
            self.values.append(words[2])
    
    def displayResult(self):
        print(self.maxWeight, self.items, self.weights, self.values, sep = "\n")


class Driver():
    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    file = File("items_10.txt")
    file.displayResult()
