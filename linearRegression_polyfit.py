# import some non-ml libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# set values for clean data visualization
labelsize 	= 12
width 		= 5
height 		= width / 1.618

plt.rc('font', family ='serif')
plt.rc('text', usetex = True)
plt.rc('xtick', labelsize = labelsize)
plt.rc('ytick', labelsize = labelsize)
plt.rc('axes', labelsize = labelsize)

fig1, ax 	= plt.subplots()
fig1.subplots_adjust(left=.16, bottom=.2, right=.99, top=.97)

# read the data
data 		= 	pd.read_csv('Temp_Vs_Chirp.csv').sort_values(by=['Temperature'])
x 			=	data['Temperature']
y 			=	data['Chirps']


# do the ploynomial fits
p0 = np.poly1d(np.polyfit(x, y, 0))
p1 = np.poly1d(np.polyfit(x, y, 1))
p2 = np.poly1d(np.polyfit(x, y, 2))


# plot the raw data and approximation functions
plt.scatter(x, y, color ='k', label = 'raw data')
plt.plot(x,p0(x), color= 'm', label = '$16.65x^0$') 
plt.plot(x,p1(x), color= 'g', label = '$0.21x-0.32$', linestyle='--') 
plt.plot(x,p2(x), color= 'b', label = '$0.0089x^2- 1.22x+ 56.79$', linestyle=':') 
plt.xlabel('Temperature in Fahrenheit')
plt.ylabel('number of chirps/sec')
plt.legend()

# save the graph
fig1.set_size_inches(width, height)
plt.savefig('polyfit.jpeg', dpi = 300)
plt.close()
