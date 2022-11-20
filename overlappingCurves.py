# Import libraries
import numpy as np
from os import path
import matplotlib.pyplot as plt

def main():

    labelsize   =   12
    width       =   6
    height      =   4 

    plt.rc('font', family ='serif')
    plt.rc('text', usetex = True)
    plt.rc('xtick', labelsize = labelsize)
    plt.rc('ytick', labelsize = labelsize)
    plt.rc('axes', labelsize = labelsize)

    fig1, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    fig1.subplots_adjust(left=.1, bottom=.2, right=.90, top=.97)

    N = 100
    y1 = np.random.randn(N)
    y2 = 2*np.random.randn(N)
    x = np.arange(N)

    ax1.plot(x,\
            y1,\
            label='Signal 1',\
            c='r',\
            alpha=0.7,\
            linewidth=1.5)

    ax2.plot(x,\
            y2,\
            label='Signal 2',\
            c='b',\
            alpha=0.8,\
            linewidth=1)

    ax1.set_xlabel('$x$')
    ax1.set_ylabel('$y_1$')
    ax2.set_ylabel('$y_2$')
    ax1.legend(loc='upper left')
    ax2.legend(loc= 'lower right')
    plt.show()

    fig1.set_size_inches(width, height)
    fig1.savefig(path.join('graphs', 'signals.jpeg'), dpi = 150)
    plt.close()

if __name__ == "__main__":
    main()
