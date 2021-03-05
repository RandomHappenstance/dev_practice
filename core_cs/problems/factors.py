import sympy
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def get_factors(num):
    factors = []
    if not sympy.isprime(num):
        for m in range(1, num+1):
            if num % m == 0 and m != num and m != 1:
                factors.append(m)
    return factors


def animate(i):
    # print(counter)

    x = next(index)  # counter or x variable -> index
    counter = next(index)
    print(counter)
    x_values.append(x)
    '''
    Three random value series ->
    Y : 0-5
    Z : 3-8
    Q : 0-10
    '''
    y = random.randint(0, 5)
    z = random.randint(3, 8)
    q = random.randint(0, 10)
    # append values to keep graph dynamic
    # this can be replaced with reading values from a csv files also
    # or reading values from a pandas dataframe
    y_values.append(y)
    z_values.append(z)
    q_values.append(q)

    if counter > 40:
        '''
        This helps in keeping the graph fresh and refreshes values after every 40 timesteps
        '''
        x_values.pop(0)
        y_values.pop(0)
        z_values.pop(0)
        q_values.pop(0)
        # counter = 0
        plt.cla()  # clears the values of the graph

    plt.plot(x_values, y_values, linestyle='--')

    ax.legend(["Value 1 ", "Value 2", "Value 3"])
    ax.set_xlabel("X values")
    ax.set_ylabel("Values for Three different variable")
    plt.title('Dynamic line graphs')

    time.sleep(.25)  # keep refresh rate of 0.25 seconds


if __name__ == "__main__":

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    plt.style.use("ggplot")
    plt.plot([], [])
    plt.show()

    xdata = []
    ydata = []
    axes = plt.gca()
    axes.set_xlim(0, 100000)
    axes.set_ylim(0, +250)
    line, = axes.plot(xdata, ydata, 'r-')

    for i in range(120000):
        # print(i)
        f = get_factors(i)
        plt.ion()
        xdata.append(len(f))
        ydata.append(i)
        line.set_xdata(xdata)
        line.set_ydata(ydata)
        plt.plot(xdata, ydata)
        plt.draw()

    plt.show()