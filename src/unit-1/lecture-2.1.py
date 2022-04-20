class Food(object):
    def __init__(self, name, value, cost, cal):
        self.name = name
        self.value = value
        self.cost = cost
        self.calories = cal

    def getValue(self):
        return self.value

    def getCost(self):
        return self.cost

    def density(self):
        return self.getValue()/self.getCost()

    def __str__(self):
        return '{} : < {} , {} >'.format(self.name, self.value, self.calories)


def builMenu(names, values, cost, calories):
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], cost[i], calories[i]))
    return menu


def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
    Returns a tuples of the total value of a solution to the 0/1 knapsack
    problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getCost())
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # Explore better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'coke', 'apple', 'donut']
values = [89, 90, 30, 50, 90 , 79, 90, 10]
costs = [1, 1, 1, 1, 1, 1, 1, 1]
calories = [123, 154, 258, 354, 365, 150, 95, 195]


m = builMenu(names, values, costs, calories)
r = maxVal(m, 1)
for ri in r[1]:
    print(str(ri))