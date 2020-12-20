import random
import math


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

tmax = 875
t = 0

x = [0]
y = [0]


t=0
t_total = 0

dist = 0

#coord = [[x[t],y[t]]]

while t < tmax:
    coord = random.randint(0,1)

    if coord == 0:
        direction = random.randint(0,1)
        direction = 2*direction -1
        x.append(x[t] + direction)
        y.append(y[t])
        #print("x , " + str(direction))
    else:
        direction = random.randint(0,1)
        direction = 2*direction -1
        y.append(y[t] + direction)
        x.append(x[t])
    cur_dist = x[t]*x[t]+y[t]*y[t]
    if cur_dist > dist:
        dist = cur_dist
    #    print("y , " + str(direction))

    #    print(str(x[t]) + " , " +  str(y[t]))
    t=t+1
    #coord.append([x[t],y[t]])



print("max distance was " + str(math.sqrt(dist)))



height = 40
width = 40

fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(111)

xdata, ydata = [], []
ln, = plt.plot([], [])

points = np.c_[x, y]

def init():
#    ax.set_xticks(range(-10,10))
#    ax.set_yticks(range(-10,10))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    #ax.grid()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
#    ax.set_xlim([-1*width, width])
#    ax.set_ylim([-1*height, height])
    ax.set_aspect('equal')
    plt.tick_params(length=0)
    return ln,

def update(points):
    xdata.append(points[0])
    ydata.append(points[1])
    ln.set_data(xdata, ydata)
    ax.set_xticks(range(len(xdata)))
    ax.set_yticks(range(len(ydata)))
    ax.set_xlim([min(xdata+ydata)-1, max(xdata + ydata)+1])
    ax.set_ylim([min(xdata+ydata)-1, max(*xdata, *ydata)+1])
    #ax.grid(b=True, which='both', linewidth=1, c='b', linestyle='-')
    return ln,

input("waiting for input")
ani = animation.FuncAnimation(fig, update, frames=points,
                             init_func=init, blit=True, repeat=False, interval=1)


#ani.save('random_walk.mp4')

plt.show()
