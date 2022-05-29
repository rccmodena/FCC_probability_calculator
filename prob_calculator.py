#!/usr/bin/env python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""

import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for color, n in kwargs.items():
            self.contents += [color] * n

    def draw(self, n_balls):
        if n_balls >= len(self.contents):
            return self.contents
        else:
            return [self.contents.pop(random.randint(0, len(self.contents) -1)) for _ in range(n_balls)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    for _ in range(num_experiments):
        compare_balls = expected_balls.copy()
        copy_hat = copy.deepcopy(hat)
        balls_drawn = copy_hat.draw(num_balls_drawn)
        for ball in balls_drawn:
            if compare_balls.get(ball) is not None:
                compare_balls[ball] -= 1
        
        if all([True if v <= 0 else False for k, v in compare_balls.items()]):
            num_success += 1

    return num_success / num_experiments