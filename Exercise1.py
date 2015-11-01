# Imports
import matplotlib.pyplot as plt
import numpy as np

# Defining array range
x = np.arange(0, 2*np.pi, 0.01)

# Create a new subplot from a grid 
fig, ax = plt.subplots(1)

# Plot cosine using blue color with a continuous line of width 1 (pixels)
ax.plot(x, np.cos(x),'-b',label='cosine')

# Plot sine using red color with a continuous line of width 1 (pixels)
ax.plot(x, np.sin(x),'-r',label='sine')

# Set y limits
plt.ylim(-1.5,1.5)

# Customizing the plot: Axes Labels and Title
plt.title('Plots of the sine and cosine function')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Setting ticks & ticks labels
plt.xticks([0., .5*np.pi, np.pi, 1.5*np.pi, 2*np.pi],["$0$", r"$\frac{1}{2}\pi$",
                                                     r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
# Adding a legend
plt.legend(loc='best')

# Show result on screen
plt.show()
