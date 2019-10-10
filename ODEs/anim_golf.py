
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp

plt.ion()

np.seterr(divide='ignore');

Vx = 30.        # m/s
Vy = 10.        # m/s  - use 40 here, get 250 m driv

f = 1.8           # frequency
fieldSize = 20.  # m
bHeight = 4.    # m
tspan = [0., 5.]
initial = [0., 0, Vy]

# Vx h = distance travelled in time h
# set MaxStep so that Vx MaxStep = 1, so time stepping can't
# pass through 1 foot wide barrier in one step

#========= Model Functions ==========
def barrier_height(t, bh, f):
    return bh + 1.5*np.cos(2.*np.pi*f*t)

def golf(t, z, Vx):
    return np.array([Vx, z[2], -9.81])

def hit_ground(t,z):
    return z[1]
hit_ground.terminal = True
hit_ground.direction = -1

def hit_barrier(t, z, fieldSize, bHeight, f):
    bDyn = barrier_height(t, bHeight, f)
    event2 = max( abs(z[0]-fieldSize)-0.5 , z[1]-bDyn )
    return event2
hit_barrier_w = lambda t,z: hit_barrier(t,z,fieldSize,bHeight,f)
hit_barrier_w.terminal = True
hit_barrier_w.direction = -1
#=====================================

# Set up animation code
fig = plt.figure(figsize=[15,5])
ax = fig.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')
plt.axis('equal')
barrier, = plt.plot([],[], 'b')

def init():
    ax.set_xlim(0, 60.)
    ax.set_ylim(0, 20)
    return ln, barrier

def update(frame):
    t = frame[0]
    xdata = frame[1]
    ydata = frame[2]
    ln.set_data(xdata, ydata)
    bDyn = barrier_height(t, bHeight, f)
    xbarrier = [fieldSize-0.5, fieldSize-0.5, fieldSize+0.5, fieldSize+0.5]
    ybarrier = [0, bDyn, bDyn, 0]
    barrier.set_data(xbarrier, ybarrier)
    return ln, barrier


for k in range(50):
    # Run the simulation
    Vx = 22. + 10.*np.random.rand()
    Vy = 19. + 5*np.random.rand()
    f = 1.+2.*np.random.rand()
    fieldSize = 40.
    bHeight = 4.
    fun = lambda t,z: golf(t,z,Vx)
    efun = [hit_ground, hit_barrier_w]
    fps = 60.
    tt = np.arange(tspan[0], tspan[1], 1./fps)
    sol = solve_ivp(fun, tspan, initial, max_step=1./(4.*Vx), events=efun, t_eval=tt)

    anim = FuncAnimation(fig, update, frames=zip(sol.t, sol.y[0], sol.y[1]),
                        init_func=init, blit=True, interval=2000/fps, save_count=len(sol.t))
    plt.show()
    plt.pause(3.2*sol.t[-1]) # adjust this if it behaves oddly




