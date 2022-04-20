import pylab as plt


def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    m_rate = rate / 12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + m_rate) + monthly]
    return base, savings


def display_retire(monthlies, rates, terms):
    plt.figure('retire-both')
    plt.clf()
    plt.xlim(30 * 12, 40 * 12)
    month_labels = ['r', 'b', 'g', 'k']
    rate_labels = ['-', 'o', '--']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        month_label = month_labels[i % len(month_labels)]
        for j in range(len(rates)):
            rate = rates[j]
            rate_label = rate_labels[j % len(rate_labels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals, yvals, month_label + rate_label,
                     label='retire:' + str(monthly) + ':' + str(int(rate * 100)))

    plt.legend()
    plt.show()


display_retire([500, 550, 600, 650], [.01, .02, .03, .035], 40 * 12)

print()
