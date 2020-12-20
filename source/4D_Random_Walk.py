import random
import math


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import threading

tmax = 1000
t = 0

x = [0]
y = [0]
z = [0]
w = [0]


t=0
t_total = 0
coodr = [[x[t],y[t],z[t],w[t]]]
dist = 0
left = True
up  = True
right = True
down = True
front = True
behind = True
w_plus = True
w_minus = True
while t < tmax:# and t_total < tmax:
#    print(len(x) ,  len(y) , len(coodr))
    if [(x[t]-1),y[t],z[t],w[t]] in coodr:
        left = False
    else:
        left = True
    if [(x[t]+1),y[t],z[t],w[t]] in coodr:
        right = False
    else:
        right = True
    if [(x[t]),(y[t]+1),z[t],w[t]] in coodr:
        front = False
    else:
        front = True
    if [(x[t]),(y[t]-1),z[t],w[t]] in coodr:
        behind = False
    else:
        behind = True
    if [(x[t]),(y[t]),(z[t]+1),w[t]] in coodr:
        up = False
    else:
        up = True
    if [(x[t]),(y[t]),(z[t]-1),w[t]] in coodr:
        down = False
    else:
        down = True
    if [(x[t]),(y[t]),(z[t]),(w[t]+1)] in coodr:
        w_plus = False
    else:
        w_plus = True
    if [(x[t]),(y[t]),(z[t]),(w[t]-1)] in coodr:
        w_minus = False
    else:
        w_minus = True

    all_dir = [left, front,right, behind, up,  down, w_plus , w_minus]
#    print(all_dir)
    available_dir = []
    i=0
    for dir in all_dir:
        if dir == True:
            available_dir.append(i)
        i=i+1
#    print(available_dir)
    if False:
        if len(available_dir) == 5:
            left_inf = []
            up_inf = []
            right_inf = []
            down_inf = []
            front_inf = []
            behind_inf = []
            for j in range(0,100):
            #for j in range(0, tmax):
                left_inf.append([x[t]-j,y[t],z[t]] )
                front_inf.append([x[t],y[t]+j,z[t]] )
                right_inf.append([x[t]+j,y[t],z[t]] )
                behind_inf.append([x[t],y[t]-j,z[t]] )
                up_inf.append([x[t],y[t],z[t]+j] )
                down_inf.append([x[t],y[t],z[t]-j] )
        #    left_inf_tuple = [tuple(lst) for lst in left_inf]
            left_inf_tuple = set(map(tuple, left_inf))
            up_inf_tuple = set(map(tuple, up_inf))
            right_inf_tuple = set(map(tuple, right_inf))
            down_inf_tuple = set(map(tuple, down_inf))
            front_inf_tuple = set(map(tuple, front_inf))
            behind_inf_tuple = set(map(tuple, behind_inf))
            coord_tuple = set(map(tuple, coodr))
        #    print("types")
        #    print(type(left_inf_tuple))
        #    print(type((coord_tuple)) )
        #    print((left_inf_tuple).intersection(coord_tuple))
            if  (left_inf_tuple).intersection(coord_tuple) == set():
            #if (any(i in left_inf_tuple for j in coord_tuple)):
            #    print(left_inf_tuple)
            #    print([x[t] , y[t]])
            #    print(coord_tuple)
                #print(left_inf)
            #    print("left is safe")
                safe_t = t
            elif  (up_inf_tuple).intersection(coord_tuple) == set():
            #    print("up is safe")
                safe_t = t
            elif  (right_inf_tuple).intersection(coord_tuple) == set():
            #    print("right is safe")
                safe_t = t
            elif  (down_inf_tuple).intersection(coord_tuple) == set():
            #    print("down is safe")
                safe_t = t
            elif  (front_inf_tuple).intersection(coord_tuple) == set():
            #    print("front is safe")
                safe_t = t
            elif (behind_inf_tuple).intersection(coord_tuple) == set():
            #    print("behind is safe")
                safe_t = t


    #    safe_t = t
    #    print(t)
    #    print("tsafe = " + str(safe_t))
    if not available_dir:
        print("backtracking...")
        t_diff = t - safe_t
        t = safe_t
        print("went back " + str(t_diff) + " steps")
        coodr = coodr[:-(t_diff)]
        x = x[:-(t_diff)]
        y = y[:(-(t_diff))]
        z = z[:-(t_diff)]

        print("current length " + str(len(x)))
    else:
        chosen_dir = random.choice(available_dir)
        if chosen_dir == 0:
            x.append(x[t]-1)
            y.append(y[t])
            z.append(z[t])
            w.append(w[t])
        elif chosen_dir == 1:
            x.append(x[t])
            y.append(y[t]+1)
            z.append(z[t])
            w.append(w[t])
        elif chosen_dir == 2:
            x.append(x[t]+1)
            y.append(y[t])
            z.append(z[t])
            w.append(w[t])
        elif chosen_dir == 3:
            x.append(x[t])
            y.append(y[t]-1)
            z.append(z[t])
            w.append(w[t])
        elif chosen_dir == 4:
            x.append(x[t])
            y.append(y[t])
            z.append(z[t]+1)
            w.append(w[t])
        elif chosen_dir == 5:
            x.append(x[t])
            y.append(y[t])
            z.append(z[t]-1)
            w.append(w[t])
        elif chosen_dir == 6:
            x.append(x[t])
            y.append(y[t])
            z.append(z[t])
            w.append(w[t]+1)
        elif chosen_dir == 7:
            x.append(x[t])
            y.append(y[t])
            z.append(z[t])
            w.append(w[t]-1)


        cur_dist = x[t]*x[t]+y[t]*y[t]+z[t]*z[t]+w[t]*w[t]
        if cur_dist > dist:
            dist = cur_dist
        coodr.append([x[t],y[t],z[t],w[t]])
        t=t+1
    t_total = t_total + 1

