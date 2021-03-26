from random import random


class MonteCarlo:
    
    def __init__(self, length, width, rectangles):
        """constructor
        :param length - length of the enclosing rectangle
        :param width - width of the enclosing rectangle
        :param rectangles - array that contains the embedded rectangles
        :raises ValueError if any of the paramters is None
        """
        self.l = length
        self.w = width
        self.r = rectangles
        if self.l is None or self.w is None or self.r is None:
            raise ValueError("The parameters can't be None")
        

    def area(self, num_of_shots):
        """Method "area "to estimate the area of the enclosing rectangle that is not covered by the embedded rectangles
        :param num_of_shots - Number (>0) of generated random points whose location (inside/outside) is analyzed
        :return float
        :raises ValueError if any of the paramters is None
        """
        n=num_of_shots
        nr=0
        i=0
        for i in range (0,n):
            x = self.l*random()
            y = self.w*random()
            ok=0
            for j in self.r:#testing for each rectangle
                if self.inside(x, y, j) == True:
                    ok=1
                    break
            if ok==0:
                nr=nr+1    
        if n is None:
            raise ValueError("The parameters can't be None")
        
        return nr/n*self.l*self.w
        
    def inside(self, x, y, rect):
        """Method "inside" to determine if a given point (x,y) is inside a given rectangle
        :param x,y - coordinates of the point to check
        :param rect - given rectangle
        :return bool
        :raises ValueError if any of the paramters is None
        """
        if x >= rect.origin_x and y >= rect.origin_y and x <= rect.origin_x+rect.length and y <= rect.origin_y+rect.width:
            return True
        else:
            return False
        if x is None or y is None or rect is None:
            raise ValueError("The parameters can't be None")
