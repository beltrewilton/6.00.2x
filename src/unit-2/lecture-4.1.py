import pylab as plt

mysamples = []
mylinear = []
myquadratic = []
mycubic = []
myexponential = []

for i in range(0, 30):
    mysamples.append(i)
    mylinear.append(i)
    myquadratic.append(i**2)
    mycubic.append(i**3)
    myexponential.append(1.5**i)

plt.figure('lin quad')
plt.clf()
plt.plot(mysamples, mylinear, label='linear')
plt.plot(mysamples, myquadratic, label='quadratic')
plt.legend()

plt.figure('cube expo')
plt.clf()
plt.plot(mysamples, mycubic, label='cubic')
plt.plot(mysamples, myexponential, label='exponential')
plt.yscale('log')
plt.legend()
plt.figure('lin quad')
plt.title('Linear vs. Quadratic')
plt.figure('cube expo')
plt.title('Cubic vs. Exponential')

plt.show()

