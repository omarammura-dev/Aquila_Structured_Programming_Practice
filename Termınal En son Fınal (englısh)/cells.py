class Cell:
    def __init__(self, number):
        self.number = number
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal_name):
        self.animals = [a for a in self.animals if a.name != animal_name]
