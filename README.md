# ICRA-quiz

This program simulate a simple pendulum with python.

## Preparation

Firstly, import the required packages.

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
```

## About the code

Create a class of pendulum movement, including the function of computing the position and update each t time.

```python
class SimplePendulum:
...
```

Generate a SimplePendulum 

```python
pendulum = SimplePendulum(40)
t = 0.03
```
Create UI
```python
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, 
                     xlim=(-2, 2), ylim=(-2, 2))
ax.grid()
line, = ax.plot([], [], 'o-', lw=2, color='black')
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
```

Create animation function
```python
def init():
...
def animate(i):
...
```

Finally set the time and call function.
