from unicodedata import name


class Item():
    def __init__(self, name, weight, value) -> None:
        self.name = name
        self.weight = weight
        self.value = value