#!/usr/bin/env python3

# Fortune Wheel to select the leader for the OMG discussion 
# [Zheng Zheng @ U of Utah, 20210606]

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

Names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace']
np.random.shuffle(Names)
print("The discussion leader will be one of")
print(Names)
N = len(Names)
data = [1]*N

fig, ax = plt.subplots(figsize=(8,8))
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.set_aspect(1)
ax.set_title('Order-of-Magnitude for the Group', fontsize=20, weight='bold')
ax.text(0, 0, 'OMG', ha='center', va='center', color='k', fontsize=60, weight='bold')

wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=90, labels=Names, textprops={'size': 20})

r = np.arange(0,0.9,0.1)
t = 0
x = r*np.cos(t)
y = r*np.sin(t)
line, = ax.plot(x, y, linewidth=10, color='y')

rand = np.random.rand(1)
t = np.arange(0,(1+4*rand)*2*np.pi,0.05)
t = -t+np.pi/2 
def animate(i):
    if i==1 : 
       input("Press Enter to start ...")
    line.set_xdata(r*np.cos(t[i]))
    line.set_ydata(r*np.sin(t[i]))  # update the data.
    return line,

ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=5, blit=True, repeat=False, save_count=50)

plt.show()


