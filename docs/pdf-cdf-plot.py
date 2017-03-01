#!/usr/bin/env python
"""
generally illustrate the concept of a cdf and pdf
"""

import numpy as np
import matplotlib.pyplot as plt

# Create some test data
dx = .01
X  = np.arange(-2,2,dx)
Y  = np.exp(-X**2)

# Normalize the data to a proper PDF
Y /= (dx*Y).sum()

# Compute the CDF
CY = np.cumsum(Y*dx)

# Plot both
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)
p1 = ax.plot(X,Y)
p2 = ax. plot(X,CY,'r--')
ax.legend([p1[0],p2[0]],["pdf","cdf"],loc="upper left")
plt.show()
