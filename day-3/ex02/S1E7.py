from S1E9 import Character


class Baratheon(Character):
    """ Baratheon Family Character"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def say_house_words(self):
        print("Ours is the Fury")


class Lannister(Character):

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def count_gold(self):
        print(f"{self.first_name} has a wealth level of Rich")

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)
