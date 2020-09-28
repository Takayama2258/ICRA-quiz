import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import time

class SimplePendulum:
    """create a class of pendulum movement"""
    def __init__(self,
                 init_angle=45,
                 L=1.0, 
                 G=9.8, 
                 origin=(0,0)): 
        self.L = L
        self.G = G
        self.origin = origin
        self.time = 0
        self.init_angle = init_angle * np.pi / 180.
        self.angle = self.init_angle
    
    def step(self, t):
      
        self.time += t
        self.angle = self.init_angle * np.cos(np.sqrt( self.G / self.L) * self.time)
    
    def position(self):
        """calculate the updating position"""
        x = np.cumsum([self.origin[0], self.L * np.sin(self.angle)])
        y = np.cumsum([self.origin[1], -self.L * np.cos(self.angle)])
        return (x, y)

pendulum = SimplePendulum(40)
t = 0.01

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, 
                     xlim=(-2, 2), ylim=(-2, 2))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2, color='yellow')
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

def init():
    
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

def animate(i):
    
    global pendulum, t
    pendulum.step(t)
    
    line.set_data(*pendulum.position())
    return line


t0 = time()
animate(0)
t1 = time()
interval = 1000 * t - (t1 - t0)

ani = animation.FuncAnimation(fig,
                              animate,
                              frames=300,
                              interval=interval,
                              blit=False,
                              init_func=init)

plt.show()
