# Random-Walks
Simulation of simple and self-avoiding random walks in python.

This project is part of a presentation I did on Self-avoiding random walks. It contains the algorithms I used to generate and visualize Simple and Self avoiding random walks on 2, 3 and 4 dimensions. The presentation can also be found here.

## How to run

Go to `source/` and run any of the following 3 scripts:

- `2D_Comparing_Walks.py` change `tmax` parameter in line 10 to change the number of steps, this algorithm will produce two media files, one called '2D_Self_Avoiding.mp4' and one called '2D_Random_Walk.mp4' which are meant to view side by side. The borders of the two random walks are the same so sizes are directly comparable between the two. Change the `debug` parameter in line 11 to disable status messages.

- `3D_Random_Walk.py` again change `tmax` in line 15 to change number of steps, this algorithm will produce a 3D plot showing the evolution of the random walk

- `4D_Random_Walk.py` `tmax` in line 10 changes number of steps again, since we can't see 4D I showcase this result by taking the projection of the random walk in 2 coordinates each time, so it produces 4 media files each corresponding to a projection of a certain random walk.

## Detailed explanation

## Directory structure

- [`media/`](https://github.com/xalhs/Random-Walks/tree/master/media): directory containing media files that were produces as output from the scripts.
- [`source/`](https://github.com/xalhs/Random-Walks/tree/master/source): directory containing all source files that run the simulations.

