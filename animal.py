class Animal:
    prey = []

    def __init__(self):
        self.name = 'I don\'t have a name dude!'     

    def __repr__(self):
        """ 
        """
        species = self.__class__.__name__
        return self.name + " " + species if self.name != 'I don\'t have a name dude!' else species
