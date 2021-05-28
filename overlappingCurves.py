# import some non-ml libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# set values for clean data visualization
labelsize 	= 12
# width 		= 9
width 		= 6
height 		= 4 # width / 1.618
# height 		= width / 1.618

plt.rc('font', family ='serif')
plt.rc('text', usetex = True)
plt.rc('xtick', labelsize = labelsize)
plt.rc('ytick', labelsize = labelsize)
plt.rc('axes', labelsize = labelsize)

fig1, ax1 = plt.subplots()
ax2 = ax1.twinx()
fig1.subplots_adjust(left=.1, bottom=.2, right=.90, top=.97)


dataset = pd.read_csv('DRREDDY.csv')
y1 = dataset['Open'].values
N = dataset.shape[0]
x = np.arange(N)

y2 = y1.copy()
y2[2500:]= y1[2500:]+2000
y2 = y2/(np.max(y2)-np.min(y2))


ax1.plot(x, y1, label='Signal 1', c='g', alpha=0.4,linewidth=1.5)
ax2.plot(x, y2, label='Signal 2', c='b', alpha=0.5,linewidth=1)

ax1.set_xlabel('$x$')
ax1.set_ylabel('$y_1$')
ax2.set_ylabel('$y_2$')
ax1.legend(loc='upper left')
ax2.legend(loc= 'lower right')
# plt.show()


# save the graph
fig1.set_size_inches(width, height)
plt.savefig('Signals2.jpeg', dpi = 200)
plt.close()