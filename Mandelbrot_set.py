# -*- coding: utf-8 -*-
"""
Implementation of the Mandelbrot set in Python.

@author: Tomas Arzola Röber
"""

import numpy as np
import matplotlib.pyplot as plt

# Region of the mandelbrot set
xmin, xmax = -1.940158209, -1.940156455
ymin, ymax = -1.22e-7, -0.000001525
# Resolution
width, height = 1920, 1080
# Number of iterations
max_iter = 256

img = np.zeros((height, width, 3), dtype=np.uint8)
x = np.linspace(xmin, xmax, width)
y = np.linspace(ymin, ymax, height)

# Colors
psychedelic_colors = [
    (70, 70, 70),
    (30, 30, 30),
    (128, 0, 0),
    (0, 128, 0),
    (128, 128, 0),
    (128, 0, 128),
    (255, 69, 0),
    (0, 0, 0)
]

# Recursion for the mandelbrot set
for i in range(width):
    for j in range(height):
        zx, zy = x[i], y[j]
        c = zx + zy * 1j
        z = c
        for k in range(max_iter):
            if abs(z) > 2.0:
                break
            z = z * z + c
        color_index = k % len(psychedelic_colors)
        img[j, i, :] = psychedelic_colors[color_index]

# Visualization of the mandelbrot set for the region
fig, ax = plt.subplots(figsize=(width/100, height/100), dpi=100)
ax.imshow(img, extent=(xmin, xmax, ymin, ymax))
ax.axis('off')
plt.show()