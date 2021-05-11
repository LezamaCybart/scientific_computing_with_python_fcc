class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        result = ""
        if self.width > 50 or self.height > 50: 
            return "Too big for picture."
        else:
            for i in range(self.height):
                for j in range(self.width):
                    result = result + "*"
                result = result + "\n"
        return result
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def get_amount_inside(self, polygon):
        return int(self.get_area() / polygon.get_area())
        


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side
    
    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side
    
    def __str__(self):
        return f"Square(side={self.width})"
    