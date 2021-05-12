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
        if top >= len(self.contents):
            balls_drawed = self.contents
        else:
            while(top > 0):
                balls_drawed.append(self.contents.pop(random.randint(0, top)))
                top = top -1

        return balls_drawed

    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    the_expected_balls = list()
    for color in expected_balls:
        for number in range(expected_balls[color]):
            the_expected_balls.append(color)
    #the_expected_balls.sort()



    for experiment in range(num_experiments):
        copy_hat = copy.copy(hat)
        returned_balls = copy_hat.draw(num_balls_drawn)
        #returned_balls.sort()
        #if the_expected_balls in returned_balls:
        if all(elem in the_expected_balls for elem in returned_balls):
            m = m +1
    
    return m / num_experiments

