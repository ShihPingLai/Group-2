%matplotlib inline
import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

#set initial condition(m,s)
x=6371000 #radius of earth
y=0.
v=7000
g=9.8
angle0=60

#in x,y represent
r=(x**2+y**2)**0.5
pro_deg= np.deg2rad(angle0)
vx=v*math.cos(pro_deg)
vy=v*math.sin(pro_deg)

#record initial condition
x0=x
y0=y
v0=v
g0=g
r0=r

#lists record position
x_lst=[x0]
y_lst=[y0]
r_lst=[r0]

#caculate the state next 0.1sec
t=0
dt=0.1
while r>=r0:
    #we must consider gravity in radial direction, using theta
    r=(x**2+y**2)**0.5
    cos_theta= x/r
    sin_theta= y/r
    gx=-g0*((r0**2)/(r**2))*cos_theta
    gy=-g0*((r0**2)/(r**2))*sin_theta
    
    #then we try to caculate
    vx += gx*dt
    vy += gy*dt
    x  += vx*dt
    y  += vy*dt
    t  += dt
    #record position in lists
    x_lst.append(x)
    y_lst.append(y)
    r_lst.append(r)

#I just want to draw a circle    
cx_lst=[]
cy_lst=[]
for i in range(200):
    cx = 6371000*math.cos(6.29*i/200)
    cy = 6371000*math.sin(6.29*i/200)
    cx_lst.append(cx)
    cy_lst.append(cy)



#simply plot   
plt.figure(figsize=(10, 10))
plt.ylim(-15000000, 15000000)
plt.xlim(-15000000, 15000000)
plt.plot(cx_lst,cy_lst)
plt.plot(x_lst,y_lst)
plt.show()      

print "INFORMATION"
print "Launching Position:(",int(x0),",",int(y0),")" 
print "Launching speed:", int(v0), "m/s"
print "launching Angle:", int(angle0), "degree"
print "Time Require:", int(t), "sec"
print "Landing Position:(",int(x),",",int(y),")"

# New figure with white background
fig = plt.figure(figsize=(6,6), facecolor='white')

# New axis over the whole figure, no frame and a 1:1 aspect ratio
ax = fig.add_axes([0,0,1,1], frameon=False, aspect=1)

p = np.column_stack((cx_lst, cy_lst))
scat = ax.scatter(p[:,0], p[:,1])


def update(frame):
    i=frame % 19789
    global x_lst,y_lst,cx_lst,cy_lst,p
    cx_lst.append(x_lst[i])
    cy_lst.append(y_lst[i])
    scat.set_offsets(p)
    return scat,

animation = FuncAnimation(fig, update, interval=10, blit=True, frames=19789)
# animation.save('rain.gif', writer='imagemagick', fps=30, dpi=40)
plt.show()
