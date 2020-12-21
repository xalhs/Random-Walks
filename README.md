# Random-Walks
Simulation of simple and self-avoiding random walks in python.

This project is part of a presentation I did on Self-avoiding random walks. It contains the algorithms I used to generate and visualize Simple and Self avoiding random walks on 2, 3 and 4 dimensions. The presentation can also be found here.

## How to run

Go to `source/` and run any of the following 3 scripts:

- `2D_Comparing_Walks.py` change `tmax` parameter in line 10 to change the number of steps, this algorithm will produce two media files, one called '2D_Self_Avoiding.mp4' and one called '2D_Random_Walk.mp4' which are meant to view side by side. The borders of the two random walks are the same so sizes are directly comparable between the two. Change the `debug` parameter in line 11 to disable status messages.

- `3D_Random_Walk.py` again change `tmax` in line 15 to change number of steps, this algorithm will produce a 3D plot showing the evolution of the random walk

- `4D_Random_Walk.py` `tmax` in line 10 changes number of steps again, since we can't see 4D I showcase this result by taking the projection of the random walk in 2 coordinates each time, so it produces 4 media files each corresponding to a projection of a certain random walk.

## Detailed explanation
These simulations focus mainly on Self Avoiding Random Walks and comparisons to Simple Random Walks. A simple random walk on an n-dimensional Cartesian grid just has a 1/(2n) probability of going into each neighboring node. A self avoiding walk is this with the exception that it cannot revisit nodes that have been visited before (like the game snake). Now for each of the programs

Random_walk.py just does a regular random walk, having a 1/4 probability of going to each direction on every step. Then it plots the whole thing

random_self_avoiding.py does something similar, only it "remembers" all previously visited nodes and prevents the algorithm from going there again. Naturally this creates situations where the algorithm has no available points to go, to overcome this every once in a while it checks if it is in a safe position and if so it stores that position so that it can backtrack there if stuck. 

2d_comparing_walks.py runs both the simple random walk and self avoiding one and creates an mp4 file for each of those. The borders of the simulation are the same for these mp4s so sizes can be compared. The purpose is to see how different these two types of walks look in two dimensions, where the simple random walk confines to a small area, rarely moving outside of it, the self avoiding walk covers large distances and "closes off" big areas that it cannot visit again

3d_random_walk.py creates a self avoiding random walk in a 3 dimensional grid. It follows the same rules as the 2d self avoiding random walk and it creates savepoints once in a while. The difference is that since the algorithm runs in 3 dimensions, it is much harder to get stuck so the need to backtrack is significantly reduced. At the end, it visualizes the random walk in a 3D figure, the figure can be turned to view from different angles and after the animation finishes it can be zoomed into to see the structure of the random walk path better. Screenshots from the 3d algorithm can be seen below

4d_random_walk.py operates much like 2d_comparing_walks.py since it creates media for the self avoiding and the simple random walk. However since we cannot visualize 4 dimensions, the media are split in 2 projections for each walk for a total of 4 mp4 files. The first have the "XY" directions for each walk and the second have the "ZW" directions, "W" is the name I used for the 4th dimensional parameter. The purpose here is to see that in 4 dimensions the simple and the self avoiding walks cannot be distinguished easily (and on the scale of this simulation cannot be distinguished at all), thus the 4 projections will look statistically the same. 


### 3D Simulation

Some screenshots from the 3D animaption:

![](https://github.com/xalhs/Random-Walks/blob/master/media/3d_screenshot_1.png)

![](https://github.com/xalhs/Random-Walks/blob/master/media/3d_screenshot_2.png)

## Directory structure

- [`media/`](https://github.com/xalhs/Random-Walks/tree/master/media): directory containing media files that were produces as output from the scripts.
- [`source/`](https://github.com/xalhs/Random-Walks/tree/master/source): directory containing all source files that run the simulations.