if False:
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
    coodr.append([x[t],y[t]])

print("max distance was " + str(math.sqrt(dist)))





#ani.save('random_walk.mp4')

import random
import math


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

tmax = t
t = 0

x2 = x
y2 = y
z2 = z
w2 = w
#print(z2)
#print(w2)
x = [0]
y = [0]
z = [0]
w = [0]


t=0
t_total = 0

dist = 0

#coord = [[x[t],y[t]]]

while t < tmax:
    coord = random.randint(0,3)

    if coord == 0:
        direction = random.randint(0,1)
        direction = 2*direction -1
        x.append(x[t] + direction)
        y.append(y[t])
        z.append(z[t])
        w.append(w[t])
        #print("x , " + str(direction))
    elif coord == 1:
        direction = random.randint(0,1)
        direction = 2*direction -1
        y.append(y[t] + direction)
        x.append(x[t])
        z.append(z[t])
        w.append(w[t])
    elif coord ==2:
        direction = random.randint(0,1)
        direction = 2*direction -1
        y.append(y[t] )
        x.append(x[t])
        z.append(z[t]+ direction)
        w.append(w[t])
    elif coord == 3:
        direction = random.randint(0,1)
        direction = 2*direction -1
        y.append(y[t] )
        x.append(x[t])
        z.append(z[t])
        w.append(w[t]+ direction)
    cur_dist = x[t]*x[t]+y[t]*y[t]+z[t]*z[t]+w[t]*w[t]
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

xdata, ydata , zdata, wdata = [], [] ,[] ,[]
x2data, y2data, z2data, w2data = [], [] ,[] ,[]
ln, = plt.plot([], [])

#x = [0, 0, 0, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5]
#y = [0, 1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8]

points = np.c_[x, y, x2, y2,z,w,z2,w2]

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
    x2data.append(points[2])
    y2data.append(points[3])
    zdata.append(points[4])
    wdata.append(points[5])
    z2data.append(points[6])
    w2data.append(points[7])
    ln.set_data(x2data, y2data)
    ax.set_xticks(range(len(x2data)))
    ax.set_yticks(range(len(y2data)))
    ax.set_xlim([min(xdata+ydata+x2data+y2data+zdata +wdata+z2data+w2data)-1, max(xdata + ydata + x2data + y2data+zdata +wdata+z2data+w2data)+1])
    ax.set_ylim([min(xdata+ydata+x2data+y2data+zdata +wdata+z2data+w2data)-1, max(*xdata, *ydata, *x2data, *y2data, *zdata , *wdata , *z2data ,*w2data)+1])
    #ax.grid(b=True, which='both', linewidth=1, c='b', linestyle='-')
    return ln,
print("plotting self avoiding XY coordinates")
#input("waiting for input")
ani = animation.FuncAnimation(fig, update, frames=points,
                             init_func=init, blit=True, repeat=False, interval=50)

ani.save('4Drandom_self_avoiding_walk2_XY.mp4')
#plt.show()

height = 40
width = 40

fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(111)

xdata, ydata , zdata, wdata = [], [] ,[] ,[]
x2data, y2data, z2data, w2data = [], [] ,[] ,[]
ln, = plt.plot([], [])

#x = [0, 0, 0, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5]
#y = [0, 1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8]

