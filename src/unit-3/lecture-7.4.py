import pylab
import random


def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**.5
    return mean, std


def plot_means(num_dice, num_rolls, num_bins, legend, color, style):
    means = []
    for i in range(num_rolls//num_dice):
        vals = 0
        for j in range(num_dice):
            vals += 5*random.random()
        means.append(vals/float(num_dice))
    pylab.hist(means, num_bins, color=color, label=legend, weights=pylab.array(len(means)*[1])/len(means), hatch= style)
    print(pylab.array(len(means)*[1])/len(means))
    return get_mean_and_std(means)


mean, std = plot_means(1, 1000000, 300, '1 die', 'b', '*')
print('Mean of rolling 1 die = %s, Std = %s' % (mean, std))
mean, std = plot_means(50, 1000000, 300, 'Mean of 50 dices', 'r', '//')
print('Mean of rolling 50 dies = %s, Std = %s' % (mean, std))

pylab.title('Rolling continous dice')
pylab.xlabel('Value')
pylab.ylabel('Probability')
pylab.legend()
pylab.show()