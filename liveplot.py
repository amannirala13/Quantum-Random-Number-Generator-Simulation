# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 01:39:31 2020

@author: amann
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('log.txt', 'r').read()
    lines = graph_data.split('\n')
    print(lines)
    xa = []
    ya = []
    for line in lines:
        if len(line)>1:
            x,y = line.split(',')
            xa.append(x)
            ya.append(y)
    
    ax.clear()
    ax.plot(xa, ya)

ani = animation.FuncAnimation(fig, animate, interval = 500)
plt.show()