points = np.c_[x, y, x2, y2,z,w,z2,w2]
#points2 = np.c_[x2, y2]

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
    x2data.append(points[2])
    y2data.append(points[3])
    zdata.append(points[4])
    wdata.append(points[5])
    z2data.append(points[6])
    w2data.append(points[7])
    ln.set_data(z2data, w2data)
    ax.set_xticks(range(len(z2data)))
    ax.set_yticks(range(len(w2data)))
    ax.set_xlim([min(xdata+ydata+x2data+y2data+zdata +wdata+z2data+w2data)-1, max(xdata + ydata + x2data + y2data+zdata +wdata+z2data+w2data)+1])
    ax.set_ylim([min(xdata+ydata+x2data+y2data+zdata +wdata+z2data+w2data)-1, max(*xdata, *ydata, *x2data, *y2data, *zdata , *wdata , *z2data ,*w2data)+1])
    #ax.grid(b=True, which='both', linewidth=1, c='b', linestyle='-')
    #ax.grid(b=True, which='both', linewidth=1, c='b', linestyle='-')
    return ln,

#input("waiting for input")
print("plotting self avoiding ZW coordinates")
ani = animation.FuncAnimation(fig, update, frames=points,
                             init_func=init, blit=True, repeat=False, interval=50)


ani.save('4Drandom_self_avoiding_walk2_ZW.mp4')

plt.show()


height = 40
width = 40

fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(111)

xdata, ydata , zdata, wdata = [], [] ,[] ,[]
x2data, y2data, z2data, w2data = [], [] ,[] ,[]
ln, = plt.plot([], [])

#x = [0, 0, 0, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5]
#y = [0, 1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8]

points = np.c_[x, y, x2, y2,z,w,z2,w2]
#points2 = np.c_[x2, y2]

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
    x2data.append(points[2])
    y2data.append(points[3])
    zdata.append(points[4])
    wdata.append(points[5])
    z2data.append(points[6])
    w2data.append(points[7])
    ln.set_data(xdata, ydata)
    ax.set_xticks(range(len(xdata)))
    ax.set_yticks(range(len(ydata)))
    ax.set_xlim([min(xdata+ydata+x2data+y2data+zdata +wdata+z2data+w2data)-1, max(xdata + ydata + x2data + y2data+zdata +wdata+z2data+w2data)+1])
    ax.set_ylim([min(xdata+ydata+x2data+y2data+zdata +wdata+z2data+w2data)-1, max(*xdata, *ydata, *x2data, *y2data, *zdata , *wdata , *z2data ,*w2data)+1])
    #ax.grid(b=True, which='both', linewidth=1, c='b', linestyle='-')
    #ax.grid(b=True, which='both', linewidth=1, c='b', linestyle='-')
    return ln,

#input("waiting for input")
print("plotting simple walk XY coordinates")
ani = animation.FuncAnimation(fig, update, frames=points,
                             init_func=init, blit=True, repeat=False, interval=50)


ani.save('4D_random_walk2_XY.mp4')

#plt.show()

height = 40
width = 40

fig = plt.figure(figsize=(10, 10))
ax = plt.subplot(111)

xdata, ydata , zdata, wdata = [], [] ,[] ,[]
x2data, y2data, z2data, w2data = [], [] ,[] ,[]
ln, = plt.plot([], [])

#x = [0, 0, 0, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5]
#y = [0, 1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 7, 7, 7, 8, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8]

points = np.c_[x, y, x2, y2,z,w,z2,w2]
#points2 = np.c_[x2, y2]

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
    x2data.append(points[2])
    y2data.append(points[3])
    zdata.append(points[4])
    wdata.append(points[5])
    z2data.append(points[6])
    w2data.append(points[7])
    ln.set_data(zdata, wdata)
    ax.set_xticks(range(len(zdata)))
    ax.set_yticks(range(len(wdata)))
    ax.set_xlim([min(xdata+ydata+x2data+y2data+zdata +wdata+z2data+w2data)-1, max(xdata + ydata + x2data + y2data+zdata +wdata+z2data+w2data)+1])
    ax.set_ylim([min(xdata+ydata+x2data+y2data+zdata +wdata+z2data+w2data)-1, max(*xdata, *ydata, *x2data, *y2data, *zdata , *wdata , *z2data ,*w2data)+1])
    #ax.grid(b=True, which='both', linewidth=1, c='b', linestyle='-')
    #ax.grid(b=True, which='both', linewidth=1, c='b', linestyle='-')
    return ln,

print("plotting simple walk ZW coordinates")
#input("waiting for input")
ani = animation.FuncAnimation(fig, update, frames=points,
                             init_func=init, blit=True, repeat=False, interval=50)


ani.save('4D_random_walk2_WZ.mp4')

#plt.show()
