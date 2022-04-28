# random walks simulation
import random


class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        x_dist = self.x - ox
        y_dist = self.y - oy
        return (x_dist**2 + y_dist**2)**5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'


class Field(object):
    def __init__(self):
        self.drunks = {}

    def add_drunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc

    def get_loc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

    def move_drunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        x_dist, y_dist = drunk.take_step()
        current_location = self.drunks[drunk]
        # use move method of Location to get new location
        self.drunks[drunk] = current_location.move(x_dist, y_dist)


class Drunk(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'This drunk is named ' + self.name


class UsualDrunk(Drunk):
    def take_step(self):
        step_choices = [(0., 1.), (0., -1.), (1., 0.), (-1., 0.)]
        return random.choice(step_choices)


class ColdDrunk(Drunk):
    def take_step(self):
        step_choices = [(0., .9), (0., -1.), (1., 0.), (-1., 0.)]
        return random.choice(step_choices)


def walk(field, drunk, num_steps):
    start = field.get_loc(drunk)
    for s in range(num_steps):
        field.move_drunk(drunk)
    return start.distFrom(field.get_loc(drunk))


def sim_walks(num_steps, num_trials, d_class):
    homer = d_class('juan')
    origin = Location(0, 0)
    distances = []
    for t in range(num_trials):
        f = Field()
        f.add_drunk(homer, origin)
        distances.append(round(walk(f, homer, num_steps), 1))
    return distances


def drunkTest(walk_len, num_trials, d_class):
    for nstep in walk_len:
        distances = sim_walks(nstep, num_trials, d_class)
        print(d_class.__name__, 'random walk of ', nstep, ' steps')
        print(' Mean =', round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances), ' Min =', min(distances))


random.seed(0)
drunkTest((0, 1, 2), 100, UsualDrunk)