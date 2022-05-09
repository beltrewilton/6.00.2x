import random
import math


def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**.5
    return mean, std


def est_sin_x(num_needles):
    in_area = 0
    for n in range(1, num_needles + 1, 1):
        x = math.pi * random.random()
        y = random.random()
        if 0 < x <= math.sin(x) or 0 < y <= math.sin(x):
            in_area += 1
    return in_area/float(num_needles)


def throw_needles(num_needles):
    in_circle = 0
    for n in range(1, num_needles+1, 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**.5 <= 1.:
            in_circle += 1
    return 4 * (in_circle/float(num_needles))


def get_est(num_needles, num_trials):
    estimates = []
    for t in range(num_trials):
        # pi_guess = throw_needles(num_needles)
        pi_guess = est_sin_x(num_needles)
        estimates.append(pi_guess)
    mean, std = get_mean_and_std(estimates)
    print('Estimation: %s, Std. dev.: %s, Needles: %s' % (mean, std, num_needles))
    return mean, std


def estimate_pi(precision, num_trials):
    num_needles = 1000
    std = precision
    while std >= precision/1.96:
        mean, std = get_est(num_needles, num_trials)
        num_needles *= 2
    return mean

random.seed(0)
estimate_pi(0.005, 100)