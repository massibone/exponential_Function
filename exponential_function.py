import matplotlib.pyplot as plt
import numpy as np
import random

# 100 linearly spaced numbers
x = np.linspace(-2,2,100)

# the function, which is y = e^x here
y = np.exp(x)
y2 = -y
y3 = y**0
# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y, 'y', label='y=e^x')
plt.plot(x,y2, 'g', label='x=-1')
plt.plot(x,y3, 'b', label='x=1')



plt.legend(loc='upper left')

# show the plot
plt.show()



