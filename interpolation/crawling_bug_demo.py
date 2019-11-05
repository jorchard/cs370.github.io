
# Parametric Curve Demo

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.ion()

plt.close(1)
t = np.arange(0, 1, 0.01)

s = t
#s = t**4
#s = (0.125 + (t-0.5)**3)/0.25

x = np.cos(2.*np.pi*s)
y = np.sin(2.*np.pi*s)

#plt.figure(1)
#fig.clf()
f, ax = plt.subplots(nrows=2, ncols=2, sharex='col', sharey='row', figsize=(10,10))
#ax0 = plt.subplot(2,2,1)
#ax[0].axis('square')
ax[0,0].set_xlim(-1, 1)
ax[0,0].set_ylim(-1, 1)
ax[0,0].plot(x,y, '--', color='silver')
line, = ax[0,0].plot([], [], 'bo', markersize=14)

#ax_y = plt.subplot(2,2,2)
#ax_y.axis('square')
ax[0,1].set_xlim(0,1)
#ax_y.set_ylim(-1,1)
ax[0,1].plot(t,y, '--', color='silver')
line_y, = ax[0,1].plot([],[],'bo', markersize=14)

#ax_x = plt.subplot(2,2,3)
#ax_x.axis('square')
#ax_x.set_xlim(-1,1)
ax[1,0].set_ylim(0,1)
ax[1,0].plot(x,t, '--', color='silver')
line_x, = ax[1,0].plot([],[],'bo', markersize=14)

ax[1,1].axis('off')

def init():
	line.set_data([],[])
	line_y.set_data([],[])
	line_x.set_data([],[])
	return line, line_x, line_y,

def update(frame):
	t = frame[0]
	xdata = frame[1]
	ydata = frame[2]
	line.set_data(xdata, ydata)
	line_x.set_data(xdata, t)
	line_y.set_data(t, ydata)
	return line, line_x, line_y,

anim = FuncAnimation(f, update, frames=zip(t,x,y), blit=True, init_func=init, interval=40)
plt.show()
#plt.pause(0.1)




