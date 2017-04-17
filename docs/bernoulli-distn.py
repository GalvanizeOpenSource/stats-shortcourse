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
fig = plt.figure(figsize=(10,6))
splot = 0

## loop through parameterizations of the beta
for p in [0.3,0.6,0.9]:
    splot += 1
    ax = fig.add_subplot(1,3,splot)
    
    x = np.arange(scs.bernoulli.ppf(0.01, p),scs.bernoulli.ppf(0.99, p)+1)
    ax.plot(x, scs.bernoulli.pmf(x, p), 'bo', ms=8, label='pmf')
    ax.vlines(x, 0, scs.bernoulli.pmf(x, p), colors='b', lw=5, alpha=0.5)
    rv = scs.bernoulli(p)
    
    ax.set_ylim((0,1.0))
    ax.set_xlim((-0.25, 1.25))
    ax.set_title("p=%s"%(p))
    ax.set_aspect(1./ax.get_data_ratio())

    for t in ax.get_xticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)
    for t in ax.get_yticklabels():
        t.set_fontsize(font_size-1)
        t.set_fontname(font_name)

plt.savefig("bernoulli-distn.png", dpi=400)
plt.show()
