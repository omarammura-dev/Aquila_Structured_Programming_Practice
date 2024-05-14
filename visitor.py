class Visitor:
    def __init__(self, age, group_type):
        self.age = age
        self.group_type = group_type

    def observe_animals(self, animal):
        print(f"The visitor is observing the {animal.name}")

    def interact(self, animal):
        print(f"The visitor is interacting with the {animal.name}")