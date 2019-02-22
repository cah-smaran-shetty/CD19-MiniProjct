class Variable:
    name = ""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        hash = 0
        for i in self.name:
            hash += ord(i)
        return hash
