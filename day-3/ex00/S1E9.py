from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract class for Character
       https://irma.math.unistra.fr/~franck/cours/Pythonl2/cours7_2021_slides.pdf 
    """
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """ first_name : first name string of character
        is_alive : bool status of the character, true by default
        """


        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        pass

    
class Stark(Character):
    """class for representation of Stark character"""
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        self.is_alive = False