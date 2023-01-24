import noise
import numpy as np
import matplotlib.pyplot as plt
import random

# Define the size of the clouds
width = 800
height = 800

# Create a numpy array to hold the fractal clouds
clouds = np.zeros((height, width))

# Define the properties of the fractal clouds
octaves = 8
persistence = 0.5
lacunarity = 2.0
scale = 100.0

# Generate the fractal clouds
for y in range(height):
    for x in range(width):
        clouds[y][x] = noise.pnoise2(x / scale, y / scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)

# Normalize the fractal clouds
clouds = (clouds + 1) / 2

# Create a figure and axes
fig, ax = plt.subplots()

# Plot the fractal clouds
ax.imshow(clouds, cmap='gray')

# Add the colorbar
fig.colorbar(ax.imshow(clouds, cmap='gray'))

# Show the plot
plt.show()
