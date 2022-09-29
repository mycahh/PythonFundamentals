# ABC = Abstract Base Class
from abc import ABC, abstractmethod

class Geometry(ABC):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    @abstractmethod
    def calculateArea(self):
        pass

