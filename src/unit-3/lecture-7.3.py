import scipy
from scipy import integrate
import random


def gaussian(x, mu, sigma):
    factor_1 = (1./(sigma*(scipy.pi*2)**.5))
    factor_2 = scipy.e**-(((x-mu)**2)/(2*sigma**2))
    return factor_1 * factor_2

def check_empirical(num_trials):
    for t in range(num_trials):
        mu = random.randint(-10, 10)
        sigma = random.randint(1, 10)
        print('For mu: %s and sigma: %s' % (mu, sigma))
        for num_std in (1, 1.96, 3):
            area = integrate.quad(gaussian, mu-num_std*sigma, mu+num_std*sigma, (mu, sigma))[0]
            print('Fraction (a:%s, b:%s) within %s, std: %s' % (mu-num_std*sigma, mu+num_std*sigma, num_std, round(area, 6)))

check_empirical(3)