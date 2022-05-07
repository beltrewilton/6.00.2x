import random


class FairRoulette(object):
    def __init__(self):
        self.pockets = [i for i in  range(1, 37)]
        self.ball = None
        self.black_odds, self.red_odds = 1., 1.
        self.pocket_odds = len(self.pockets) - 1.

    def spin(self):
        self.ball = random.choice(self.pockets)

    def is_black(self):
        if type(self.ball) != int:
            return False
        if (0 < self.ball <= 10) or (18 < self.ball <= 28):
            # (self.ball > 0 and self.ball <= 10) or (self.ball > 18 and self.ball <= 28):
            return self.ball % 2 == 0
        else:
            return self.ball % 2 == 1

    def is_red(self):
        return type(self.ball) == int and not self.is_black()

    def bet_black(self, amount):
        if self.is_black():
            return amount * self.black_odds
        else:
            return -amount

    def bet_red(self, amount):
        if self.is_red():
            return amount * self.red_odds
        else:
            return -amount * self.red_odds

    def bet_pocket(self, pocket, amount):
        if str(pocket) == str(self.ball):
            return amount * self.pocket_odds
        else:
            return -amount

    def __str__(self):
        return 'Fair Roulette'


class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')

    def __str__(self):
        return 'European Roulette'


class AmRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('00')

    def __str__(self):
        return 'American Roulette'


def get_mean_and_std(X):
    mean = sum(X)/float(len(X))
    tot = 0.
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**.5
    return mean, std


def play_roulette(game: FairRoulette, num_spins, to_print = True):
    lucky_number = 2
    bet = 1
    tot_red, tot_black, tot_pocket = 0., 0., 0.
    for i in range(num_spins):
        game.spin()
        tot_red += game.bet_red(bet)
        tot_black += game.bet_black(bet)
        tot_pocket += game.bet_pocket(lucky_number, bet)

    if to_print:
        print('%s spins of %s' % (num_spins, game))
        print('Expected return betting red = %s %%' % (str(100*tot_red/num_spins)))
        print('Expected return betting black = %s %%' % (str(100*tot_black/num_spins)))
        print('Expected return betting betting %s = %s %%' % (lucky_number, str(100*tot_pocket/num_spins)))

    return (tot_red/num_spins, tot_black/num_spins, tot_pocket/num_spins)


def find_pocket_return(game, num_trials, trial_size, to_print):
    pocket_returns = []
    for i in range(num_trials):
        trial_vals = play_roulette(game, trial_size, to_print)
        pocket_returns.append(trial_vals[2])

    return pocket_returns


random.seed(0)
num_trials = 20
result_dict = {}
games = (FairRoulette, EuRoulette, AmRoulette)
for G in games:
    result_dict[G().__str__()] = []

for num_spins in (100, 1000, 10000, 100000):
    print('\nSimulate betting a pocket for %s trials %s spins each' % (num_trials, num_spins))
    for G in games:
        pocket_returns = find_pocket_return(G(), num_trials, num_spins, False)
        mean, std = get_mean_and_std(pocket_returns)
        result_dict[G().__str__()].append((num_spins, 100*mean, 100*std))
        print('Expected return for %s = %s%% +/- %s%% with 95%% confidence.' % (G(), round(100*mean, 3), round(100*1.96*std, 3)))



# num_spins = 100000000
# game = FairRoulette()
# play_roulette(game, num_spins)