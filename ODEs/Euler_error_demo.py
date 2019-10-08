import numpy as np
from matplotlib.pyplot import ion, plot, axis, figure, xlabel, ylabel, title, legend, cla, clf, pause, draw
ion()

# Can change this line
de = 2 # 1 or 2 or 3
auto_pause = False    # 0 to control with buttons, 1 for auto

y0 = 2
t0 = -1
tf = 1.5

c2 = [0.2, 0.2, 1]
c1 = [1, 0.7, 0.4]
tt = np.linspace(t0,tf,100)

if de==1:
    soln = lambda t, t0, y0: np.exp(-t0)*(y0+t0+1)*np.exp(t) - t - 1
    my_de = lambda t,y: t+y
    axis_limits = [-1, 1, 0, 10]
    # Initial conditions
    t0 = -1
    y0 = 1.7
elif de==2:
    soln = lambda t, t0, y0: np.exp(t0)*(y0-t0+1)*np.exp(-t) + t - 1
    my_de = lambda t,y: t-y
    axis_limits = [-1, 1, -1, 2]
    t0 = -1
    y0 = 2
elif de==3:
    # dydt = t - y
    soln = lambda t, t0, y0: np.exp(-t0)*(y0 - t0 - 1) * np.exp(t) + t + 1
    my_de = lambda t,y: y-t
    axis_limits = [-1, 1, -1, 8]
    t0 = -1
    y0 = 0.5

# Plot a whole bunch of solutions
mygray = [0.8, 0.8, 0.8]
figure(1, figsize=[10,10])
clf()
for a in np.arange(-5, 10, 0.1):
    plot(tt, soln(tt, t0, a), color=mygray)
axis(axis_limits)
draw()

tc = t0
yc = y0
if auto_pause==0:
    h = 0.5
    lw = 2
    ms = 10
else:
    h = 0.05
    lw = 1
    ms = 5


steps = int( np.ceil( (tf-h-t0)/h ) )
yEuler = np.zeros(steps+1)
tEuler = np.zeros(steps+1)
n = 0

yEuler = [y0]
tEuler = [t0]

if auto_pause:
    pause(0.05)
else:
    input('Hit Enter')


for n in range(steps):
    
    # Plot current solution curve
    plot(tt,soln(tt,tc,yc), color=c1, lineWidth=lw)
    draw()
    if auto_pause:
        pause(0.05)
    else:
        input('Hit Enter')

    # Euler step
    F = my_de(tc, yc)
    ynext = yc + h*F
    ynext_true = soln(tc+h,tc,yc)
    plot([tc, tc+h], [yc, ynext], color=c2, lineWidth=2)
    draw()
    if auto_pause:
        pause(0.05)
    else:
        input('Hit Enter')
    plot([tc+h, tc+h], [ynext, ynext_true],'r', lineWidth=2)
    draw()

    yEuler.append(ynext)
    tEuler.append(tc+h)
    
    # Set up for next step
    tc = tc+h
    yc = ynext
    if auto_pause:
        pause(0.05)
    else:
        input('Hit Enter')

plot(tEuler, yEuler, 'k.', markersize=ms)





