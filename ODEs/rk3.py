
import numpy as np
from matplotlib.pyplot import plot, xlabel, ylabel, title, axis, ion, figure, cla, draw
ion()

# Can change these 2 lines
method = 2 # 1 or 2
de = 1 # 1 or 2

y0 = 2
t0 = 0
h = 1

tt = np.linspace(0,1,20);

if method==1:
    c2 = 1/3; c3 = 2/3;
    w1 = 1/4; w2 = 0; w3 = 3/4;
    a21 = 1/3; a31 = 0; a32 = 2/3;
elif method==2:
    c2 = 1/2; c3 = 3/4;
    w1 = 2/9; w2 = 3/9; w3 = 4/9;
    a21 = 1/2; a31 = 0; a32 = 3/4;

if de==1:
    soln = lambda t, t0, y0: np.exp(-t0)*(y0+t0+1)*np.exp(t) - t - 1
    my_de = lambda t,y: t+y
    #yy = soln(tt, t0, y0);
    #yy = 3*exp(tt) - tt - 1;
    axis_limits = [0, 1, 1, 7];
elif de==2:
    soln = lambda t, t0, y0: np.exp(t0)*(y0-t0+1)*np.exp(-t) + t - 1
    my_de = lambda t,y: t-y
    #yy = 2*exp(0.5*tt.^2);
    axis_limits = [0, 1, -2, 3];
elif de==3:
    soln = lambda t, t0, y0: np.exp(-t0)*(y0 - t0 - 1) * np.exp(t) + t + 1
    my_de = lambda t,y: y-t
    #yy = 2*exp(-tt) + tt - 1;
    axis_limits = [0, 1, 0, 5];

yy = soln(tt, t0, y0)
figure(1, figsize=[10,10])
cla()
plot(tt,yy)
axis(axis_limits)

# Plot a whole bunch of solutions
mygray = [0.8, 0.8, 0.8]
for a in np.arange(-2, 7, 0.2):
    plot(tt, soln(tt, t0, a), color=mygray, linewidth=1)

#figure(1, figsize=[18,18])
plot(tt,yy, 'b', lineWidth=3)
draw()

input('Hit return')

k1 = h * my_de(t0,y0)
plot([t0, t0+h], [y0, y0+k1], 'g',lineWidth=2)
draw()
input('Hit return')

k2 = h * my_de(t0+h*c2, y0+k1*a21)
plot([t0+h*c2, t0+h], [y0+k1*a21, y0+k1*a21+k2*(1-a21)], 'r', lineWidth=2)
draw()
input('Hit return')


cla()
plot(tt,yy)
axis(axis_limits)

# Solutions
for a in np.arange(-2, 7, 0.2):
    plot(tt, soln(tt, t0, a), color=mygray)
plot(tt,yy, 'b', lineWidth=3)
plot([t0, t0+h], [y0, y0+k1], 'g', lineWidth=2)
plot([t0, t0+h], [y0, y0+k2], 'g', lineWidth=2)
draw()
input('Hit return')

k3 = h * my_de(t0+h*c3, y0+k1*a31+k2*a32)
plot([t0+h*c3, t0+h], [y0+k1*a31+k2*a32, y0+k1*a31+k2*a32+k3*(1-a31-a32)], 'r',lineWidth=2)
draw()
input('Hit return')

cla()
plot(tt,yy)
axis(axis_limits)

# Plot a whole bunch of solutions
for a in np.arange(-2, 7, 0.2):
    plot(tt, soln(tt, t0, a), color=mygray)
plot(tt,yy, 'b', lineWidth=3)
plot([t0, t0+h], [y0, y0+k1],'g',lineWidth=2)
plot([t0, t0+h], [y0, y0+k2],'g',lineWidth=2)
plot([t0, t0+h], [y0, y0+k3],'g',lineWidth=2)
draw()
input('Hit return')

y = y0 + k1*w1 + k2*w2 + k3*w3

plot([t0, t0+h], [y0, y],'ko', markersize=10)




