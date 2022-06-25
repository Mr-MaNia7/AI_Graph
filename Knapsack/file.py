class File():
    def __init__(self) -> None:
        self.maxWeight = 0
        self.items = []
        self.weights = []
        self.values = []
        self.maxChoice = 3
    
    def process(self, fname):
        f = open(fname)
        lines = f.readlines()
        for line in lines:
            if line.startswith('item,weight,value'):
                continue
            line = line.rstrip()
            if line.find(',') == -1:
                self.maxWeight = int(line)
                continue
            words = line.split(',')
            self.items.append(words[0])
            self.weights.append(int(words[1]))
            self.values.append(int(words[2]))

        return (self.maxWeight, self.items, self.weights, self.values)
    
    def displayResult(self):
        print()
        print("Maximum Weight Limit =>", self.maxWeight) 
        print("Items List =>", self.items)     
        print("Weights List =>", self.weights) 
        print("Values List =>", self.values)
        print()

if __name__ == "__main__":
    file = File()
    file.process("items_10.txt")
    file.displayResult()
