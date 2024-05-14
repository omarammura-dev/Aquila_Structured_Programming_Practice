class Habitat:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.cages = []  

    def add_animal(self, animal):
        self.animals.append(animal)