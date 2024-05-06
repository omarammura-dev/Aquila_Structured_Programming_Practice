class Visitor:
    def __init__(self, age, group_type):
        self.age = age
        self.group_type = group_type

    def observe_animals(self):
        pass

    def interact(self):
        pass