from Geometry import Geometry

class Square(Geometry):
    
    def __init__(self, width):
        Geometry.__init__(self, width, width)

    def __str__(self):
        return f'This square has {self.width} of width.'
    
    def calculateArea(self):
        return self.width * self.height
