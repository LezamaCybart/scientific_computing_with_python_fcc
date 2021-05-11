import copy
import random
# Consider using the modules imported above.

class Hat:
    hat = dict()
    contents = list()

    def __init__(self, **balls):
        self.hat = balls

        for color in self.hat:
            for number in range(self.hat[color]):
                self.contents.append(color)
    
    def draw(self, amount):
        top = amount
        balls_drawed = list()
        if top > len(self.contents):
            balls_drawed = self.contents
        else:
            while(top > 0):
                balls_drawed.append(self.contents.pop(random.randint(0, top)))
                top = top -1

        return balls_drawed

    


#def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

hat1 = Hat(yellow=3, blue=2, green=6)
print(hat1.hat)
print(hat1.contents)
print(hat1.draw(50))