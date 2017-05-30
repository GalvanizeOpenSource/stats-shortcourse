#!/usr/bin/env python 
"""
fit a bernoulli distribution with several parameterizations
"""

import sys,os
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as scs

## declare variables
font_size = 11
font_name = 'sans-serif'
n = 10000
fig = plt.figure(figsize=(10,6),dpi=300)
splot = 0

## loop through parameterizations of the beta
for lamb in [1.0,2.0,5.0]:
    splot += 1
    ax = fig.add_subplot(1,3,splot)
    
    x = np.arange(scs.poisson.ppf(0.01, lamb),scs.poisson.ppf(0.99, lamb))
    ax.plot(x, scs.poisson.pmf(x, lamb), 'bo', ms=8, label='pmf')
    ax.vlines(x, 0, scs.poisson.pmf(x, lamb), colors='b', lw=5, alpha=0.5)
    rv = scs.poisson(lamb)

    ax.set_xlim((-0.5,10.5))
    ax.set_ylim((0,0.6))
    ax.set_title("lambda=%s"%(lamb))
    ax.set_aspect(1./ax.get_data_ratio())

    for t in ax.get_xticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    for t in ax.get_yticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
plt.savefig("poisson.png",dpi=400)
plt.show()
