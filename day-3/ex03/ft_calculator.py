

class calculator:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, scalar):
        result = [x + scalar for x in self.vector]
        print(result)
        return [x for x in self.vector]

    def __mul__(self, scalar):
        result = [x * scalar for x in self.vector]
        print(result)
        return [x for x in self.vector]

    def __sub__(self, scalar):
        result = [x - scalar for x in self.vector]
        print(result)
        return [x for x in self.vector]

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Can t divide by zero")
        result = [x / scalar for x in self.vector]
        print(result)
        return [x for x in self.vector]

    def __str__(self):
        return str(self.vector)
