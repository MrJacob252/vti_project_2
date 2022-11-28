# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# x = np.arange(10)
# y = np.random.random(10)

# fig = plt.figure()

# plt.xlim(0,10)
# plt.ylim(0,1)
# graph = plt.plot([],[],'o')

# def animate(i):
#     graph.set_data(x[:i+1], y[:i+1])
#     return graph

# ani = FuncAnimation(fig, animate, frames=10, interval=200)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# fig, ax = plt.subplots()

# x = np.arange(0, 2*np.pi, 0.01)
# line, = ax.plot(x, np.sin(x))


# def animate(i):
#     line.set_ydata(np.sin(x + i / 50))  # update the data.
#     return line,


# ani = animation.FuncAnimation(
#     fig, animate, interval=20, blit=True, save_count=50)

# # To save the animation, use e.g.
# #
# # ani.save("movie.mp4")
# #
# # or
# #
# # writer = animation.FFMpegWriter(
# #     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# # ani.save("movie.mp4", writer=writer)

# plt.show()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

steps = 50
nodes = 100
positions = []
solutions = []

for i in range(steps):
   positions.append(np.random.rand(2, nodes))
   solutions.append(np.random.random(nodes))

fig, ax = plt.subplots()
marker_size = 50

def animate(i):
   fig.clear()
   ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim=(0, 1), ylim=(0, 1))
   ax.set_xlim(0, 1)
   ax.set_ylim(0, 1)
   s = ax.scatter(positions[i][0], positions[i][1], s=marker_size, c=solutions[i], cmap="RdBu_r", marker="o", edgecolor='black')

plt.grid(False)
ani = animation.FuncAnimation(fig, animate, interval=100, frames=range(steps))
plt.show()
ani.save('animation.gif', writer='pillow')