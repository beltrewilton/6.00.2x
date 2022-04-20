import random
import secrets
import string
from ps1_partition import get_partitions
import time


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


def greedy_cow_transport(cows, limit=10):
    import collections
    items = collections.OrderedDict(sorted(cows.items(), reverse=True, key=lambda u: u[1]))
    trips = []

    def next_trip(it, limit):
        current_limit = 0
        trip = []
        names = list(it.keys())
        for n in names:
            if (current_limit + it.get(n)) <= limit:
                trip.append(n)
                current_limit = current_limit + it.get(n)
                it.pop(n)
        return trip, it

    trip, items = next_trip(items, limit)
    while len(trip) > 0:
        trips.append(trip)
        trip, items = next_trip(items, limit)

    return trips


def rnames():
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for g in range(10))


def _cows(n):
    return {rnames(): random.randint(0, 100) for i in range(0, n)}


def brute_force_cow_transport(cows, limit=10):
    best_len = 10**10
    selected = []

    for partitions in get_partitions(cows.keys()):
        if len(partitions) < best_len:
            reject = False
            for element in partitions:
                if sum([cows.get(i) for i in element]) <= limit:
                    reject = True
                else:
                    reject = False
                    break

            if reject:
                best_len = len(partitions)
                selected = partitions

    return selected




# cows = _cows(5)

m = {'Louis': 45, 'Patches': 60, 'Polaris': 20, 'Lotus': 10, 'Miss Bella': 15, 'Milkshake': 75, 'Clover': 5, 'Muscles': 65, 'MooMoo': 85, 'Horns': 50}
j = {'Daisy': 50, 'Abby': 38, 'Rose': 50, 'Dottie': 85, 'Buttercup': 72, 'Willow': 35, 'Betsy': 65, 'Coco': 10, 'Lilly': 24, 'Patches': 12}
h = {'Starlight': 54, 'Rose': 42, 'Luna': 41, 'Abby': 28, 'Buttercup': 11, 'Willow': 59, 'Betsy': 39, 'Coco': 59}
# r = greedy_cow_transport(cows, 100)
# print(r)


# brute_force_cow_transport(m, 100)

cows = load_cows("./unit-1/ps1_cow_data.txt")
start = time.time()
greedy_cow_transport(cows, 10)
end = time.time()
print(end - start)

# brute force : 0.3038620948791504
# greddy: 2.002716064453125e-05
