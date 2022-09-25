from Geometry import Geometry
from Color import Color

class Square(Geometry, Color):
    
    def __init__(self, width, color):
        Geometry.__init__(self, width, width)
        Color.__init__(self, color)

    def __str__(self):
        return f'This square has {self.width} of width and its color is {self.color}'
    
    def CalculateArea(self):
        return self.width * self.height
