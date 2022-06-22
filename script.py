import random

class Content():
    """A class modelling a content with random lines to be generated."""
    def __init__(self) -> None:
        """A constructor."""
        self.header = "item,weight,value\n"
        self.items = []
        self.indices = [i for i in range(1, 46)]
        random.shuffle(self.indices)
        self.weights = [str(self.indices[i]) + ',' for i in range(1, 45)]
        self.values = [str(random.randint(500, 1500)) + '\n' for _ in range(45)]
    
    def generateContent(self, fileName, itemNum):
        """A method for generating and writing content."""
        self.maxWeight = str(random.randint(10, 20) * itemNum) + '\n'
        content = [self.maxWeight, self.header]
        
        for idx in range(itemNum):
            content.append(self.items[idx])
            content.append(self.weights[idx])
            content.append(self.values[idx])

        f = open(fileName, "w+")
        f.writelines(content)
        f.close()

        # print(content) # debug line
        # print(self.indices)

    def main(self):
        """Main method of the class."""
        f = open("Items/random_items.txt")
        lines = f.readlines()
        for line in lines:
            self.items.append(line.rstrip() + ',')
        f.close()

        self.generateContent("Items/items_10.txt", 10)
        self.generateContent("Items/items_15.txt", 15)
        self.generateContent("Items/items_20.txt", 20)

if __name__ == "__main__":
    content = Content()
    content.main()
