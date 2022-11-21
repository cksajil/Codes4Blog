# Import librarires
import numpy as np
from os import path
import matplotlib.pyplot as plt

def main():

    # Set plotting parameters
    labelsize   =   12
    width       =   5
    height      =   width / 1.618

    plt.rc('font', family ='serif')
    plt.rc('xtick', labelsize = labelsize)
    plt.rc('ytick', labelsize = labelsize)
    plt.rc('axes', labelsize = labelsize)

    fig1, ax = plt.subplots()
    fig1.subplots_adjust(left=.16, bottom=.2, right=.99, top=.97)

    N = 10
    x = np.arange(N)
    y = x**3+2*x+2

    # Do the ploynomial fits
    p0 = np.poly1d(np.polyfit(x, y, 0))
    p1 = np.poly1d(np.polyfit(x, y, 1))
    p2 = np.poly1d(np.polyfit(x, y, 2))

    # Plot the raw data and approximation functions
    plt.scatter(x, y, color ='k', label = 'raw data')
    plt.plot(x,p0(x), color= 'm', label = 'order 0 fit') 
    plt.plot(x,p1(x), color= 'g', label = 'order 1 fit', linestyle='--') 
    plt.plot(x,p2(x), color= 'b', label = 'order 2 fit', linestyle=':') 
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()

    # Save the graph
    fig1.set_size_inches(width, height)
    plt.savefig(path.join('graphs', 'polyfit.jpeg'), dpi = 150)
    plt.close()

if __name__ == "__main__":
    main()
